try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from __version__ import __version__

classifiers = """
Environment :: Console
Intended Audience :: Developers
License :: OSI Approved :: Apache Software License
Operating System :: OS Independent
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3.3
Programming Language :: Python :: 3.4
Programming Language :: Python :: 3.5
Topic :: Software Development :: Quality Assurance
Topic :: Software Development :: Testing
"""

classifier_list = [c for c in classifiers.split("\n") if c]

setup(name='pymox',
      version=__version__,
      py_modules=['mox', 'stubout', '__version__'],
      url='http://pymox.rtfd.io',
      maintainer='pymox maintainers',
      maintainer_email='mox-discuss@googlegroups.com',
      license='Apache License, Version 2.0',
      description='Mock object framework',
      classifiers=classifier_list,
      include_package_data=True,
      install_requires=['six'],
      long_description='''Pymox is an open source mock object framework for Python.
''',
      )
