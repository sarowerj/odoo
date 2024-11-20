# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, api


class L10n_LatamIdentificationType(models.Model):
    _inherit = ['l10n_latam.identification.type', 'pos.load.mixin']

    @api.model
    def _load_pos_data_domain(self, data):
        if self.env.company.country_id.code == "AR":
            return [('l10n_ar_afip_code', '!=', False), ('active', '=', True)]
        else:
            return super()._load_pos_data_domain(data)

    @api.model
    def _load_pos_data_fields(self, config_id):
        return ['name']