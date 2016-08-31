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


from PIL import Image
import autopil


def test_monkey_patching():
    image_path = './testfile_6.jpg'
    autopil.monkey_patch(False)
    img = Image.open(image_path)
    assert img.width == 300
    assert img.height == 225
    assert img._getexif().get(274) == 6

    autopil.monkey_patch(True)
    img = Image.open(image_path)
    assert img.width == 225
    assert img.height == 300
    assert img._getexif().get(274) == 1

    autopil.monkey_patch(False)
    img = Image.open(image_path)
    assert img.width == 300
    assert img.height == 225
    assert img._getexif().get(274) == 6

