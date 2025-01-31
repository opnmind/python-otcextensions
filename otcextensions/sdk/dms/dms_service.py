# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from openstack import service_description

from otcextensions.sdk.dms.v1 import _proxy as _proxy_v1
from otcextensions.sdk.dms.v2 import _proxy as _proxy_v2


class DmsService(service_description.ServiceDescription):
    """The DMS service."""

    supported_versions = {
        '1': _proxy_v1.Proxy,
        '2': _proxy_v2.Proxy
    }
