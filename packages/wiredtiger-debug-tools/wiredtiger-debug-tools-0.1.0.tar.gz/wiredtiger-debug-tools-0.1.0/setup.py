# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['wtd']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.7,<9.0.0', 'pymongo>=4.8.0,<5.0.0', 'rich>=13.7.1,<14.0.0']

entry_points = \
{'console_scripts': ['wtd = wtd.cli:main']}

setup_kwargs = {
    'name': 'wiredtiger-debug-tools',
    'version': '0.1.0',
    'description': 'Collections of tools to debug and analyze MongoDB WiredTiger files',
    'long_description': '# WiredTiger debug tools\nCollections of tools to debug and analyze MongoDB WiredTiger files\n',
    'author': 'Tommaso Tocci',
    'author_email': 'tommaso.tocci@mongodb.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
