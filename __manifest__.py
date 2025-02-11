{
    'name': 'Sale No Duplicate',
    'version': '17.0.1.0.0',
    'category': 'Sales',
    'summary': 'Restringe la duplicación de pedidos de venta y oculta el botón de duplicar.',
    'description': '''
        Este módulo evita que los usuarios puedan duplicar registros de ventas:
          - Oculta el botón de duplicar en el formulario de Sales.
          - Lanza un error si se intenta duplicar un registro desde otras rutas.
    ''',
    'author': 'Alphaqueb Consulting SAS',
    'website': 'https://alphaqueb.com',
    'license': 'LGPL-3',
    'depends': [
        'sale'
    ],
    'data': [
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
