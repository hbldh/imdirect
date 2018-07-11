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


def test_imdirect_6():
    image_path = os.path.join(this_dir, 'IMG_0859.jpg')

    img = Image.open(image_path)
    assert img.width == 640
    assert img.height == 480
    assert img._getexif().get(274) == 6

    img_rot = imdirect.imdirect_open(image_path)
    assert img_rot.width == 480
    assert img_rot.height == 640
    assert img_rot._getexif().get(274) == 1


def test_imdirect_1():
    image_path = os.path.join(this_dir, 'IMG_0860.jpg')

    img = Image.open(image_path)
    assert img.width == 640
    assert img.height == 480
    assert img._getexif().get(274) == 1

    img_rot = imdirect.imdirect_open(image_path)
    assert img_rot.width == 640
    assert img_rot.height == 480
    assert img_rot._getexif().get(274) == 1


def test_imdirect_8():
    image_path = os.path.join(this_dir, 'IMG_0861.jpg')

    img = Image.open(image_path)
    assert img.width == 640
    assert img.height == 480
    assert img._getexif().get(274) == 8

    img_rot = imdirect.imdirect_open(image_path)
    assert img_rot.width == 480
    assert img_rot.height == 640
    assert img_rot._getexif().get(274) == 1


def test_imdirect_3():
    image_path = os.path.join(this_dir, 'IMG_0862.jpg')

    img = Image.open(image_path)
    assert img.width == 640
    assert img.height == 480
    assert img._getexif().get(274) == 3

    img_rot = imdirect.imdirect_open(image_path)
    assert img_rot.width == 640
    assert img_rot.height == 480
    assert img_rot._getexif().get(274) == 1
