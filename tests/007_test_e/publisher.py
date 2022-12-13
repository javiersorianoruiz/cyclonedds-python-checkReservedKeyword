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

from module_test import _and, _continue

qos = Qos(
    Policy.Reliability.BestEffort,
    Policy.Deadline(duration(microseconds=10)),
    Policy.Durability.Transient,
    Policy.History.KeepLast(10)
)

domain_participant = DomainParticipant(0)
topic_1 = Topic(domain_participant, 'module_test__and_007_e', _and)
topic_2 = Topic(domain_participant, 'module_test__continue_007_e', _continue)
publisher = Publisher(domain_participant)
writer_1 = DataWriter(publisher, topic_1)
writer_2 = DataWriter(publisher, topic_2)

msg_1 = _and(var='z')
msg_2 = _continue(var_2='y', var='p')

while True:
    time.sleep(3.0)
    writer_1.write(msg_1)
    print(">> Wrote _and msg_1")
    time.sleep(3.0)
    writer_2.write(msg_2)
    print(">> Wrote _continue msg_2")
