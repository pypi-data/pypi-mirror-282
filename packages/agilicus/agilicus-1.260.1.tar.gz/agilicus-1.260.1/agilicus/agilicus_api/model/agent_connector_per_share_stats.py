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



class AgentConnectorPerShareStats(ModelNormal):
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
    }

    validations = {
        ('total_requests',): {
            'inclusive_minimum': 0,
        },
        ('successful_requests',): {
            'inclusive_minimum': 0,
        },
        ('failed_requests',): {
            'inclusive_minimum': 0,
        },
        ('bytes_sent',): {
            'inclusive_minimum': 0,
        },
        ('bytes_received',): {
            'inclusive_minimum': 0,
        },
    }

    @property
    def share_prefix(self):
       return self.get("share_prefix")

    @share_prefix.setter
    def share_prefix(self, new_value):
       self.share_prefix = new_value

    @property
    def share_id(self):
       return self.get("share_id")

    @share_id.setter
    def share_id(self, new_value):
       self.share_id = new_value

    @property
    def local_path(self):
       return self.get("local_path")

    @local_path.setter
    def local_path(self, new_value):
       self.local_path = new_value

    @property
    def total_requests(self):
       return self.get("total_requests")

    @total_requests.setter
    def total_requests(self, new_value):
       self.total_requests = new_value

    @property
    def successful_requests(self):
       return self.get("successful_requests")

    @successful_requests.setter
    def successful_requests(self, new_value):
       self.successful_requests = new_value

    @property
    def failed_requests(self):
       return self.get("failed_requests")

    @failed_requests.setter
    def failed_requests(self, new_value):
       self.failed_requests = new_value

    @property
    def bytes_sent(self):
       return self.get("bytes_sent")

    @bytes_sent.setter
    def bytes_sent(self, new_value):
       self.bytes_sent = new_value

    @property
    def bytes_received(self):
       return self.get("bytes_received")

    @bytes_received.setter
    def bytes_received(self, new_value):
       self.bytes_received = new_value

    @property
    def share_start_time(self):
       return self.get("share_start_time")

    @share_start_time.setter
    def share_start_time(self, new_value):
       self.share_start_time = new_value

    @property
    def correct_share_permissions(self):
       return self.get("correct_share_permissions")

    @correct_share_permissions.setter
    def correct_share_permissions(self, new_value):
       self.correct_share_permissions = new_value

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
            'share_prefix': (str,),  # noqa: E501
            'share_id': (str,),  # noqa: E501
            'local_path': (str,),  # noqa: E501
            'total_requests': (int,),  # noqa: E501
            'successful_requests': (int,),  # noqa: E501
            'failed_requests': (int,),  # noqa: E501
            'bytes_sent': (int,),  # noqa: E501
            'bytes_received': (int,),  # noqa: E501
            'share_start_time': (datetime,),  # noqa: E501
            'correct_share_permissions': (bool,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'share_prefix': 'share_prefix',  # noqa: E501
        'share_id': 'share_id',  # noqa: E501
        'local_path': 'local_path',  # noqa: E501
        'total_requests': 'total_requests',  # noqa: E501
        'successful_requests': 'successful_requests',  # noqa: E501
        'failed_requests': 'failed_requests',  # noqa: E501
        'bytes_sent': 'bytes_sent',  # noqa: E501
        'bytes_received': 'bytes_received',  # noqa: E501
        'share_start_time': 'share_start_time',  # noqa: E501
        'correct_share_permissions': 'correct_share_permissions',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, share_prefix, share_id, local_path, total_requests, successful_requests, failed_requests, bytes_sent, bytes_received, share_start_time, *args, **kwargs):  # noqa: E501
        """AgentConnectorPerShareStats - a model defined in OpenAPI

        Args:
            share_prefix (str): The prefix used to route the requests to the shared local path. This is typically derived from the share_name of the Share. 
            share_id (str): The unique ID of the FileShareService to which this share corresponds. 
            local_path (str): The path on the local file system which is being shared.
            total_requests (int): The total number of requests made to this share.
            successful_requests (int): The total number of requests which have succeeded.
            failed_requests (int): The total number of requests which have failed.
            bytes_sent (int): The total number of bytes sent in the body of responses to requests. This includes any metadata about files, or data included in failure responses. 
            bytes_received (int): The total number of bytes received in the body of requests. This includes any metadata about files, files themselves, or general commands such as lock requests. 
            share_start_time (datetime): When the share was started.

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
            correct_share_permissions (bool): True if share has correct permissions, false otherwise. . [optional]  # noqa: E501
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

        self.share_prefix = share_prefix
        self.share_id = share_id
        self.local_path = local_path
        self.total_requests = total_requests
        self.successful_requests = successful_requests
        self.failed_requests = failed_requests
        self.bytes_sent = bytes_sent
        self.bytes_received = bytes_received
        self.share_start_time = share_start_time
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
    def __init__(self, share_prefix, share_id, local_path, total_requests, successful_requests, failed_requests, bytes_sent, bytes_received, share_start_time, *args, **kwargs):  # noqa: E501
        """AgentConnectorPerShareStats - a model defined in OpenAPI

        Args:
            share_prefix (str): The prefix used to route the requests to the shared local path. This is typically derived from the share_name of the Share. 
            share_id (str): The unique ID of the FileShareService to which this share corresponds. 
            local_path (str): The path on the local file system which is being shared.
            total_requests (int): The total number of requests made to this share.
            successful_requests (int): The total number of requests which have succeeded.
            failed_requests (int): The total number of requests which have failed.
            bytes_sent (int): The total number of bytes sent in the body of responses to requests. This includes any metadata about files, or data included in failure responses. 
            bytes_received (int): The total number of bytes received in the body of requests. This includes any metadata about files, files themselves, or general commands such as lock requests. 
            share_start_time (datetime): When the share was started.

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
            correct_share_permissions (bool): True if share has correct permissions, false otherwise. . [optional]  # noqa: E501
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

        self.share_prefix = share_prefix
        self.share_id = share_id
        self.local_path = local_path
        self.total_requests = total_requests
        self.successful_requests = successful_requests
        self.failed_requests = failed_requests
        self.bytes_sent = bytes_sent
        self.bytes_received = bytes_received
        self.share_start_time = share_start_time
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

