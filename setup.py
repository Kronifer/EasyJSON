from distutils.core import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_des = f.read()
setup(
  name = 'kvJSON',         # How you named your package folder (MyLib)
  packages = ['kvJSON'],   # Chose the same as "name"
  version = '1.4.2',
  description = 'An easy way to work with JSON in Python.',
  long_description="""
  kvJSON
======

.. _a-python-library-for-interacting-with-json-in-a-key-value-format:

**A Python library for interacting with JSON in a key-value format.**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Source code is available
at https://github.com/Kronifer/kvJSON/**

**Docs are at https://kvjson.readthedocs.io/**

Examples:
---------

**Initialization**:

.. code:: py

   import kvJSON

   kvJSON.init("storage.json")

**Adding Data:**

.. code:: py

   import kvJSON

   kvJSON.init("storage.json")

   kvJSON.addData("key", "value")

Contributing:
-------------

To contribute, fork and make a pr. Honestly, if the addition makes sense
I'll add it, so I'm not gonna set guidelines.""", # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  author = 'Dillon Runke',                   # Type in your name
  author_email = 'dillonr5@live.wsd1.org',      # Type in your E-Mail
  url = 'https://github.com/Kronifer/kvJSON',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Kronifer/kvJSON/archive/v1.4.4.tar.gz',    # I explain this later on
  keywords = ['JSON', 'Data Storage'],   # Keywords that define your package best
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.8',
  ],
)
