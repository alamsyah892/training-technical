from odoo import _, api, fields, models
from random import randint

class PlaningRoleTraining(models.Model):
    _name = 'planing.role.training'
    _description = 'Planing Role Training'
    _order = 'name asc'
    _log_access = True
    
    def _get_default_color(self):
        return randint(1, 11)
    
    company_id_id = fields.Many2one('res.company', string='Company')


    active = fields.Boolean('Active', default=True)
    name = fields.Char('Nama Role', index=True)
    color = fields.Integer('Color', default=getDefaultColor())
    resource_ids = fields.Many2many(comodel_name='resource.resource',
                                    relation='planing_resource_ids',
                                    colom1='planing_role_id',
                                    colom2='resource_id',
                                    string='Resource')
    sequence = fields.integer('Sequence')
    
