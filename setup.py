from setuptools import setup

__project__ = 'mcpi-r'
__desc__ = 'Библиотека для программирования на Python + Minecraft (Russian) FIX'
__version__ = '1.0'
__author__ = "Flapchick"
__license__ = 'MIT'
__url__ = 'https://github.com/martinohanlon/mcpi'
__long_description__ = """# Minecraft: Pi edition API Python Library
`mcpi` Python library for communicating with [Minecraft: Pi edition](https://minecraft.net/en-us/edition/pi/) and [RaspberryJuice](https://github.com/zhuowei/RaspberryJuice).
Visit [github.com/martinohanlon/mcpi](https://github.com/martinohanlon/mcpi) for more information.
"""

__classifiers__ = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Education",
    "Intended Audience :: Developers",
    "Topic :: Education",
    "Topic :: Games/Entertainment",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
]

setup(name=__project__,
      version = __version__,
      description = __desc__,
      long_description=__long_description__,
      long_description_content_type='text/markdown',
      url = __url__,
      author = __author__,
      license = __license__,
      packages = [__project__],
      classifiers = __classifiers__,
      zip_safe=False)