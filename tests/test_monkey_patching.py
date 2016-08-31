#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:mod:`test_monkey_patching`
=======================

.. moduleauthor:: hbldh <henrik.blidh@swedwise.com>
Created on 2016-08-31, 11:23

"""

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import os

from PIL import Image
import imdirect

this_dir = os.path.dirname(os.path.abspath(__file__))


def test_monkey_patching():
    image_path = os.path.join(this_dir, 'testfile_6.jpg')
    imdirect.monkey_patch(False)
    img = Image.open(image_path)
    assert img.width == 300
    assert img.height == 225
    assert img._getexif().get(274) == 6

    imdirect.monkey_patch(True)
    img = Image.open(image_path)
    assert img.width == 225
    assert img.height == 300
    assert img._getexif().get(274) == 1

    imdirect.monkey_patch(False)
    img = Image.open(image_path)
    assert img.width == 300
    assert img.height == 225
    assert img._getexif().get(274) == 6

