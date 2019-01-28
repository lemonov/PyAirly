# Copyright 2019 Piotr Lemanczyk
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import requests
import urllib
import json

BASE_V2 = 'https://airapi.airly.eu/v2/'

INSTALLATIONS = 'installations/'
INSTALLATIONS_NEAREST = 'installations/nearest/'

MEASUREMENTS_BY_ID = 'measurements/installation/'
MEASUREMENTS_NEAREST = 'measurements/nearest/'
MEASUREMENTS_FOR_POINT = 'measurements/point/'

# META
META_INDEXES = 'meta/indexes/'
META_MEASUREMENTS = 'meta/measurements/'


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class PyAirly:
    def __init__(self, apikey, debug=False, accept_gzip_encoding=False):
        """
        :param accept_gzip_encoding: True to get gzip response
        :param apikey: apikey as specified in https://developer.airly.eu/docs#general.authentication
        :param debug: True for extra printed information on requests/responses
        """
        self.__debug = debug
        self.apikey = apikey
        self.accept_gzip_encoding = accept_gzip_encoding

    def send_request(self, endpoint, params=None):
        headers = {'Accept': 'application/json', 'apikey': self.apikey}
        if self.accept_gzip_encoding:
            headers['Accept-Encoding'] = 'gzip'
        if params:
            endpoint = endpoint + '?' + urllib.parse.urlencode(params)

        url = BASE_V2 + endpoint
        result = requests.get(url, headers=headers)
        if self.__debug:
            print(Colors.OKGREEN)
            print('------------REQUEST------------')
            print('URL: ' + url)
            print('HEADER: ' + str(headers))
            print(Colors.OKBLUE)
            print('------------RESPONSE-----------')
            print(json.dumps(result.json(), indent=4, sort_keys=True))
            print(Colors.ENDC)
        return result

    # INSTALLATIONS
    def get_installations_by_id(self, installation_id):
        """https://developer.airly.eu/docs#endpoints.installations.getbyid"""
        return self.send_request(INSTALLATIONS + str(installation_id))

    def get_installations_nearest(self, latitude, longitude, max_distance_km="", max_results="",
                                  ):
        """https://developer.airly.eu/docs#endpoints.installations.nearest"""
        params = [('lat', latitude), ('lng', longitude), ('maxDistanceKM', max_distance_km),
                  ('maxResults', max_results)]
        return self.send_request(INSTALLATIONS_NEAREST, params)

    # MEASUREMENTS
    def get_measurements_by_installation(self, installation_id):
        """https://developer.airly.eu/docs#endpoints.measurements.installation"""
        params = [('installationId', installation_id)]
        return self.send_request(MEASUREMENTS_BY_ID, params)

    def get_measurements_nearest(self, latitude, longitude, max_distance_km=""):
        """https://developer.airly.eu/docs#endpoints.measurements.nearest"""
        params = [('lat', latitude), ('lng', longitude), ('maxDistanceKM', max_distance_km)]
        return self.send_request(MEASUREMENTS_NEAREST, params)

    def get_measurements_for_point(self, latitude, longitude):
        """https://developer.airly.eu/docs#endpoints.measurements.point"""
        params = [('lat', latitude), ('lng', longitude)]
        return self.send_request(MEASUREMENTS_FOR_POINT, params)

    def get_meta_indexes(self):
        """https://developer.airly.eu/docs#endpoints.meta.indexes"""
        return self.send_request(META_INDEXES)

    def get_meta_measurements(self):
        """https://developer.airly.eu/docs#endpoints.meta.measurements"""
        return self.send_request(META_MEASUREMENTS)
