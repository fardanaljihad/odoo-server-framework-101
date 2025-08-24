{
    'name': "The Real Estate Advertisement",
    'version': '1.0',
    'depends': ['base'],  # The only necessary framework module for now is base.
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
    ],
    'application': True  # The key so that the module appears when the ‘Apps’ filter is on.
}