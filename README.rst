imdirect
========

|Build Status| |Coverage Status|

The orientation of the photographed
object or scene with respect to the digital camera is encoded in the resulting
image's [1]_ data (given that it is saved as a JPEG). When working with such digital camera images,
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

    pip install git+https://www.github.com/hbldh/imdirect

Usage
-----

Demonstration of the monkey patching and how it works.

.. code:: python

   from PIL import Image
   import imdirect

   img = Image.open('2016-08-28 15.11.44.jpg')
   # Print image as string and the EXIF orientation.
   print(img)
   print("Orientation: {0}".format(img._getexif().get(274)))

   # Apply the autorotate monkey patch.
   imdirect.monkey_patch()
   img_autorotated = Image.open('2016-08-28 15.11.44.jpg')
   print(img_autorotated)
   print("Orientation: {0}".format(img_autorotated._getexif().get(274)))

The output of the above:

.. code:: python

   <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=4032x3024 at 0x7FC3238AC810>
   Orientation: 6
   <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=3024x4032 at 0x7FC323875250>
   Orientation: 1




Tests
~~~~~

TBD.

References
----------

.. [1] `Exif <https://en.wikipedia.org/wiki/Exif>`_

.. [2] `Exif on Wikipedia <https://en.wikipedia.org/wiki/Exif>`_




.. |Build Status| image:: https://travis-ci.org/hbldh/imdirect.svg?branch=master
   :target: https://travis-ci.org/hbldh/imdirect
.. |Coverage Status| image:: https://coveralls.io/repos/github/hbldh/imdirect/badge.svg?branch=master
   :target: https://coveralls.io/github/hbldh/imdirect?branch=master


