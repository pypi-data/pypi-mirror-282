# -*- coding: UTF-8 -*-
"""Classes for working with astronomical alerts."""
import base64
import importlib.resources
import io
import logging
from datetime import datetime
from pathlib import Path
from typing import TYPE_CHECKING, Any, Mapping, Union

import fastavro
from attrs import define, field

from . import registry, types_, utils
from .exceptions import BadRequest, OpenAlertError, SchemaNotFoundError

if TYPE_CHECKING:
    import google.cloud.pubsub_v1
    import pandas as pd  # always lazy-load pandas. it hogs memory on cloud functions and run

LOGGER = logging.getLogger(__name__)
PACKAGE_DIR = importlib.resources.files(__package__)


@define(kw_only=True)
class Alert:
    """Container for an astronomical alert.

    Instances of this class are returned by other calls like :meth:`pittgoogle.Subscription.pull_batch`,
    so it is often not necessary to instantiate this directly.
    In cases where you do want to create an `Alert` directly, use one of the `from_*` methods like
    :meth:`pittgoogle.Alert.from_dict`.

    All parameters are keyword only.

    Args:
        bytes (bytes, optional):
            The message payload, as returned by Pub/Sub. It may be Avro or JSON serialized depending
            on the topic.
        dict (dict, optional):
            The message payload as a dictionary.
        metadata (dict, optional):
            The message metadata.
        msg (google.cloud.pubsub_v1.types.PubsubMessage, optional):
            The Pub/Sub message object, documented at
            `<https://cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.PubsubMessage>`__.
        schema_name (str):
            Schema name of the alert. Used for unpacking. If not provided, some properties of the
            `Alert` may not be available. See :meth:`pittgoogle.Schemas.names` for a list of options.
    """

    # Use "Union" because " | " is throwing an error when combined with forward references.
    msg: Union["google.cloud.pubsub_v1.types.PubsubMessage", types_.PubsubMessageLike, None] = (
        field(default=None)
    )
    _attributes: Mapping[str, str] | None = field(default=None)
    _dict: Mapping | None = field(default=None)
    _dataframe: Union["pd.DataFrame", None] = field(default=None)
    schema_name: str | None = field(default=None)
    _schema: types_.Schema | None = field(default=None, init=False)
    path: Path | None = field(default=None)

    # ---- class methods ---- #
    @classmethod
    def from_cloud_run(cls, envelope: Mapping, schema_name: str | None = None) -> "Alert":
        """Create an `Alert` from an HTTP request envelope containing a Pub/Sub message, as received by a Cloud Run module.

        Args:
            envelope (dict):
                The HTTP request envelope containing the Pub/Sub message.
            schema_name (str, optional):
                The name of the schema to use. Defaults to None.

        Returns:
            Alert:
                An instance of the `Alert` class.

        Raises:
            BadRequest:
                If the Pub/Sub message is invalid or missing.

        Example:
            Code for a Cloud Run module that uses this method to open a ZTF alert:

        .. code-block:: python

            import pittgoogle
            # flask is used to work with HTTP requests, which trigger Cloud Run modules
            # the request contains the Pub/Sub message, which contains the alert packet
            import flask

            app = flask.Flask(__name__)

            # function that receives the request
            @app.route("/", methods=["POST"])
            def index():

                try:
                    # unpack the alert
                    # if the request does not contain a valid message, this raises a `BadRequest`
                    alert = pittgoogle.Alert.from_cloud_run(envelope=flask.request.get_json(), schema_name="ztf")

                except pittgoogle.exceptions.BadRequest as exc:
                    # return the error text and an HTTP 400 Bad Request code
                    return str(exc), 400

                # continue processing the alert
                # when finished, return an empty string and an HTTP success code
                return "", 204
        """
        # check whether received message is valid, as suggested by Cloud Run docs
        if not envelope:
            raise BadRequest("Bad Request: no Pub/Sub message received")
        if not isinstance(envelope, dict) or "message" not in envelope:
            raise BadRequest("Bad Request: invalid Pub/Sub message format")

        # convert the message publish_time string -> datetime
        # occasionally the string doesn't include microseconds so we need a try/except
        publish_time = envelope["message"]["publish_time"].replace("Z", "+00:00")
        try:
            publish_time = datetime.strptime(publish_time, "%Y-%m-%dT%H:%M:%S.%f%z")
        except ValueError:
            publish_time = datetime.strptime(publish_time, "%Y-%m-%dT%H:%M:%S%z")

        return cls(
            msg=types_.PubsubMessageLike(
                # data is required. the rest should be present in the message, but use get to be lenient
                data=base64.b64decode(envelope["message"]["data"].encode("utf-8")),
                attributes=envelope["message"].get("attributes"),
                message_id=envelope["message"].get("message_id"),
                publish_time=publish_time,
                ordering_key=envelope["message"].get("ordering_key"),
            ),
            schema_name=schema_name,
        )

    @classmethod
    def from_dict(
        cls,
        payload: Mapping,
        attributes: Mapping[str, str] | None = None,
        schema_name: str | None = None,
    ) -> "Alert":
        """Create an `Alert` object from the given `payload` dictionary.

        Args:
            payload (dict):
                The dictionary containing the data for the `Alert` object.
            attributes (Mapping[str, str], None):
                Additional attributes for the `Alert` object. Defaults to None.
            schema_name (str, None):
                The name of the schema. Defaults to None.

        Returns:
            Alert:
                An instance of the `Alert` class.
        """
        return cls(dict=payload, attributes=attributes, schema_name=schema_name)

    @classmethod
    def from_msg(
        cls, msg: "google.cloud.pubsub_v1.types.PubsubMessage", schema_name: str | None = None
    ) -> "Alert":
        """Create an `Alert` object from a `google.cloud.pubsub_v1.types.PubsubMessage`.

        Args:
            msg (google.cloud.pubsub_v1.types.PubsubMessage):
                The PubsubMessage object to create the Alert from.
            schema_name (str, optional):
                The name of the schema to use for the Alert. Defaults to None.

        Returns:
            Alert:
                The created `Alert` object.
        """
        return cls(msg=msg, schema_name=schema_name)

    @classmethod
    def from_path(cls, path: str | Path, schema_name: str | None = None) -> "Alert":
        """Creates an `Alert` object from the file at the specified `path`.

        Args:
            path (str or Path):
                The path to the file containing the alert data.
            schema_name (str, optional):
                The name of the schema to use for the alert. Defaults to None.

        Returns:
            Alert:
                An instance of the `Alert` class.

        Raises:
            FileNotFoundError:
                If the file at the specified `path` does not exist.
            IOError:
                If there is an error reading the file.
        """
        with open(path, "rb") as f:
            bytes_ = f.read()
        return cls(
            msg=types_.PubsubMessageLike(data=bytes_), schema_name=schema_name, path=Path(path)
        )

    # ---- properties ---- #
    @property
    def attributes(self) -> Mapping:
        """Return the alert's custom metadata.

        If this was not provided (typical case), this attribute will contain a copy of
        the incoming :attr:`Alert.msg.attributes`.

        You may update this dictionary as desired. If you publish this alert using
        :attr:`pittgoogle.Topic.publish`, this dictionary will be sent as the outgoing
        message's Pub/Sub attributes.
        """
        if self._attributes is None:
            self._attributes = dict(self.msg.attributes)
        return self._attributes

    @property
    def dict(self) -> Mapping:
        """Return the alert data as a dictionary.

        If this was not provided (typical case), this attribute will contain the deserialized
        alert bytes stored in the incoming :attr:`Alert.msg.data` as a dictionary.

        You may update this dictionary as desired. If you publish this alert using
        :attr:`pittgoogle.Topic.publish`, this dictionary will be sent as the outgoing
        Pub/Sub message's data payload.

        Note: The following is required in order to deserialize the incoming alert bytes.
        The bytes can be in either Avro or JSON format, depending on the topic.
        If the alert bytes are Avro and contain the schema in the header, the deserialization can
        be done without requiring :attr:`Alert.schema`. However, if the alert bytes are
        schemaless Avro, the deserialization requires the :attr:`Alert.schema.avsc` attribute to
        contain the schema definition.

        Returns:
            dict:
                The alert data as a dictionary.

        Raises:
            OpenAlertError:
                If unable to deserialize the alert bytes.
        """
        if self._dict is not None:
            return self._dict

        # [TODO] Add a `required` attribute to types_.Schema (whether the schema is required in order to deserialize the alerts).
        # deserialize self.msg.data (avro or json bytestring) into a dict.
        # if self.msg.data is either (1) json; or (2) avro that contains the schema in the header,
        # self.schema is not required for deserialization, so we want to be lenient.
        # if self.msg.data is schemaless avro, deserialization requires self.schema.avsc to exist.
        # currently, there is a clean separation between surveys:
        #     elasticc always requires self.schema.avsc; ztf never does.
        # we'll check the survey name from self.schema.survey; but first we need to check whether
        # the schema exists so we can try to continue without one instead of raising an error.
        # we may want or need to handle this differently in the future.
        try:
            self.schema
        except SchemaNotFoundError as exc:
            LOGGER.warning(f"schema not found. attempting to deserialize without it. {exc}")
            avro_schema = None
        else:
            if self.schema.survey in ["elasticc"]:
                avro_schema = self.schema.avsc
            else:
                avro_schema = None

        # if we have an avro schema, use it to deserialize and return
        if avro_schema:
            with io.BytesIO(self.msg.data) as fin:
                self._dict = fastavro.schemaless_reader(fin, avro_schema)
            return self._dict

        # [TODO] this should be rewritten to catch specific errors
        # for now, just try avro then json, catching basically all errors in the process
        try:
            self._dict = utils.Cast.avro_to_dict(self.msg.data)
        except Exception:
            try:
                self._dict = utils.Cast.json_to_dict(self.msg.data)
            except Exception:
                raise OpenAlertError("failed to deserialize the alert bytes")
        return self._dict

    @property
    def dataframe(self) -> "pd.DataFrame":
        """Return a pandas DataFrame containing the source detections."""
        if self._dataframe is not None:
            return self._dataframe

        import pandas as pd  # always lazy-load pandas. it hogs memory on cloud functions and run

        # sources and previous sources are expected to have the same fields
        sources_df = pd.DataFrame([self.get("source")] + self.get("prv_sources"))
        # sources and forced sources may have different fields
        forced_df = pd.DataFrame(self.get("prv_forced_sources"))

        # use nullable integer data type to avoid converting ints to floats
        # for columns in one dataframe but not the other
        sources_ints = [c for c, v in sources_df.dtypes.items() if v == int]
        sources_df = sources_df.astype(
            {c: "Int64" for c in set(sources_ints) - set(forced_df.columns)}
        )
        forced_ints = [c for c, v in forced_df.dtypes.items() if v == int]
        forced_df = forced_df.astype(
            {c: "Int64" for c in set(forced_ints) - set(sources_df.columns)}
        )

        self._dataframe = pd.concat([sources_df, forced_df], ignore_index=True)
        return self._dataframe

    @property
    def alertid(self) -> str | int:
        """Return the alert ID. Convenience wrapper around :attr:`Alert.get`.

        If the survey does not define an alert ID, this returns the `sourceid`.
        """
        return self.get("alertid", self.sourceid)

    @property
    def objectid(self) -> str | int:
        """Return the object ID. Convenience wrapper around :attr:`Alert.get`.

        The "object" represents a collection of sources, as determined by the survey.
        """
        return self.get("objectid")

    @property
    def sourceid(self) -> str | int:
        """Return the source ID. Convenience wrapper around :attr:`Alert.get`.

        The "source" is the detection that triggered the alert.
        """
        return self.get("sourceid")

    @property
    def schema(self) -> types_.Schema:
        """Return the schema from the :class:`pittgoogle.Schemas` registry.

        Raises:
            pittgoogle.exceptions.SchemaNotFoundError:
                If the `schema_name` is not supplied or a schema with this name is not found.
        """
        if self._schema is not None:
            return self._schema

        # need to load the schema. raise an error if no schema_name given
        if self.schema_name is None:
            raise SchemaNotFoundError("a schema_name is required")

        # this also may raise SchemaNotFoundError
        self._schema = registry.Schemas.get(self.schema_name)
        return self._schema

    # ---- methods ---- #
    def add_id_attributes(self) -> None:
        """Add the IDs ("alertid", "objectid", "sourceid") to :attr:`Alert.attributes`."""
        ids = ["alertid", "objectid", "sourceid"]
        values = [self.get(id) for id in ids]

        # get the survey-specific field names
        survey_names = [self.get_key(id) for id in ids]
        # if the field is nested, the key will be a list
        # but pubsub message attributes must be strings. join to avoid a future error on publish
        names = [".".join(id) if isinstance(id, list) else id for id in survey_names]

        # only add to attributes if the survey has defined this field
        for idname, idvalue in zip(names, values):
            if idname is not None:
                self.attributes[idname] = idvalue

    def get(self, field: str, default: Any = None) -> Any:
        """Return the value of a field from the alert data.

        Parameters:
            field (str):
                Name of a field. This must be one of the generic field names used by Pitt-Google
                (keys in :attr:`Alert.schema.map`). To use a survey-specific field name instead, use
                :attr:`Alert.dict.get`.
            default (str, optional):
                The default value to be returned if the field is not found.

        Returns:
            any:
                The value in the :attr:`Alert.dict` corresponding to the field.
        """
        survey_field = self.schema.map.get(field)  # str, list[str], or None

        if survey_field is None:
            return default

        if isinstance(survey_field, str):
            return self.dict.get(survey_field, default)

        # if survey_field is not one of the expected types, the schema map is malformed
        # maybe this was intentional, but we don't know how to handle it here
        if not isinstance(survey_field, list):
            raise TypeError(
                f"field lookup not implemented for a schema-map value of type {type(survey_field)}"
            )

        # the list must have more than 1 item, else it would be a single str
        if len(survey_field) == 2:
            try:
                return self.dict[survey_field[0]][survey_field[1]]
            except KeyError:
                return default

        if len(survey_field) == 3:
            try:
                return self.dict[survey_field[0]][survey_field[1]][survey_field[2]]
            except KeyError:
                return default

        raise NotImplementedError(
            f"field lookup not implemented for depth {len(survey_field)} (key = {survey_field})"
        )

    def get_key(
        self, field: str, name_only: bool = False, default: str | None = None
    ) -> str | list[str] | None:
        """Return the survey-specific field name.

        Args:
            field (str):
                Generic field name whose survey-specific name is to be returned. This must be one of the
                keys in the dict `self.schema.map`.
            name_only (bool):
                In case the survey-specific field name is nested below the top level, whether to return
                just the single final name as a str (True) or the full path as a list[str] (False).
            default (str or None):
                Default value to be returned if the field is not found.

        Returns:
            str or list[str]):
                Survey-specific name for the `field`, or `default` if the field is not found.
                list[str] if this is a nested field and `name_only` is False, else str with the
                final field name only.
        """
        survey_field = self.schema.map.get(field)  # str, list[str], or None

        if survey_field is None:
            return default

        if name_only and isinstance(survey_field, list):
            return survey_field[-1]

        return survey_field
