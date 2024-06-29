"""
    Agilicus API

    Agilicus is API-first. Modern software is controlled by other software, is open, is available for you to use the way you want, securely, simply.  The OpenAPI Specification in YAML format is available on [www](https://www.agilicus.com/www/api/agilicus-openapi.yaml) for importing to other tools.  A rendered, online viewable and usable version of this specification is available at [api](https://www.agilicus.com/api). You may try the API inline directly in the web page. To do so, first obtain an Authentication Token (the simplest way is to install the Python SDK, and then run `agilicus-cli --issuer https://MYISSUER get-token`). You will need an org-id for most calls (and can obtain from `agilicus-cli --issuer https://MYISSUER list-orgs`). The `MYISSUER` will typically be `auth.MYDOMAIN`, and you will see it as you sign-in to the administrative UI.  This API releases on Bearer-Token authentication. To obtain a valid bearer token you will need to Authenticate to an Issuer with OpenID Connect (a superset of OAUTH2).  Your \"issuer\" will look like https://auth.MYDOMAIN. For example, when you signed-up, if you said \"use my own domain name\" and assigned a CNAME of cloud.example.com, then your issuer would be https://auth.cloud.example.com.  If you selected \"use an Agilicus supplied domain name\", your issuer would look like https://auth.myorg.agilicus.cloud.  For test purposes you can use our [Python SDK](https://pypi.org/project/agilicus/) and run `agilicus-cli --issuer https://auth.MYDOMAIN get-token`.  This API may be used in any language runtime that supports OpenAPI 3.0, or, you may use our [Python SDK](https://pypi.org/project/agilicus/), our [Typescript SDK](https://www.npmjs.com/package/@agilicus/angular), or our [Golang SDK](https://git.agilicus.com/pub/sdk-go).  100% of the activities in our system our API-driven, from our web-admin, through our progressive web applications, to all internals: there is nothing that is not accessible.  For more information, see [developer resources](https://www.agilicus.com/developer).   # noqa: E501

    The version of the OpenAPI document: 2024.06.21
    Contact: dev@agilicus.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import agilicus_api
from agilicus_api.api.hosts_api import HostsApi  # noqa: E501


class TestHostsApi(unittest.TestCase):
    """HostsApi unit test stubs"""

    def setUp(self):
        self.api = HostsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_host(self):
        """Test case for add_host

        Creates a Host  # noqa: E501
        """
        pass

    def test_add_host_bundle(self):
        """Test case for add_host_bundle

        Creates a HostBundle  # noqa: E501
        """
        pass

    def test_add_host_label(self):
        """Test case for add_host_label

        Creates a HostLabel  # noqa: E501
        """
        pass

    def test_delete_host(self):
        """Test case for delete_host

        Delete a Host  # noqa: E501
        """
        pass

    def test_delete_host_bundle(self):
        """Test case for delete_host_bundle

        Delete a HostBundle  # noqa: E501
        """
        pass

    def test_delete_host_label(self):
        """Test case for delete_host_label

        Delete a HostLabel  # noqa: E501
        """
        pass

    def test_get_host(self):
        """Test case for get_host

        Get a Host  # noqa: E501
        """
        pass

    def test_get_host_bundle(self):
        """Test case for get_host_bundle

        Get a HostBundle  # noqa: E501
        """
        pass

    def test_get_host_label(self):
        """Test case for get_host_label

        Get a HostLabel  # noqa: E501
        """
        pass

    def test_list_host_bundles(self):
        """Test case for list_host_bundles

        list HostBundle  # noqa: E501
        """
        pass

    def test_list_host_labels(self):
        """Test case for list_host_labels

        list HostLabel  # noqa: E501
        """
        pass

    def test_list_host_orgs(self):
        """Test case for list_host_orgs

        list orgs that have available hosts  # noqa: E501
        """
        pass

    def test_list_hosts(self):
        """Test case for list_hosts

        list hosts  # noqa: E501
        """
        pass

    def test_replace_host(self):
        """Test case for replace_host

        Update a Host  # noqa: E501
        """
        pass

    def test_replace_host_bundle(self):
        """Test case for replace_host_bundle

        Update a HostBundle  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
