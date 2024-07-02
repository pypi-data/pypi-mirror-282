#   Copyright ETH 2023 Zürich, Scientific IT Services
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#


import settings
import testcase
import util as util


class TestCase(testcase.TestCase):

    def execute(self):
        self.installOpenbis(technologies=['eln-lims', 'eln-lims-template-types', 'flow'])
        # pybis should be installed on the jenkins job configuration level
        self.openbisController = self.createOpenbisController()
        self.openbisController.allUp()
        # run tests
        util.executeCommand(['pytest', '--verbose', '--junitxml=test_results_pybis.xml',
                             'api-openbis-python3-pybis/src/python/tests'])


TestCase(settings, __file__).runTest()
