{
    'name': "The Real Estate Advertisement",
    'version': '1.0',
    'depends': ['base'],  # The only necessary framework module for now is base.
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_menus.xml',
        'views/res_users_views.xml'
    ],
    'application': True  # The key so that the module appears when the ‘Apps’ filter is on.
}