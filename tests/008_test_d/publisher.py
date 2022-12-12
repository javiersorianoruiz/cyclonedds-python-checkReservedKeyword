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

from module_test import struct_test, _assert


qos = Qos(
    Policy.Reliability.BestEffort,
    Policy.Deadline(duration(microseconds=10)),
    Policy.Durability.Transient,
    Policy.History.KeepLast(10)
)

domain_participant = DomainParticipant(0)
topic = Topic(domain_participant, 'module_test_struct_test_008_d', struct_test)
publisher = Publisher(domain_participant)
writer = DataWriter(publisher, topic)

msg1 = struct_test(_as=_assert(discriminator=1,value=10))
msg2 = struct_test(_as=_assert(discriminator=2,value=['a','b','c','d','e']))
msg3 = struct_test(_as=_assert(discriminator=3,value="hello wold"))

while True:
    time.sleep(3.0)
    writer.write(msg1)
    print(">> Wrote struct_test msg1")
    time.sleep(3.0)
    writer.write(msg2)
    print(">> Wrote struct_test msg2")
    time.sleep(3.0)
    writer.write(msg3)
    print(">> Wrote struct_test msg3")
