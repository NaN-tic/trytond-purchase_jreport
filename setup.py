#!/usr/bin/env python
# This file is part purchase_jreport module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.

from setuptools import setup
import re
import ConfigParser

MODULE2PREFIX = {
    'jasper_reports_options': 'trytonzz',
    'party_lang': 'trytonzz',
    'purchase_payment_type': 'trytonspain',
}

config = ConfigParser.ConfigParser()
config.readfp(open('tryton.cfg'))
info = dict(config.items('tryton'))
for key in ('depends', 'extras_depend', 'xml'):
    if key in info:
        info[key] = info[key].strip().splitlines()
major_version, minor_version, _ = info.get('version', '0.0.1').split('.', 2)
major_version = int(major_version)
minor_version = int(minor_version)

def get_require_version(name):
    if minor_version % 2:
        require = '%s >= %s.%s.dev0, < %s.%s'
    else:
        require = '%s >= %s.%s, < %s.%s'
    require %= (
        name, major_version, minor_version, major_version, minor_version + 1)
    return require

requires = []
for dep in info.get('depends', []):
    if not re.match(r'(ir|res|webdav)(\W|$)', dep):
        prefix = MODULE2PREFIX.get(dep, 'trytond')
        requires.append(
            '%s_%s >= %s.%s, < %s.%s' %
            (prefix, dep, major_version, minor_version,
                major_version, minor_version + 1))
requires.append(get_require_version('trytond'))


setup(name='trytonzz_purchase_jreport',
    version=info.get('version', '0.0.1'),
    description='Tryton module to Jasper Report for purchase order',
    author='Zikzakmedia SL',
    author_email='zikzak@zikzakmedia.com',
    url='http://www.zikzakmedia.com',
    download_url="https://bitbucket.org/trytonspain/trytond-purchase_jreport",
    package_dir={'trytond.modules.purchase_jreport': '.'},
    packages=[
        'trytond.modules.purchase_jreport',
        'trytond.modules.purchase_jreport.tests',
        ],
    package_data={
        'trytond.modules.purchase_jreport': info.get('xml', []) \
            + ['tryton.cfg', 'locale/*.po', '*.jrxml'],
        },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Framework :: Tryton',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Legal Industry',
        'Intended Audience :: Manufacturing',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: Catalan',
        'Natural Language :: Spanish',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Office/Business',
        ],
    license='GPL-3',
    install_requires=requires,
    zip_safe=False,
    entry_points="""
    [trytond.modules]
    purchase_jreport = trytond.modules.purchase_jreport
    """,
    test_suite='tests',
    test_loader='trytond.test_loader:Loader',
)
