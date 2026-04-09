{
    "name": "Test Odoo Module",
    "summary": "A module to test pre-commit hooks in Odoo",
    "version": "18.0.1.0.0",
    "category": "Extra Tools",
    "website": "https://github.com/OCA/python-precommit-demo",
    "license": "LGPL-3",
    "depends": ["base"],
    "external_dependencies": {
        "python": ["requests"],
    },
    "data": [
        "views/test_model_views.xml",
    ],
    "installable": True,
}
