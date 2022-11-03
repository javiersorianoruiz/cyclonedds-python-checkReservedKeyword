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

from module_test import struct_test_A, struct_test_B

qos = Qos(
    Policy.Reliability.BestEffort,
    Policy.Deadline(duration(microseconds=10)),
    Policy.Durability.Transient,
    Policy.History.KeepLast(10)
)

domain_participant = DomainParticipant(0)
topic_1 = Topic(domain_participant, 'module_test_struct_test_A_002', struct_test_A)
topic_2 = Topic(domain_participant, 'module_test_struct_test_B_002', struct_test_B)
publisher = Publisher(domain_participant)
writer_1 = DataWriter(publisher, topic_1)
writer_2 = DataWriter(publisher, topic_2)

msg_1 = struct_test_A(var='z')
msg_2 = struct_test_B(var_2='y')

while True:
    writer_1.write(msg_1)
    writer_2.write(msg_2)
    print(">> Wrote struct_test_A msg_1 and struct_test_B msg_2")
    time.sleep(3.0)
