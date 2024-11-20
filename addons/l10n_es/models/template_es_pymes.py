# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models, _
from odoo.addons.account.models.chart_template import template


class AccountChartTemplate(models.AbstractModel):
    _inherit = ['account.chart.template']

    @template('es_pymes')
    def _get_es_pymes_template_data(self):
        return {
            'name': _('SMEs (2008)'),
            'parent': 'es_common',
            'sequence': 0,
        }

    @template('es_pymes', 'res.company')
    def _get_es_pymes_res_company(self):
        return {
            self.env.company.id: {
                'account_fiscal_country_id': 'base.es',
                'bank_account_code_prefix': '572',
                'cash_account_code_prefix': '570',
                'transfer_account_code_prefix': '57299',
                'account_sale_tax_id': 'account_tax_template_s_iva21b',
                'account_purchase_tax_id': 'account_tax_template_p_iva21_bc',
            },
        }
