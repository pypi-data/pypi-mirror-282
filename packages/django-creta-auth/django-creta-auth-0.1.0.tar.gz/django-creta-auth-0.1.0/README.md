# django_creta_auth

**Current version: 0.1.0**

Boilerplate for a Django Package

## 1. Installation

The preferred installation method is directly from pypi:

```bash
# Install the package.
$ pip install -U django_creta_auth
```

## Quickstart

1. Add django_creta_auth to your INSTALLED_APPS in settings.py:

```python
INSTALLED_APPS = [
    ...,
    'django_creta_auth'
]
```

2. Include the django_creta_auth URLs in your urls.py:

```python
from django.urls import path, include

urlpatterns = [
    ...,
    path('auth/', include('django_creta_auth.urls')),
]
```

3. Run ``python manage.py migrate``
   Create the models.

```bash
BASE_URL = 'https://...'
```

4. Run ``python manage.py migrate``
   Create the models.

```bash
$ python manage.py migrate
```

## 3. Configuration

- Language setting: Todo

## 4. Update Package

In ``setup.cfg``, upgrade version

```
[metadata]
name = django-creta-auth
version = x.x.x
...
```

Build package

```bash
$ python setup.py sdist bdist_wheel
```

Deploy package

```bash
$ twine upload --verbose dist/django-creta-auth-x.x.x.tar.gz
```

## The MIT License

Copyright (c) 2023 Runners Co., Ltd.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
