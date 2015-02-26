#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys

sep = os.path.sep
mylist = ["a", "b", "c"]

tmp = os.path.sep.join(mylist[:-1])

print(tmp)


a = False

if not a:
    print("KENNY")
else:
    print("NOEEY")