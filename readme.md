# Github scraper

Author: Carles Garcia Cabot

This **proof-of-concept** Github scraper can scrape repositories, issues and wikis. 
The queries are specified in JSON files. Proxies are supported.

### Features
- JSON files with keywords, proxies and type are supported.
- Coverage >90%.
- Uses requests and regex to find the targets.
- I've run black, isort and mypy for code quality.

### How to run:
I used Python 3.8, but I expect it to work with 3.7 or higher.
```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python main.py -i repositories.json
pytest --cov=. test_main.py
```

### Examples provided:
```bash
python main.py -i wikis.json
[{"url": "https://github.com//JeongtaekLim/TIL/wiki/JWT"}, {"url": "https://github.com//Altiimax/DevWebProject/wiki/12_References"}, {"url": "https://github.com//Altiimax/DevWebProject/wiki/12"}, {"url": "https://github.com//Altiimax/DevWebProject/wiki/Links"}, {"url": "https://github.com//tsrnd/dp-yashoes/wiki/Authenticate-package-in-django"}, {"url": "https://github.com//codestates/Devmap_client/wiki/Members"}, {"url": "https://github.com//balakrishnanm/mybook/wiki/Django-Authentication"}]

python main.py -i repositories.json
[{"url": "https://github.com/atuldjadhav/DropBox-Cloud-Storage"}, {"url": "https://github.com/michealbalogun/Horizon-dashboard"}]

python main.py -i issues.json
[{"url": "https://github.com/jazzband/djangorestframework-simplejwt/issues/71"}, {"url": "https://github.com/thiagoferreiraw/mentoring-program/issues/1"}, {"url": "https://github.com/Pr0Ger/PyAPNs2/issues/103"}, {"url": "https://github.com/barseghyanartur/django-mongoengine-filter/issues/12"}, {"url": "https://github.com/juanifioren/django-oidc-provider/issues/78"}]
```

### Things to improve
- make code more modular
- make code more fault tolerant
- add integration tests to test with real requests and responses
- add docstrings
