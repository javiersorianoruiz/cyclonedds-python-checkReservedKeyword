"""
 * Copyright(c) 2021 ZettaScale Technology and others
 *
 * This program and the accompanying materials are made available under the
 * terms of the Eclipse Public License v. 2.0 which is available at
 * http://www.eclipse.org/legal/epl-2.0, or the Eclipse Distribution License
 * v. 1.0 which is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 *
 * SPDX-License-Identifier: EPL-2.0 OR BSD-3-Clause
"""

import time
import random

from cyclonedds.core import Qos, Policy
from cyclonedds.domain import DomainParticipant
from cyclonedds.pub import Publisher, DataWriter
from cyclonedds.topic import Topic
from cyclonedds.util import duration

#from vehicles import Vehicle
from HelloWorldData import Msg

print("from HelloWorldData import Msg")

#from cyclonedds.idl._main import IDLNamespaceScope,IdlMeta

#from cyclonedds.idl._type_normalize import get_idl_field_annotations

#print ("type(cls): ", type(cls))
#tipo_struct: Type[IdlStruct]
#from typing import Type

#from cyclonedds.idl import IdlStruct

#field_annotations = get_idl_field_annotations(Type[IdlStruct])
#field_annotations = get_idl_field_annotations(IdlStruct)
#print("field_annotations: ", field_annotations)

#print("IDLNamespaceScope.current[\"__idl_field_annotations__\"]: ", IDLNamespaceScope.current["__idl_field_annotations__"])
#print("IDLNamespaceScope.current[\"__idl_field_annotations__\"][\"_break\"][\"name\"]: ", IDLNamespaceScope.current["__idl_field_annotations__"]["_break"]["name"])


# This is the publisher in the Vehicle Demo. It publishes a randomly moving
# vehicle updated every 0.1-1.0 seconds randomly. The 'Vehicle' class was
# generated from the vehicle.idl file with `idlc -l py vehicle.idl`


qos = Qos(
    Policy.Reliability.BestEffort,
    Policy.Deadline(duration(microseconds=10)),
    Policy.Durability.Transient,
    Policy.History.KeepLast(10)
)

domain_participant = DomainParticipant(0)
#topic = Topic(domain_participant, 'Vehicle', Vehicle, qos=qos)
topic = Topic(domain_participant, 'HelloWorldData_Msg', Msg)
publisher = Publisher(domain_participant)
writer = DataWriter(publisher, topic)


msg = Msg(userID=1000, message="Hello World")
#msg = Msg(userID=1000, message="Hello World",_break="Break message",_None="None message")


while True:
    #vehicle.x += random.choice([-1, 0, 1])
    #vehicle.y += random.choice([-1, 0, 1])
    writer.write(msg)
    print(">> Wrote Hello World msg")
    #time.sleep(random.random() * 10.0 + 0.1)
    time.sleep(3.0)
