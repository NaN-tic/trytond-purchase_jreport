# This file is part purchase_jreport module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from .configuration import *
from .purchase import *


def register():
    Pool.register(
        Configuration,
        PurchaseConfigurationCompany,
        module='purchase_jreport', type_='model'),
    Pool.register(
        PurchaseReport,
        PurchaseRequestReport,
        module='purchase_jreport', type_='report')
