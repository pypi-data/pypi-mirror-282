# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['libgen_api_modern']

package_data = \
{'': ['*']}

install_requires = \
['bs4>=0.0.2,<0.0.3', 'requests>=2.32.3,<3.0.0']

entry_points = \
{'console_scripts': ['libgen_api_modern = libgen_api_modern:main']}

setup_kwargs = {
    'name': 'libgen-api-modern',
    'version': '0.1.0',
    'description': 'Search Library Genesis',
    'long_description': '# libgen-api-modern\n\nSearch Library Genesis programmatically using an enhanced Python library. This fork extends the original `libgen-api` by [Harrison Broadbent](https://github.com/harrison-broadbent/libgen-api) and `libgen-api-enhanced` by [Onurhan](https://github.com/onurhanak/libgen-api-enhanced) with added features like direct download links and book cover links. It also returns 100 results by default.\n\n## Contents\n\n- [libgen-api-modern](#libgen-api-modern)\n  - [Contents](#contents)\n  - [Getting Started](#getting-started)\n  - [Basic Searching:](#basic-searching)\n    - [Title:](#title)\n    - [Author:](#author)\n  - [Filtered Searching](#filtered-searching)\n    - [Filtered Title Searching](#filtered-title-searching)\n    - [Filtered Author Searching](#filtered-author-searching)\n    - [Non-exact Filtered Searching](#non-exact-filtered-searching)\n  - [Results Layout](#results-layout)\n  - [Contributors](#contributors)\n\n## Getting Started\n\nInstall the package -\n\n```\npip install libgen-api-modern\n```\n\nPerform a basic search -\n\n```python\n# search_title()\n\nfrom libgen_api_enhanced import LibgenSearch\ns = LibgenSearch()\nresults = s.search_title("Pride and Prejudice")\nprint(results)\n```\n\nCheck out the [results layout](#results-layout) to see available fields and how the results data is formatted.\n\n## Basic Searching:\nSearch by title or author:\n\n### Title:\n\n```python\n# search_title()\n\nfrom libgen_api_enhanced import LibgenSearch\ns = LibgenSearch()\nresults = s.search_title("Pride and Prejudice")\nprint(results)\n```\n\n### Author:\n\n```python\n# search_author()\n\nfrom libgen_api_enhanced import LibgenSearch\ns = LibgenSearch()\nresults = s.search_author("Jane Austen")\nprint(results)\n```\n\n## Filtered Searching\n\n- You can define a set of filters, and then use them to filter the search results that get returned.\n- By default, filtering will remove results that do not match the filters exactly (case-sensitive) -\n  - This can be adjusted by setting `exact_match=False` when calling one of the filter methods, which allows for case-insensitive and substring filtering.\n\n### Filtered Title Searching\n\n```python\n# search_title_filtered()\n\nfrom libgen_api_enhanced import LibgenSearch\n\ntf = LibgenSearch()\ntitle_filters = {"Year": "2007", "Extension": "epub"}\ntitles = tf.search_title_filtered("Pride and Prejudice", title_filters, exact_match=True)\nprint(titles)\n```\n\n### Filtered Author Searching\n\n```python\n# search_author_filtered()\n\nfrom libgen_api_enhanced import LibgenSearch\n\naf = LibgenSearch()\nauthor_filters = {"Language": "German", "Year": "2009"}\ntitles = af.search_author_filtered("Agatha Christie", author_filters, exact_match=True)\nprint(titles)\n```\n\n### Non-exact Filtered Searching\n\n```python\n# search_author_filtered(exact_match = False)\n\nfrom libgen_api_enhanced import LibgenSearch\n\nne_af = LibgenSearch()\npartial_filters = {"Year": "200"}\ntitles = ne_af.search_author_filtered("Agatha Christie", partial_filters, exact_match=False)\nprint(titles)\n\n```\n\n## Results Layout\n\nResults are returned as a list of dictionaries:\n\n```json\n[\n  {\n    "ID": "123456",\n    "Author": "John Smith",\n    "Title": "Title",\n    "Publisher": "Publisher",\n    "Year": "2021"\n    "Pages": "410",\n    "Language": "German",\n    "Size": "1005 Kb",\n    "Extension": "epub",\n    "Mirror_1": "http://example.com",\n    "Mirror_2": "http://example.com",\n    "Mirror_3": "http://example.com",\n    "Mirror_4": "http://example.com",\n    "Mirror_5": "http://example.com",\n    "Direct_Download_Link": "http://example.com",\n    "Cover": "https://covers.openlibrary.org/b/olid/OL1234-M.jpg"\n  }]\n```\n\n## Contributors\n\nPlease don\'t hesitate to raise an issue, or fork this project and improve on it.\n\nThanks to the following people:\n\n- [harrison-broadbent](https://github.com/harrison-broadbent) who wrote the original Libgen API.\n- [calmoo](https://github.com/calmoo)\n- [HENRYMARTIN5](https://github.com/HENRYMARTIN5)\n- [Onurhan](https://github.com/onurhanak)',
    'author': 'Johnnie',
    'author_email': '99084912+johnnie-610@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<3.12',
}


setup(**setup_kwargs)
