from setuptools import setup, find_packages

VERSION = '1.1'
DOWNLOAD_URL = ('https://github.com/harsimrans/word-treasure/archive/'
                '{}.zip'.format(VERSION))
REQUIRES = []

PACKAGES = find_packages(exclude=["*.tests", "*.tests.*", "tests.*",
                                    "tests"])

add_keywords = dict(
    entry_points={
        'console_scripts': ['wt = word_treasure.word_treasure:main'],
    }, )

setup(
    name='word_treasure',
    version=VERSION,
    license='GNU GPL v3.0',
    author='harsimran singh',
    author_email='harsimransingh032@gmail.com',
    download_url=DOWNLOAD_URL,
    install_requires=REQUIRES,
    packages=PACKAGES,
    include_package_data=True,
    zip_safe=False,
    url='https://github.com/harsimrans/word-treasure',
    description='Simple tool to look up words with single command',
    **add_keywords
)
