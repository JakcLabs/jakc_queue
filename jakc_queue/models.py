from openerp import models, fields, api

AVAILABLE_STATES = [
    ('draft','New'),
    ('open','Active'),    
    ('done','Closed'),
]

AVAILABLE_PICKUP = [
    ('desktop','Desktop'),
    ('device','Device'),
]

AVAILABLE_DISPLAY = [
    ('single','Single'),
    ('route','Route'),
]

class Queue_display(models.Model):
    _name = 'queue.display'
    name = fields.Char('Display Code', size=4, required=True)
    display_type = fields.Selection(AVAILABLE_DISPLAY,'Display Type', size=16, required=True)
    font_size = fields.Integer('Font Size',default=10)
    state = fields.Selection(AVAILABLE_STATES,'Status',size=16,readonly=True, default='open')
      
class Queue_type(models.Model):
    _name = 'queue.type'
    name = fields.Char('Name', size=30, required=True)
    number = fields.Integer('Number', default=0)
    is_active = fields.Boolean('Active', default=False) 
    state = fields.Selection(AVAILABLE_STATES, 'Status', size=16 , readonly=True, default='open')

class Queue_pickup(models.Model):
    _name = 'queue.pickup'
    name = fields.Char('Pickup Code', size=4, required=True)
    pickup_type = fields.Selection(AVAILABLE_PICKUP, 'Pickup Type', size=16, required=True)
    type_id = fields.Many2one('queue.type','Queue Type',index=True, required=True)
    display_id = fields.Many2one('queue.display','Display', index=True, required=True)
    is_active = fields.Boolean('Is Active',default=False)
    state = fields.Selection(AVAILABLE_STATES, 'Status', size=16, readonly=True, default='open')

class Queue_pickup_log(models.Model):
    _name = 'queue.pickup.log'
    pickup_id = fields.Many2one('queue.pickup','Pickup',index=True)
    queue_type_id = fields.Many2one('queue.type','Queue Type',index=True)
    log_in = fields.Datetime('Log In')
    log_out = fields.Datetime('Log Out')
    state = fields.Selection(AVAILABLE_STATES, 'Status', size=16, readonly=True , default='open')

class Queue_trans(models.Model):
    _name = 'queue.trans'
    trans_id = fields.Char('Transaction ID', size=4, required=True)
    trans_date = fields.Date('Date', required=True , default=fields.Date.today)
    type_id = fields.Many2one('queue.type', 'Type', index=True)
    display_id = fields.Many2one('queue.display','Display',index=True)
    start_date_time = fields.Datetime('Start Time', default=fields.Datetime.now)
    is_pickup = fields.Boolean('Is Pickup', default=False)    
    pickup_date_time = fields.Datetime('Pickup Time')    
    end_date_time = fields.Datetime('End Time')
    printed = fields.Boolean('Printed',default=False)    
    state = fields.Selection(AVAILABLE_STATES, 'Status', size=16, readonly=True , default='draft')

    @api.model
    def create(self,values):
        result = super(Queue_trans,self).create(values)
        trans_data = {}
        trans_data.update({'trans_id': result.id})
        self.env['queue.trans.print'].create(trans_data)
        self.env['queue.trans.sound'].create(trans_data)
        return result
        
        
class Queue_trans_print(models.Model):
    _name = 'queue.trans.print'
    trans_id = fields.Many2one('queue.trans', 'Transaction ID', index=True)
    trans_date_time = fields.Datetime('Date and Time', default=fields.Datetime.now)
    state = fields.Selection(AVAILABLE_STATES, 'Status', size=16, readonly=True, default='open')
    

class Queue_trans_sound(models.Model):    
    _name = 'queue.trans.sound'
    trans_id = fields.Many2one('queue.trans', 'Transaction ID', index=True)
    trans_date_time = fields.Datetime('Date and Time', default=fields.Datetime.now)
    state = fields.Selection(AVAILABLE_STATES, 'Status', size=16, readonly=True, default='open')
    

    
    
    