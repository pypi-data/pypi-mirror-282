import os

from odoo import http
from odoo.addons.web.controllers.home import Home
from odoo.addons.web.controllers.utils import ensure_db
from odoo.tools.translate import _


class CustomLoginController(Home):
    @http.route("/web/login", type="http", auth="none")
    def web_login(self, *args, **kw):
        ensure_db()
        allow_odoo_login = os.getenv("ODOO_ALLOW_ODOO_LOGIN", False)
        # This is a hack to force error triggering when allow_odoo_login is set
        if http.request.httprequest.method == "POST" and not allow_odoo_login:
            http.request.params['password'] = ''
        response = super(CustomLoginController, self).web_login(*args, **kw)
        if http.request.httprequest.method == "POST" and not allow_odoo_login:
            response.qcontext['error'] = _("The Odoo login is disabled")
        response.qcontext['allow_odoo_login'] = allow_odoo_login
        return response

