#!/usr/bin/env python
from __future__ import print_function
import os

path = 'txt/fiction/foreign/Vern'

files = os.listdir(path)
for name in files:
    print(name)