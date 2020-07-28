from setuptools import setup
setup(
    name = 'laborterminal-cli',
    version = '0.1.0',
    packages = ['laborterminal'],
    entry_points = {
        'console_scripts': [
            'laborterminal = laborterminal.__main__:main'
        ]
    })
