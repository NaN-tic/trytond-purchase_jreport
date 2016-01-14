# This file is part purchase_jreport module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool, PoolMeta
from trytond.modules.jasper_reports.jasper import JasperReport

__all__ = ['PurchaseReport', 'PurchaseRequestReport']
__metaclass__ = PoolMeta


class PurchaseReport(JasperReport):
    __name__ = 'purchase.purchase'

    @classmethod
    def execute(cls, ids, data):
        pool = Pool()
        Config = pool.get('purchase.configuration')
        config = Config(1)
        parameters = {
            'purchase_qty_decimal': config.purchase_qty_decimal
            }
        if 'parameters' in data:
            data['parameters'] += parameters
        else:
            data['parameters'] = parameters
        return super(PurchaseReport, cls).execute(ids, data)


class PurchaseRequestReport(JasperReport):
    __name__ = 'purchase.purchase_request'

    @classmethod
    def execute(cls, ids, data):
        pool = Pool()
        Config = pool.get('purchase.configuration')
        config = Config(1)
        parameters = {
            'purchase_qty_decimal': config.purchase_qty_decimal
            }
        if 'parameters' in data:
            data['parameters'] += parameters
        else:
            data['parameters'] = parameters
        return super(PurchaseRequestReport, cls).execute(ids, data)
