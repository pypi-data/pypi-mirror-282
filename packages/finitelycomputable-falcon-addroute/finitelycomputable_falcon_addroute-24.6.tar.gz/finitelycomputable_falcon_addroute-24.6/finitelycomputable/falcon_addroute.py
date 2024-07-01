import falcon
from importlib import import_module, metadata
from os import environ
from platform import python_version
from posixpath import join


class Index(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_HTML
        apps_list_items = '''</li>
  <li>'''.join(included_apps.values())
        resp.text = (f'''<!DOCTYPE html><html><body>
<h1>Finitely Computable Microsites</h1>
<h2>Falcon framework (addroute method)</h2>
<a href="https://pypi.org/project/finitelycomputable-falcon-addroute/">
  {__name__}</a>
{metadata.version(__name__)} is available on
<a href="https://pypi.org/">PyPi</a>
<h3>Available Microsites</h3>
<ul>
  <li>{apps_list_items}</li>
</ul>
<a href="{join(base_path, "wsgi_info")}">wsgi info</a>
<h3>Source Code</h3>
<ul>
  <li><a href="https://git.sr.ht/~thrasymache/finitelycomputable-microsites">
    Sourcehut
  </a></li>
  <li><a href="https://notabug.org/thrasymache/finitelycomputable-microsites">
    Notabug
  </a></li>
  <li><a href="https://gitlab.com/thrasymache/microsites">
    Gitlab
  </a></li>
  <li><a href="https://github.com/thrasymache/microsites">
    Github
  </a></li>
</ul>
</body></html>'''
        )


class WsgiInfo(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_HTML
        dist_list_items = '''</li>
  <li>'''.join([f'{d.name} version {d.version}'
            for d in [metadata.distribution(j) for j in
                metadata.packages_distributions()['finitelycomputable']]
        ])
        apps_list_items = '''</li>
  <li>'''.join([f'{v} installed at {k}' for k, v in included_apps.items()])
        resp.text = (f'''<!DOCTYPE html><html><body>
Microsites Version "{version_text}"<br> using
<a href="https://pypi.org/project/finitelycomputable-falcon-addroute/">
  {__name__}</a>
{metadata.version(__name__)}<br>
on falcon version {metadata.distribution('falcon').version}<br>
on Python {python_version()}<br>
at {base_path} with the following apps
<ul>
  <li>{apps_list_items}</li>
</ul>
and the following finitelycomputable packages
<ul>
  <li>{dist_list_items}</li>
</ul>
</body></html>'''
        )

def include_app(name, app_path):
    ab_name = "finitelycomputable." + name
    pack_stem = "finitelycomputable-" + name.replace("_", "-")
    module = import_module(ab_name)
    pack = module.add_routes.__module__
    dists = [d for d in metadata.packages_distributions()['finitelycomputable']
            if d.startswith(pack_stem)]
    if dists:
        dm = metadata.distribution(dists[0])
        included_apps[pack] = f'<a href={app_path}>{dm.name}</a> {dm.version}'
    else:
        included_apps[pack] = f'<a href={app_path}>{ab_name}</a> unknown version'
    return module

def add_routes(application, base_path):
    application.add_route(base_path, Index())
    application.add_route(join(base_path, 'wsgi_info'), WsgiInfo())

application = falcon.App(media_type=falcon.MEDIA_HTML)
application.req_options.strip_url_path_trailing_slash = True
base_path = join('/', environ.get('BASE_PATH', ''))
version_text = environ.get('MICROSITES_VERSION_TEXT', '')
included_apps = {}
add_routes(application, base_path)

try:
    app_path = join(base_path, 'hello_world')
    module = include_app("helloworld_falcon", app_path)
    module.add_routes(application, app_path)
except ModuleNotFoundError:
    pass

try:
    app_path = join(base_path, 'identification_of_trust')
    module = include_app("idtrust_falcon", app_path)
    module.add_routes(application, app_path)
except ModuleNotFoundError:
    pass

def run():
    from sys import argv, exit, stderr
    usage = f'usage: {argv[0]} run [port]\n'
    if len(argv) < 2:
        stderr.write(usage)
        exit(1)
    if argv[1] == 'run':
        from wsgiref import simple_server
        try:
            port=int(argv[2])
        except IndexError:
            port=8080
        simple_server.make_server('0.0.0.0', port, application).serve_forever()
    else:
        stderr.write(usage)
        exit(1)
