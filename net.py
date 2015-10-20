#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import wire
import hands

class Net(wire.Wire):
    def __init__(self):
        ROPE_DISTANCE = 20
        self.wire = Wire
    def createNet(self):
        net = hands.weave(self.wire)
        return net