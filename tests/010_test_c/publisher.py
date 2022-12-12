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

from module_test import struct_test,_except

qos = Qos(
    Policy.Reliability.BestEffort,
    Policy.Deadline(duration(microseconds=10)),
    Policy.Durability.Transient,
    Policy.History.KeepLast(10)
)

domain_participant = DomainParticipant(0)
topic = Topic(domain_participant, 'module_test_struct_test_010_c', struct_test)
publisher = Publisher(domain_participant)
writer = DataWriter(publisher, topic)

msg = struct_test(bitmask_value=_except(_finally=True,_for=False))

while True:
    writer.write(msg)
    print(">> Wrote struct_test msg")
    time.sleep(3.0)
