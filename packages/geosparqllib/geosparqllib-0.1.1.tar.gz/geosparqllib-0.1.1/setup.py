# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['geosparqllib']

package_data = \
{'': ['*']}

install_requires = \
['rdflib>=7.0.0,<8.0.0', 'shapely>=2.0.4,<3.0.0']

setup_kwargs = {
    'name': 'geosparqllib',
    'version': '0.1.1',
    'description': 'A Python functions library for working with GeoSPARQL data',
    'long_description': '# geosparqllib\n\nA Python functions library for working with GeoSPARQL data.\n\nThis Python library contains a series of functions for creating, using and otherwise working with GeoSPARQL RDF data.\n\nCommon tasks handled by this library are:\n\n* creating GeoSPARQL data from other spatial data\n* ...\n\n## Installation\n\nThis is a Python library created using [the Poetry dependency manager](https://python-poetry.org/).\n\n## License\n\n[BSD- 3-Clause](https://opensource.org/license/BSD-3-clause) (and [in RDF](https://purl.org/NET/rdflicense/BSD3.0)).\n\n\n## Contact\n\nDeveloper:\n\n*Nicholas Car*  \n[KurrawongAI](https://kurrawong.ai)  \n<nick@kurrawong.ai>\n\n\n## Useful commands\n\n```\n~$ poetry run pytest\n# update version in pyproject.toml\n~$ git commit -am "new version x.x.x"\n~$ git tag x.x.x\n~$ git push --tags\n~$ poetry build\n~$ poetry publish\n```',
    'author': 'Nicholas Car',
    'author_email': 'nick@kurrawong.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
