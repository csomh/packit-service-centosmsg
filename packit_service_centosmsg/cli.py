# MIT License
#
# Copyright (c) 2018-2019 Red Hat, Inc.

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
Listen to messages coming to centos messaging
"""
import os
from time import sleep

import click

from packit_service_centosmsg.consumer import Consumerino


@click.command("listen-to-centos-messaging")
def listen_to_centos_messaging():
    """
    Listen to events on centos messaging and process them.
    """

    # hardcoded defaults, because env defined in docker file is not visible (maybe to openshift)
    CA_CERTS = os.getenv("CENTOS_CA_CERTS", "/secrets/centos-server-ca.cert")
    CERTFILE = os.getenv("CENTOS_CERTFILE", "/secrets/centos.cert")

    centos_mqtt_client = Consumerino()
    centos_mqtt_client.consume_from_centos_messaging(ca_certs=CA_CERTS, certfile=CERTFILE)

