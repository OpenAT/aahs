# -*- coding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################

{
    'name': 'ahch_config',
    'summary': """FCOM Customer AHCH Modifications""",
    'description': """
FCOM Customer Modifications
===========================

Use this Addon as a Base for all Customer specific Modifications containing:

- Default Settings (User Defaults, Accounts, Taxes, Project Stages, ...)
- View Modifications
- CSS Modifications (sass in scss format)
- Translations (i18n, pot, po)

    """,
    'author': 'Michael Karrer (michael.karrer@datadialog.net), DataDialog',
    'version': '1.0',
    'website': 'https://www.datadialog.net',
    'installable': True,
    'depends': [
        'sale',
        'portal_sale',
        'website',
        'website_sale',
        'website_sale_donate',
    ],
    'data': [
        'views/templates.xml',
        'views/transactionstate_template.xml',
        'views/invoice_mail_template.xml',
        'views/salesorder_mail_template.xml',
    ],
}
