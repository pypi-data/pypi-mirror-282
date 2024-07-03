import pathlib
import sys
from setuptools import setup, find_packages


HERE = pathlib.Path(__file__).parent
VERSION = '0.15'
PACKAGE_NAME = 'oslili'
AUTHOR = 'Oscar Valenzuela B.'
AUTHOR_EMAIL = 'alkamod@gmail.com'
URL = 'https://github.com/oscarvalenzuelab/oslili'
LICENSE = 'Apache-2.0'
DESCRIPTION = 'Open Source License Identification Library'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    license=LICENSE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    packages=['oslili', 'oslili.spdx', 'oslili.datasets'],
    install_requires=["scikit-learn==1.4.2", "ssdeep" ],
    url=URL,
    package_data={
        "oslili.spdx": ["*.txt",],
        "oslili.datasets": ["*",],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux',
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License'
    ],
)
