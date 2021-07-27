from odoo import models, fields, api

class ProductTempletInherit(models.Model):
    _inherit = 'product.template'

    matrial_type = fields.Many2one('matrial.type',string='Matrial Type',help='Select Matrial type for the current product')
    matrial_group = fields.Many2one('matrial.group',string='Matrial Group',help='Select Matrial group for the current product')
    
    thickness= fields.Float('Length',digits=(5,3))
    height = fields.Float('Height (mm)',digits=(5,3))
    max_aspect_ratio = fields.Float(' Max. Aspect Ratio',digits=(5,3))
    width = fields.Float('Width (mm)',digits=(5,3))


    matrial_types = fields.Many2one('matrial.type',string='Matrial Type',help='Select Matrial type for the current product')
    matrial_groups = fields.Many2one('matrial.group',string='Matrial Group',help='Select Matrial group for the current product')
    
    thicknes= fields.Float('Length',digits=(5,3))
    hei = fields.Float('Height (mm)',digits=(5,3))
    wid = fields.Float('Width (mm)',digits=(5,3))
    max_aspect_rati = fields.Float(' Max. Aspect Ratio',digits=(5,3))



    @api.onchange('matrial_type')
    def matrial_type_change(self):
    	if not self.matrial_types:
    		self.matrial_types = self.matrial_type.name

    @api.onchange('matrial_group')
    def matrial_group_change(self):
    	if not self.matrial_groups:
    		self.matrial_groups = self.matrial_group.name

    @api.onchange('thickness')
    def thickness_change(self):
    	if not self.thicknes:
    		self.thicknes = self.thickness

    @api.onchange('height')
    def height_change(self):
    	if not self.hei:
    		self.hei = self.height
    @api.onchange('width')
    def wid_change(self):
    	if not self.wid:
    		self.wid = self.width

    @api.onchange('max_aspect_ratio')
    def max_aspect_ratio_change(self):
    	if not self.max_aspect_rati:
    		self.max_aspect_rati = self.max_aspect_ratio