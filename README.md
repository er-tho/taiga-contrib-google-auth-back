Taiga contrib google auth
=========================

A Taiga plugin for google oauth2 authentication (Ported from official gitlab auth).

Installation
------------
### Production env

#### Taiga Back

In your Taiga back python virtualenv install the pip package `taiga-contrib-google-auth-x` with:

```bash
   pip install git+https://github.com/er-tho/taiga-contrib-google-auth-x
```

Modify your `settings/local.py` and include the following lines:

```python
    INSTALLED_APPS += ["taiga_contrib_google_auth_x"]

    # Get these from https://console.cloud.google.com/apis/credentials

    GOOGLE_API_CLIENT_ID = "YOUR_GOOGLE_API_CLIENT_ID"
    GOOGLE_API_CLIENT_SECRET = "YOUR_GOOGLE_API_CLIENT_SECRET"
    GOOGLE_API_REDIRECT_URI = "YOUR_GOOGLE_API_REDIRECT_URI"
    GOOGLE_RESTRICT_LOGIN = ["YOUR_DOMAIN_1","YOUR_DOMAIN_2"]
```
You can ommit `GOOGLE_RESTRICT_LOGIN` if unnecessary.

#### Taiga Front

Download in your `dist/plugins/` directory of Taiga front the content of `taiga-contrib-google-auth-x/front/dist`:

```bash
  cd dist/
  mkdir -p plugins/google-auth
  cd plugins/google-auth
  (clone front/dist dir here)
```

Include in your `dist/conf.json` in the 'contribPlugins' list the value `"/plugins/google-auth/google-auth.json"`:

```json
...
    "googleClientId": "YOUR-GOOGLE-CLIENT-ID",
    "contribPlugins": [
        (...)
        "/plugins/google-auth/google-auth.json"
    ]
...
```

### Dev env

#### Taiga Back

Clone the repo and

```bash
  cd taiga-contrib-google-auth-x
  workon taiga
  pip install -e .
```

Modify `taiga-back/settings/local.py` and include the lines:

```python
    INSTALLED_APPS += ["taiga_contrib_google_auth_x"]

    # Get these from https://console.cloud.google.com/apis/credentials

    GOOGLE_API_CLIENT_ID = "YOUR_GOOGLE_API_CLIENT_ID"
    GOOGLE_API_CLIENT_SECRET = "YOUR_GOOGLE_API_CLIENT_SECRET"
    GOOGLE_API_REDIRECT_URI = "YOUR_GOOGLE_API_REDIRECT_URI"
    GOOGLE_RESTRICT_LOGIN = ["YOUR_DOMAIN_1","YOUR_DOMAIN_2"]
```

#### Taiga Front

After clone the repo link `dist` in `taiga-front` plugins directory:

```bash
  cd taiga-front/dist
  mkdir -p plugins
  cd plugins
  ln -s ../../../taiga-contrib-google-auth-x/front/dist google-auth
```

Include in your `dist/conf.json` in the 'contribPlugins' list the value `"/plugins/google-auth/google-auth.json"`:

```json
...
    "googleClientId": "YOUR-GOOGLE-CLIENT-ID",
    "contribPlugins": [
        (...)
        "/plugins/google-auth/google-auth.json"
    ]
...
```

In the plugin source dir `taiga-contrib-google-auth-x/front` run

```bash
npm install
```
and use:

- `gulp` to regenerate the source and watch for changes.
- `gulp build` to only regenerate the source.

Running tests
-------------

We only have backend tests, you have to add your `taiga-back` directory to the
PYTHONPATH environment variable, and run py.test, for example:

```bash
  cd back
  add2virtualenv /home/taiga/taiga-back/
  py.test
```
