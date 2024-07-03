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
    'version': '0.1.4',
    'description': 'A Python functions library for working with GeoSPARQL data',
    'long_description': '# geosparqllib\n\nA Python functions library for working with GeoSPARQL data.\n\nProject home: <https://github.com/Kurrawong/geosparqllib/>\n\nThis Python library contains a series of functions for creating, using and otherwise working with GeoSPARQL RDF data.\n\nCommon tasks handled by this library are:\n\n* creating GeoSPARQL data from other spatial data\n* ...\n\n## Installation\n\nThis library is [available on PyPI](https://pypi.org/project/geosparqllib/) so can be installed using PIP:\n\n```\npip install geosparqllib\n```\n\nor Poetry:\n\n```\npoetry add geosparqllib\n```\n\n## Use\n\nHere\'s an example of using the `make_geometry()` function:\n\n```python\nfrom geosparqllib import make_geometry\n\nj = """\n    {\n      "type": "Feature",\n      "properties": {},\n      "geometry": {\n        "type": "Polygon", \n        "coordinates": [\n          [ \n            [0, 0], \n            [1, 0], \n            [1, 1], \n            [0, 1], \n            [0, 0] \n          ]\n        ]\n      }\n    }\n    """\nf = "http://example.com/f/1"\ngeom, bn = make_geometry(f, j)\nprint(geom.serialize(format="longturtle"))\n```\nreturns:\n```\nPREFIX geo: <http://www.opengis.net/ont/geosparql#>\n\n<http://example.com/f/1>\n    geo:hasGeometry\n        [\n            a geo:Geometry ;\n            geo:asWKT "POLYGON ((0 0, 1 0, 1 1, 0 1, 0 0))"^^geo:wktLiteral ;\n        ] ;\n.\n```\n\nSee further examples of use in this module\'s tests in its source code:\n\n* <https://github.com/Kurrawong/geosparqllib/tree/main/tests>\n\n## License\n\n[BSD- 3-Clause](https://opensource.org/license/BSD-3-clause) (and [in RDF](https://purl.org/NET/rdflicense/BSD3.0)).\n\n\n## Contact\n\nDeveloper:\n\n*Nicholas Car*  \n[KurrawongAI](https://kurrawong.ai)  \n<nick@kurrawong.ai>\n\n\n## Admin\n\n### Useful build commands\n\n```\n~$ poetry run pytest\n# update version in pyproject.toml\n~$ git commit -am "new version x.x.x"\n~$ git tag x.x.x\n~$ git push --tags\n~$ poetry build\n~$ poetry publish\n```',
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
