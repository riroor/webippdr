from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSale(WebsiteSale):
    @http.route([
        '''/shop''',
        '''/shop/page/<int:page>''',
        '''/shop/category/<model("product.public.category", "[('website_id', 'in', (False, current_website_id))]"):category>''',
        '''/shop/category/<model("product.public.category", "[('website_id', 'in', (False, current_website_id))]"):category>/page/<int:page>'''
    ], type='http', auth="public", website=True)
    def shop(self, page=0, category=None, search='', ppg=False, **post):
        res = \
            super(WebsiteSale, self).shop(
                page=page, category=category, search=search, ppg=ppg, **post)
        warehouse_env = request.env['stock.warehouse'].sudo()
        warehouses = warehouse_env.search([('code', 'in', ['Sdq', 'Puj'])])
        res.qcontext.update({'warehouses': warehouses,})
        return res

    @http.route(['/shop/product/<model("product.template"):product>'],
                type='http', auth="public", website=True)
    def product(self, product, category='', search='', **kwargs):
        res = \
            super(WebsiteSale, self).product(
                product, category=category, search=search, **kwargs)
        warehouse_env = request.env['stock.warehouse'].sudo()
        warehouses = warehouse_env.search([('code', 'in', ['Sdq', 'Puj'])])
        res.qcontext.update({'warehouses': warehouses, })
        return res
