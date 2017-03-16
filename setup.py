import os, sys
from setuptools import find_packages, setup

install_requires = ['boto>=2.2.1']

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
    CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()
except IOError:
    README = "boto-rsync is a rough adaptation of boto's s3put script " + \
             "which has been reengineered to more closely mimic rsync. Its " + \
             "goal is to provide a familiar rsync-like wrapper for boto's " + \
             "S3 and Google Storage interfaces."
    CHANGES = ''

setup(
    name='boto_rsync3',
    version='0.8.1',
    author='Seth Davis',
    author_email='seth@curiasolutions.com',
    description="An rsync-like wrapper for boto's S3 and Google Storage " + \
                "interfaces.",
    long_description=README + '\n\n' + CHANGES,
    url='http://github.com/codeforamerica/boto_rsync3',
    keywords='rsync for boto and python 3',
    packages=[],
    install_requires=install_requires,
    scripts=['bin/boto-rsync3'],
    license = "MIT",
    platforms = "Posix; MacOS X; Windows",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Utilities',
        'Topic :: System :: Archiving',
        'Topic :: System :: Archiving :: Backup',
        'Topic :: System :: Archiving :: Mirroring'
    ]
)
