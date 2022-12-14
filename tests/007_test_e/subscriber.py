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

from cyclonedds.core import Listener, Qos, Policy
from cyclonedds.domain import DomainParticipant
from cyclonedds.topic import Topic
from cyclonedds.sub import Subscriber, DataReader
from cyclonedds.util import duration

from module_test import _and, _continue

class MyListener(Listener):
    def on_liveliness_changed(self, reader, status):
        print(">> Liveliness event")


listener = MyListener()
qos = Qos(
    Policy.Reliability.BestEffort,
    Policy.Deadline(duration(microseconds=10)),
    Policy.Durability.Transient,
    Policy.History.KeepLast(10)
)

domain_participant = DomainParticipant(0)
topic_1 = Topic(domain_participant, 'module_test__and_007_e', _and)
topic_2 = Topic(domain_participant, 'module_test__continue_007_e', _continue)
subscriber = Subscriber(domain_participant)
reader_1 = DataReader(domain_participant, topic_1, listener=listener)
reader_2 = DataReader(domain_participant, topic_2, listener=listener)

while True:
    for sample in reader_1.take_iter(timeout=duration(seconds=2)):
        print(sample)
    for sample in reader_2.take_iter(timeout=duration(seconds=2)):
        print(sample)
