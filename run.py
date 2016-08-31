#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
run
-----------

:copyright: 2016-08-30 by hbldh <henrik.blidh@nedomkull.com>

"""

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import imdirect
from PIL import Image

i = Image.open('2016-08-28 15.11.44.jpg')
#i = imdirect.open('2016-08-28 15.11.44.jpg')

#img = imdirect.autorotate(i)
i.show()
print(i)
