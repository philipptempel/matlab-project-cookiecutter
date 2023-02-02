import urllib.request

# Download the file from `url` and save it locally under `file_name`:
src = 'https://github.com/philipptempel/matlab-project-cookiecutter/license/{{ cookiecutter.license }}'
dst = pl.Path.cwd() / 'LICENSE'

urllib.request.urlretrieve(src, str(dst))
