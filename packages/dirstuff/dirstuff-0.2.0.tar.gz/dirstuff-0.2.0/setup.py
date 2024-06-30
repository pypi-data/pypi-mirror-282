# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dirstuff', 'dirstuff._cli', 'dirstuff.os', 'dirstuff.summary']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.0,<9.0.0', 'colorama>=0.4.0,<0.5.0']

entry_points = \
{'console_scripts': ['dirstuff = dirstuff._cli.main:main']}

setup_kwargs = {
    'name': 'dirstuff',
    'version': '0.2.0',
    'description': 'Directory summary tool.',
    'long_description': '<div align="center">\n  <img src="assets/dirstuff-banner.png">\n  <h1>dirstuff</h1>\n\n  <p>\n    <strong>utilities for filesystem operations</strong>\n  </p>\n\n  <br>\n  <div>\n    <a href="https://badge.fury.io/py/dirstuff"><img src="https://badge.fury.io/py/dirstuff.svg" alt="PyPI"></a>\n    <a href="https://pepy.tech/project/dirstuff"><img src="https://pepy.tech/badge/dirstuff" alt="Downloads"></a>\n  </div>\n  <br>\n</div>\n\n## Installation\n\nInstall the current PyPI release:\n\n```bash\npip install dirstuff\n```\n\n## Path utilities\n\ndirstuff provides some Python utilities for interacting with the filesystem.\n\n- rename\n- move\n- copy\n- delete\n- walk\n\n### Rename files with a regex\n\nIn this example we iterate over nested folders that contain .txt files and rename them to have .md extensions.\n\n```python\nfrom dirstuff import Dir\n\nd = Dir("my_folder")\nfor sub in d.iter_dirs():\n    for f in sub.iter_files():\n        f.rename_regex(r"([a-z]*)\\.txt", r"\\1.md")\n```\n\n### Delete a folder\n\nNo need to switch between `pathlib` and `shutil` packages. All filesystem utilities are available on the `Dir` class.\n\n```python\nfrom dirstuff import Dir\n\nd = Dir("my_folder")\nd.delete()\n```\n\n## Summarization\n\n### Tree\n\nSummarize a directory recursively by file size. This tool can be used to quickly search a drive for large files taking up too much space.\n\n```bash\n# Summarize the /home/user/my_documents directory\n# showing only directories greater than 20MB in size\n$ dirstuff tree /home/user/my_documents --size 20MB\n```\n\n```python\n|->  69.0 GB > my_documents\n    |->  67.8 GB > movies\n        |->  62.0 GB > from_the_internet\n        |->   5.8 GB > home_movies\n    |-> 638.1 MB > photos\n        |-> 368.2 MB > rock_concert\n        |-> 251.6 MB > vacation_2019\n        |->  18.4 MB > family_photos\n    |-> 521.6 MB > work\n        |-> 263.8 MB > boring_docs\n        |-> 257.7 MB > reports\n    |->  22.5 MB > games\n```\n\n> You can show the full absolute paths with `--absolute`\n\n### Search\n\nSearch for all folders with a matching name.\n\n```bash\n# List all node_modules folders under the /code/projects directory\n$ dirstuff search /code/projects node_modules --absolute\n```\n\n```python\n |-> 419.6 MB > /code/projects/portfolio/web/node_modules\n |-> 320.3 MB > /code/projects/fun_project/node_modules\n |-> 298.1 MB > /code/projects/simple_game/version_2/node_modules\n```\n\n> The same `--size` option also works with the search command\n',
    'author': 'Chris Gregory',
    'author_email': 'christopher.b.gregory@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/gregorybchris/dirstuff',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11',
}


setup(**setup_kwargs)
