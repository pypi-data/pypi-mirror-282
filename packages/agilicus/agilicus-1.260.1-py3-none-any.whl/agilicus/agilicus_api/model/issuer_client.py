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


def lazy_import():
    from agilicus_api.model.authentication_attribute import AuthenticationAttribute
    globals()['AuthenticationAttribute'] = AuthenticationAttribute


class IssuerClient(ModelNormal):
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
        ('organisation_scope',): {
            'ANY': "any",
            'HERE_AND_DOWN': "here_and_down",
            'HERE_ONLY': "here_only",
        },
        ('mfa_challenge',): {
            'ALWAYS': "always",
            'USER_PREFERENCE': "user_preference",
            'TRUST_UPSTREAM': "trust_upstream",
        },
        ('single_sign_on',): {
            'USER_PREFERENCE': "user_preference",
            'NEVER': "never",
        },
    }

    validations = {
        ('name',): {
            'max_length': 100,
            'min_length': 1,
        },
        ('secret',): {
            'max_length': 255,
        },
        ('application',): {
            'max_length': 100,
        },
        ('org_id',): {
            'max_length': 40,
        },
        ('restricted_organisations',): {
        },
        ('saml_metadata_file',): {
            'max_length': 1048576,
        },
        ('redirects',): {
        },
    }

    @property
    def id(self):
       return self.get("id")

    @id.setter
    def id(self, new_value):
       self.id = new_value

    @property
    def issuer_id(self):
       return self.get("issuer_id")

    @issuer_id.setter
    def issuer_id(self, new_value):
       self.issuer_id = new_value

    @property
    def name(self):
       return self.get("name")

    @name.setter
    def name(self, new_value):
       self.name = new_value

    @property
    def secret(self):
       return self.get("secret")

    @secret.setter
    def secret(self, new_value):
       self.secret = new_value

    @property
    def application(self):
       return self.get("application")

    @application.setter
    def application(self, new_value):
       self.application = new_value

    @property
    def org_id(self):
       return self.get("org_id")

    @org_id.setter
    def org_id(self, new_value):
       self.org_id = new_value

    @property
    def restricted_organisations(self):
       return self.get("restricted_organisations")

    @restricted_organisations.setter
    def restricted_organisations(self, new_value):
       self.restricted_organisations = new_value

    @property
    def saml_metadata_file(self):
       return self.get("saml_metadata_file")

    @saml_metadata_file.setter
    def saml_metadata_file(self, new_value):
       self.saml_metadata_file = new_value

    @property
    def id_mapping(self):
       return self.get("id_mapping")

    @id_mapping.setter
    def id_mapping(self, new_value):
       self.id_mapping = new_value

    @property
    def saml_scopes(self):
       return self.get("saml_scopes")

    @saml_scopes.setter
    def saml_scopes(self, new_value):
       self.saml_scopes = new_value

    @property
    def organisation_scope(self):
       return self.get("organisation_scope")

    @organisation_scope.setter
    def organisation_scope(self, new_value):
       self.organisation_scope = new_value

    @property
    def redirects(self):
       return self.get("redirects")

    @redirects.setter
    def redirects(self, new_value):
       self.redirects = new_value

    @property
    def mfa_challenge(self):
       return self.get("mfa_challenge")

    @mfa_challenge.setter
    def mfa_challenge(self, new_value):
       self.mfa_challenge = new_value

    @property
    def single_sign_on(self):
       return self.get("single_sign_on")

    @single_sign_on.setter
    def single_sign_on(self, new_value):
       self.single_sign_on = new_value

    @property
    def attributes(self):
       return self.get("attributes")

    @attributes.setter
    def attributes(self, new_value):
       self.attributes = new_value

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
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
        lazy_import()
        return {
            'name': (str,),  # noqa: E501
            'id': (str,),  # noqa: E501
            'issuer_id': (str,),  # noqa: E501
            'secret': (str,),  # noqa: E501
            'application': (str,),  # noqa: E501
            'org_id': (str,),  # noqa: E501
            'restricted_organisations': ([str],),  # noqa: E501
            'saml_metadata_file': (str,),  # noqa: E501
            'id_mapping': ([str],),  # noqa: E501
            'saml_scopes': ([str],),  # noqa: E501
            'organisation_scope': (str,),  # noqa: E501
            'redirects': ([str],),  # noqa: E501
            'mfa_challenge': (str,),  # noqa: E501
            'single_sign_on': (str,),  # noqa: E501
            'attributes': ([AuthenticationAttribute],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'name': 'name',  # noqa: E501
        'id': 'id',  # noqa: E501
        'issuer_id': 'issuer_id',  # noqa: E501
        'secret': 'secret',  # noqa: E501
        'application': 'application',  # noqa: E501
        'org_id': 'org_id',  # noqa: E501
        'restricted_organisations': 'restricted_organisations',  # noqa: E501
        'saml_metadata_file': 'saml_metadata_file',  # noqa: E501
        'id_mapping': 'id_mapping',  # noqa: E501
        'saml_scopes': 'saml_scopes',  # noqa: E501
        'organisation_scope': 'organisation_scope',  # noqa: E501
        'redirects': 'redirects',  # noqa: E501
        'mfa_challenge': 'mfa_challenge',  # noqa: E501
        'single_sign_on': 'single_sign_on',  # noqa: E501
        'attributes': 'attributes',  # noqa: E501
    }

    read_only_vars = {
        'id',  # noqa: E501
        'issuer_id',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, name, *args, **kwargs):  # noqa: E501
        """IssuerClient - a model defined in OpenAPI

        Args:
            name (str): issuer client id

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
            id (str): Unique identifier. [optional]  # noqa: E501
            issuer_id (str): Unique identifier. [optional]  # noqa: E501
            secret (str): issuer client secret. [optional]  # noqa: E501
            application (str): application associated with client. [optional]  # noqa: E501
            org_id (str): org_id associated with client. [optional]  # noqa: E501
            restricted_organisations ([str]): List of organisation IDs which are allowed to authenticate using this client. If a user is not a member of one of these organisations, their authentication attempt will be denied. Note that this list intersects with `organisation_scope`. For example, if `organisation_scope` is `here-and-down` and this list contains two organisations below the current organisation, only those two will be allowed, despite there potentially being more sub organisations. If the list is empty, no restrictions are applied by this field. Note that other restrictions may be applied, such as by `organisation_scope`. . [optional]  # noqa: E501
            saml_metadata_file (str): The Service Provider's metadata file required for the SAML protocol. . [optional]  # noqa: E501
            id_mapping ([str]): The properties from the agilicus id token to map to the user id. This can be changed if your application relies on an upstream user_id to map the user, for example SID or email. You can see what is available by logging into the admin portal and finding the token in local storage. When changing this ensure that you are requesting an appropriate saml_scope. For example in order to use federated_claims you need the federated:id scope. . [optional] if omitted the server will use the default value of ["sub"]  # noqa: E501
            saml_scopes ([str]): The set of scopes to request for the agilicus oidc token when mapping to saml. . [optional] if omitted the server will use the default value of ["openid","profile","email","urn:agilicus:api:users:self"]  # noqa: E501
            organisation_scope (str): How to limit which organisations are allowed to authenticate using this client. Note that this interacts with `restricted_organisations`: that list, if not empty, further limits the allowed organisations. * `any` indicates that there are no restrictions. All organisations served by   the issuer will be allowed to log in using this client. * `here-only` indicates that   only the organisation referenced by `org_id` may be used. * `here-and-down` indicates that the organisation referenced by `org_id`   and its children may be used. . [optional] if omitted the server will use the default value of "here_only"  # noqa: E501
            redirects ([str]): List of redirect uris. [optional]  # noqa: E501
            mfa_challenge (str): When to present an mfa challenge to a user upon login. If the system determines that an MFA challenge is required, and the user does not yet have a authenticatin mechanism valid for this login session, the user will be presented with the option to enrol a new mechanism. * `always` means that the user will always be required to validate against a second factor. * `user_preference` means that the whether the user is required to validate depends on the user's preferences.   A user could choose to always require MFA for their logins, or they could decide not to. Note that in this case,   other policy could override the preference to force the user to authenticate with MFA even if the user indicated   that they prefer not to. * `trust_upstream` means to always perform MFA, but that the upstream IDP will be trusted to have performed MFA if    the upstream indicates that it has done so. Otherwise, MFA will be performed by the system after the upstream    returns the to Issuer. . [optional] if omitted the server will use the default value of "user_preference"  # noqa: E501
            single_sign_on (str): Whether a client is allowed to use single sign-on * `user_preference` means that the user will have the option to 'remember' their upstream identity selection for single sign-on. * `never` means that the given client will not allow single sign-on. The user will be required to present credentials for each login to applications with this client id. . [optional] if omitted the server will use the default value of "never"  # noqa: E501
            attributes ([AuthenticationAttribute]): A list of attributes to derive from information about the user. The user's information returned to the relying party making a request using this client will be extended with these attributes. Only one attribute for a given `attribute_name` can exist per-client at a time. Add an attribute to this list when the default attributes do not provide sufficient information for the client application, or for when the client application expects the attributes to be named differently. . [optional]  # noqa: E501
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

        self.name = name
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
    def __init__(self, name, *args, **kwargs):  # noqa: E501
        """IssuerClient - a model defined in OpenAPI

        Args:
            name (str): issuer client id

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
            id (str): Unique identifier. [optional]  # noqa: E501
            issuer_id (str): Unique identifier. [optional]  # noqa: E501
            secret (str): issuer client secret. [optional]  # noqa: E501
            application (str): application associated with client. [optional]  # noqa: E501
            org_id (str): org_id associated with client. [optional]  # noqa: E501
            restricted_organisations ([str]): List of organisation IDs which are allowed to authenticate using this client. If a user is not a member of one of these organisations, their authentication attempt will be denied. Note that this list intersects with `organisation_scope`. For example, if `organisation_scope` is `here-and-down` and this list contains two organisations below the current organisation, only those two will be allowed, despite there potentially being more sub organisations. If the list is empty, no restrictions are applied by this field. Note that other restrictions may be applied, such as by `organisation_scope`. . [optional]  # noqa: E501
            saml_metadata_file (str): The Service Provider's metadata file required for the SAML protocol. . [optional]  # noqa: E501
            id_mapping ([str]): The properties from the agilicus id token to map to the user id. This can be changed if your application relies on an upstream user_id to map the user, for example SID or email. You can see what is available by logging into the admin portal and finding the token in local storage. When changing this ensure that you are requesting an appropriate saml_scope. For example in order to use federated_claims you need the federated:id scope. . [optional] if omitted the server will use the default value of ["sub"]  # noqa: E501
            saml_scopes ([str]): The set of scopes to request for the agilicus oidc token when mapping to saml. . [optional] if omitted the server will use the default value of ["openid","profile","email","urn:agilicus:api:users:self"]  # noqa: E501
            organisation_scope (str): How to limit which organisations are allowed to authenticate using this client. Note that this interacts with `restricted_organisations`: that list, if not empty, further limits the allowed organisations. * `any` indicates that there are no restrictions. All organisations served by   the issuer will be allowed to log in using this client. * `here-only` indicates that   only the organisation referenced by `org_id` may be used. * `here-and-down` indicates that the organisation referenced by `org_id`   and its children may be used. . [optional] if omitted the server will use the default value of "here_only"  # noqa: E501
            redirects ([str]): List of redirect uris. [optional]  # noqa: E501
            mfa_challenge (str): When to present an mfa challenge to a user upon login. If the system determines that an MFA challenge is required, and the user does not yet have a authenticatin mechanism valid for this login session, the user will be presented with the option to enrol a new mechanism. * `always` means that the user will always be required to validate against a second factor. * `user_preference` means that the whether the user is required to validate depends on the user's preferences.   A user could choose to always require MFA for their logins, or they could decide not to. Note that in this case,   other policy could override the preference to force the user to authenticate with MFA even if the user indicated   that they prefer not to. * `trust_upstream` means to always perform MFA, but that the upstream IDP will be trusted to have performed MFA if    the upstream indicates that it has done so. Otherwise, MFA will be performed by the system after the upstream    returns the to Issuer. . [optional] if omitted the server will use the default value of "user_preference"  # noqa: E501
            single_sign_on (str): Whether a client is allowed to use single sign-on * `user_preference` means that the user will have the option to 'remember' their upstream identity selection for single sign-on. * `never` means that the given client will not allow single sign-on. The user will be required to present credentials for each login to applications with this client id. . [optional] if omitted the server will use the default value of "never"  # noqa: E501
            attributes ([AuthenticationAttribute]): A list of attributes to derive from information about the user. The user's information returned to the relying party making a request using this client will be extended with these attributes. Only one attribute for a given `attribute_name` can exist per-client at a time. Add an attribute to this list when the default attributes do not provide sufficient information for the client application, or for when the client application expects the attributes to be named differently. . [optional]  # noqa: E501
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

        self.name = name
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

