#!/usr/bin/env python

import random
import time
import sys
import iothub_client

from iothub_client import *
from iothub_client_args import *


protocol = IoTHubTransportProvider.AMQP
message_timeout = 10000

connection_string = "Device connection string"

def set_certificates(iotHubClient):
    from iothub_client_cert import certificates
    try:
        iotHubClient.set_option("TrustedCerts", certificates)
        print("set_option TrustedCerts successful")
    except IoTHubClientError as e:
        print("set_option TrustedCerts failed (%s)" % e)


def send_confirmation_callback(message, result, user_context):
    print(
         "Confirmation[%d] received for message with result = %s" %
        (user_context, result))
    map_properties = message.properties()
    print("    message_id: %s" % message.message_id)
    print("    correlation_id: %s" % message.correlation_id)
    key_value_pair = map_properties.get_internals()
    print("    Properties: %s" % key_value_pair)


iotHubClient = IoTHubClient(connection_string, protocol)
iotHubClient.set_option("messageTimeout", message_timeout)

message = IoTHubMessage(bytearray("Temperature: 1", 'utf8'))
iotHubClient.send_event_async(message,send_confirmation_callback, 0);

status = iotHubClient.get_send_status()
print("Send status: %s" % status)

print "message sent"
