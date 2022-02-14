__version__ = '1.0.0'
import os

from setuptools import setup, find_packages

# README read-in
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()
# END README read-in


setup(
    name='skytemple-eventserver',
    version=__version__,
    packages=find_packages(),
    description='Websocket server that emits SkyTemple UI events',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/SkyTemple/skytemple-eventserver/',
    install_requires=[],
    extras_require={
        'discord':  ["pypresence >= 4.0.0"]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
    ],
    entry_points='''
        [skytemple.module]
        eventserver=skytemple_eventserver.module:EventserverModule
    '''
)
