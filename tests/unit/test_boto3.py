# Copyright 2014 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# https://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

import oss
from tests import mock, unittest


class TestBoto3(unittest.TestCase):
    def setUp(self):
        self.session_patch = mock.patch('oss.Session', autospec=True)
        self.Session = self.session_patch.start()

    def tearDown(self):
        oss.DEFAULT_SESSION = None
        self.session_patch.stop()

    def test_create_default_session(self):
        session = self.Session.return_value

        oss.setup_default_session()

        assert oss.DEFAULT_SESSION == session

    def test_create_default_session_with_args(self):
        oss.setup_default_session(
            aws_access_key_id='key', aws_secret_access_key='secret'
        )

        self.Session.assert_called_with(
            aws_access_key_id='key', aws_secret_access_key='secret'
        )

    @mock.patch(
        'boto3.setup_default_session', wraps=oss.setup_default_session
    )
    def test_client_creates_default_session(self, setup_session):
        oss.DEFAULT_SESSION = None

        oss.client('sqs')

        assert setup_session.called
        assert oss.DEFAULT_SESSION.client.called

    @mock.patch(
        'boto3.setup_default_session', wraps=oss.setup_default_session
    )
    def test_client_uses_existing_session(self, setup_session):
        oss.DEFAULT_SESSION = self.Session()

        oss.client('sqs')

        assert not setup_session.called
        assert oss.DEFAULT_SESSION.client.called

    def test_client_passes_through_arguments(self):
        oss.DEFAULT_SESSION = self.Session()

        oss.client('sqs', region_name='us-west-2', verify=False)

        oss.DEFAULT_SESSION.client.assert_called_with(
            'sqs', region_name='us-west-2', verify=False
        )

    @mock.patch(
        'boto3.setup_default_session', wraps=oss.setup_default_session
    )
    def test_resource_creates_default_session(self, setup_session):
        oss.DEFAULT_SESSION = None

        oss.resource('sqs')

        assert setup_session.called
        assert oss.DEFAULT_SESSION.resource.called

    @mock.patch(
        'boto3.setup_default_session', wraps=oss.setup_default_session
    )
    def test_resource_uses_existing_session(self, setup_session):
        oss.DEFAULT_SESSION = self.Session()

        oss.resource('sqs')

        assert not setup_session.called
        assert oss.DEFAULT_SESSION.resource.called

    def test_resource_passes_through_arguments(self):
        oss.DEFAULT_SESSION = self.Session()

        oss.resource('sqs', region_name='us-west-2', verify=False)

        oss.DEFAULT_SESSION.resource.assert_called_with(
            'sqs', region_name='us-west-2', verify=False
        )
