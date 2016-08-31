autopil
=======

|Build Status| |Coverage Status|

PIL extension performing automatic rotation of opened JPEG images.

Description
-----------

The orientation of the photographed
object or scene with respect to the digital camera is encoded in the resulting
image's Exif [1]_ data (given that it is saved as a JPEG). When working with such digital camera images,
this orientation might lead to problems handling the image and is very often desired to be
counteracted.

This module is a small extension to `Pillow <https://pillow.readthedocs.io/en/3.3.x/>`_,
`monkey patching <https://en.wikipedia.org/wiki/Monkey_patch>`_
the `PIL.Image.open <http://pillow.readthedocs.io/en/3.3.x/reference/Image.html#PIL.Image.open>`_ method
to automatically rotate the image (by lossless methods) and update the Exif tag
accordingly if the image is a JPEG.

The package also features a save method that includes the Exif data by default when saving JPEGs.

Installation
------------

::

    pip install git+https://www.github.com/hbldh/autopil

Usage
-----

Demonstration of the monkey patching and how it works.

.. code:: python

   from PIL import Image
   import autopil

   img = Image.open('2016-08-28 15.11.44.jpg')
   print("{0}, Orientation: {1}".format(img, img._getexif().get(274)))

   autopil.monkey_patch()
   img_autorotated = Image.open('2016-08-28 15.11.44.jpg')
   print("{0}, Orientation: {1}".format(img_autorotated, img_autorotated._getexif().get(274)))

The output of the above:

.. code:: sh

   <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=4032x3024 at 0x7F44B5E4FF10>, Orientation: 6
   <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=3024x4032 at 0x7F44B5DF5150>, Orientation: 1

The package can also be used without monkey patching `PIL` and instead using the
`autopil.autopil_open` method directly:

.. code:: python

   from autopil import autopil_open
   img = autopil_open('2016-08-28 15.11.44.jpg')


Tests
~~~~~

TBD.

References
----------

.. [1] Exif on Wikipedia (`https://en.wikipedia.org/wiki/Exif`_)

.. [2] Exif orientation (`http://sylvana.net/jpegcrop/exif_orientation.html`_)


.. |Build Status| image:: https://travis-ci.org/hbldh/autopil.svg?branch=master
   :target: https://travis-ci.org/hbldh/autopil
.. |Coverage Status| image:: https://coveralls.io/repos/github/hbldh/autopil/badge.svg?branch=master
   :target: https://coveralls.io/github/hbldh/autopil?branch=master


