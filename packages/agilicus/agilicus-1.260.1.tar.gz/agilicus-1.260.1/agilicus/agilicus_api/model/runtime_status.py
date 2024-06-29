"""
    Agilicus API

    Agilicus is API-first. Modern software is controlled by other software, is open, is available for you to use the way you want, securely, simply.  The OpenAPI Specification in YAML format is available on [www](https://www.agilicus.com/www/api/agilicus-openapi.yaml) for importing to other tools.  A rendered, online viewable and usable version of this specification is available at [api](https://www.agilicus.com/api). You may try the API inline directly in the web page. To do so, first obtain an Authentication Token (the simplest way is to install the Python SDK, and then run `agilicus-cli --issuer https://MYISSUER get-token`). You will need an org-id for most calls (and can obtain from `agilicus-cli --issuer https://MYISSUER list-orgs`). The `MYISSUER` will typically be `auth.MYDOMAIN`, and you will see it as you sign-in to the administrative UI.  This API releases on Bearer-Token authentication. To obtain a valid bearer token you will need to Authenticate to an Issuer with OpenID Connect (a superset of OAUTH2).  Your \"issuer\" will look like https://auth.MYDOMAIN. For example, when you signed-up, if you said \"use my own domain name\" and assigned a CNAME of cloud.example.com, then your issuer would be https://auth.cloud.example.com.  If you selected \"use an Agilicus supplied domain name\", your issuer would look like https://auth.myorg.agilicus.cloud.  For test purposes you can use our [Python SDK](https://pypi.org/project/agilicus/) and run `agilicus-cli --issuer https://auth.MYDOMAIN get-token`.  This API may be used in any language runtime that supports OpenAPI 3.0, or, you may use our [Python SDK](https://pypi.org/project/agilicus/), our [Typescript SDK](https://www.npmjs.com/package/@agilicus/angular), or our [Golang SDK](https://git.agilicus.com/pub/sdk-go).  100% of the activities in our system our API-driven, from our web-admin, through our progressive web applications, to all internals: there is nothing that is not accessible.  For more information, see [developer resources](https://www.agilicus.com/developer).   # noqa: E501

    The version of the OpenAPI document: 2024.06.21
    Contact: dev@agilicus.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from agilicus_api.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from agilicus_api.exceptions import ApiAttributeError



class RuntimeStatus(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('overall_status',): {
            'GOOD': "good",
            'WARN': "warn",
            'DOWN': "down",
            'STALE': "stale",
            'DEGRADED': "degraded",
        },
    }

    validations = {
    }

    @property
    def overall_status(self):
       return self.get("overall_status")

    @overall_status.setter
    def overall_status(self, new_value):
       self.overall_status = new_value

    @property
    def running_replicas(self):
       return self.get("running_replicas")

    @running_replicas.setter
    def running_replicas(self, new_value):
       self.running_replicas = new_value

    @property
    def error_message(self):
       return self.get("error_message")

    @error_message.setter
    def error_message(self, new_value):
       self.error_message = new_value

    @property
    def restarts(self):
       return self.get("restarts")

    @restarts.setter
    def restarts(self, new_value):
       self.restarts = new_value

    @property
    def cpu(self):
       return self.get("cpu")

    @cpu.setter
    def cpu(self, new_value):
       self.cpu = new_value

    @property
    def memory(self):
       return self.get("memory")

    @memory.setter
    def memory(self, new_value):
       self.memory = new_value

    @property
    def last_apply_time(self):
       return self.get("last_apply_time")

    @last_apply_time.setter
    def last_apply_time(self, new_value):
       self.last_apply_time = new_value

    @property
    def updated(self):
       return self.get("updated")

    @updated.setter
    def updated(self, new_value):
       self.updated = new_value

    @property
    def running_image(self):
       return self.get("running_image")

    @running_image.setter
    def running_image(self, new_value):
       self.running_image = new_value

    @property
    def running_hash(self):
       return self.get("running_hash")

    @running_hash.setter
    def running_hash(self, new_value):
       self.running_hash = new_value

    @property
    def org_id(self):
       return self.get("org_id")

    @org_id.setter
    def org_id(self, new_value):
       self.org_id = new_value

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'overall_status': (str,),  # noqa: E501
            'running_replicas': (int,),  # noqa: E501
            'error_message': (str,),  # noqa: E501
            'restarts': (int,),  # noqa: E501
            'cpu': (float,),  # noqa: E501
            'memory': (float,),  # noqa: E501
            'last_apply_time': (datetime,),  # noqa: E501
            'updated': (datetime,),  # noqa: E501
            'running_image': (str,),  # noqa: E501
            'running_hash': (str,),  # noqa: E501
            'org_id': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'overall_status': 'overall_status',  # noqa: E501
        'running_replicas': 'running_replicas',  # noqa: E501
        'error_message': 'error_message',  # noqa: E501
        'restarts': 'restarts',  # noqa: E501
        'cpu': 'cpu',  # noqa: E501
        'memory': 'memory',  # noqa: E501
        'last_apply_time': 'last_apply_time',  # noqa: E501
        'updated': 'updated',  # noqa: E501
        'running_image': 'running_image',  # noqa: E501
        'running_hash': 'running_hash',  # noqa: E501
        'org_id': 'org_id',  # noqa: E501
    }

    read_only_vars = {
        'updated',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """RuntimeStatus - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            overall_status (str): The status of the running components. - A `good` status means that no action is neccessary on this environment - A `warn` status means that there is an issue that should be dealt with   Examples include a rollout failing or crashing containers - A `down` status indicates that there is a service accessibility problem   that should be dealt with as soon as possible. This could   mean that there were multiple failed rollouts, containers are unstable,   access to a neccessary service is down or other problems. - A `stale` status indicates that although there may not be anything wrong,   we haven't been able to update the status recently. This may indicate   an issue with the platform - A `degraded` status indicates that the service is operational but running   in non-redundant mode. Note that this alarm would only be valid for   a service that supports redundancy. . [optional]  # noqa: E501
            running_replicas (int): The number of current running replicas. 2 is redundant, 1 could indicate error handling, 0 is down. . [optional]  # noqa: E501
            error_message (str): The error in running the current instance. Common errors include CrashLoopBackoff, ContainerPullError, ConfigError. If there is no error description, this will be empty. . [optional]  # noqa: E501
            restarts (int): How many times a container has restarted across all replicas of this instance. A non-zero number might indicate some intermittent error that is handled by the Agilicus system. A large number of errors could indicate problems in the application . [optional]  # noqa: E501
            cpu (float): The current number of CPU cores used by all the containers for the instance. A high number eg 1.00 may indicate performance problems as a container is unable to service all requests . [optional]  # noqa: E501
            memory (float): The amount of RAM used by all containers used for the instance in MiB . [optional]  # noqa: E501
            last_apply_time (datetime): The last time any change was applied to the running containers. This can be used to indicate if the system has 'picked up' a recent change that was made . [optional]  # noqa: E501
            updated (datetime): Update time. [optional]  # noqa: E501
            running_image (str): The container tag identifies what container is currently running in this instance. This could be different than the configured image if there was an error upgrading. Although relatively rare in practice, the same image tag could have been pushed with many different images, when the container is started it will pull the latest version. See running_hash for more information . [optional]  # noqa: E501
            running_hash (str): The container hash of What versions users see when they browse to the site. If a image tag has been pushed multiple times, ie for hotfixes then this could be used to identify exactly what software is running . [optional]  # noqa: E501
            org_id (str): Unique identifier. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    def __python_set(val):
        return set(val)
 
    required_properties = __python_set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """RuntimeStatus - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            overall_status (str): The status of the running components. - A `good` status means that no action is neccessary on this environment - A `warn` status means that there is an issue that should be dealt with   Examples include a rollout failing or crashing containers - A `down` status indicates that there is a service accessibility problem   that should be dealt with as soon as possible. This could   mean that there were multiple failed rollouts, containers are unstable,   access to a neccessary service is down or other problems. - A `stale` status indicates that although there may not be anything wrong,   we haven't been able to update the status recently. This may indicate   an issue with the platform - A `degraded` status indicates that the service is operational but running   in non-redundant mode. Note that this alarm would only be valid for   a service that supports redundancy. . [optional]  # noqa: E501
            running_replicas (int): The number of current running replicas. 2 is redundant, 1 could indicate error handling, 0 is down. . [optional]  # noqa: E501
            error_message (str): The error in running the current instance. Common errors include CrashLoopBackoff, ContainerPullError, ConfigError. If there is no error description, this will be empty. . [optional]  # noqa: E501
            restarts (int): How many times a container has restarted across all replicas of this instance. A non-zero number might indicate some intermittent error that is handled by the Agilicus system. A large number of errors could indicate problems in the application . [optional]  # noqa: E501
            cpu (float): The current number of CPU cores used by all the containers for the instance. A high number eg 1.00 may indicate performance problems as a container is unable to service all requests . [optional]  # noqa: E501
            memory (float): The amount of RAM used by all containers used for the instance in MiB . [optional]  # noqa: E501
            last_apply_time (datetime): The last time any change was applied to the running containers. This can be used to indicate if the system has 'picked up' a recent change that was made . [optional]  # noqa: E501
            updated (datetime): Update time. [optional]  # noqa: E501
            running_image (str): The container tag identifies what container is currently running in this instance. This could be different than the configured image if there was an error upgrading. Although relatively rare in practice, the same image tag could have been pushed with many different images, when the container is started it will pull the latest version. See running_hash for more information . [optional]  # noqa: E501
            running_hash (str): The container hash of What versions users see when they browse to the site. If a image tag has been pushed multiple times, ie for hotfixes then this could be used to identify exactly what software is running . [optional]  # noqa: E501
            org_id (str): Unique identifier. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")

