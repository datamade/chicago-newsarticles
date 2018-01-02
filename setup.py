import os
from setuptools import setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='chicago-newsarticles',
    packages=['newsarticles'],
    include_package_data=True,
    license='GPL v3.0',
    description='Scraper for news articles from Chicago media',
    author='',
    author_email='',
    install_requires=['html2text',
                      'feedparser',
                      'bs4',
                      'Django>=1.11,<2.0',
                      'PyYAML'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
