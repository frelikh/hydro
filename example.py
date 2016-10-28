#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
example.py
----------

'''

from __future__ import division, print_function, absolute_import, unicode_literals
from hydro import Hydro

h = Hydro(out_time = 100)
h.run()
h.animate()