from setuptools import setup

VERSION = '1.0'
DOWNLOAD_URL = ('https://github.com/harsimrans/word-treasure/archive/'
                '{}.zip'.format(VERSION))
REQUIRES = []

setup(
    name='word-treasure',
    version=VERSION,
    license='GNU GPL v3.0',
    author='harsimran singh',
    author_email='harsimransingh032@gmail.com',
    download_url=DOWNLOAD_URL,
    install_requires=REQUIRES,
    packages=['word-treasure'],
    include_package_data=True,
    zip_safe=False,
    url='https://github.com/harsimrans/word-treasure',
    description='Simple tool to look up words with single command',
)