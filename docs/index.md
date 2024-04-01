# Template for LLM Development, Incorporating Relevant Documentation


## Developing Requirements

Python version `python3.10` or later.

### Build `venv` for **MacOS**, **Linux**
```shell
$ python3.10 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ deactivate
$ rm -rf venv     # remove the venv
```

### Build `venv` for **Windows**
```shell
$ pip install virtualenv
$ virtualenv venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
$ deactivate
$ rmdir /s venv     # remove the venv
```

## Build docs

### Requirements

```shell
pip install mkdocs
pip install mkdocs-material
pip install pymdown-extensions
pip install mkdocstrings
pip install mkdocs-git-revision-date-plugin
pip install mkdocs-jupyter
pip install ipykernel
```

### In localhost

```shell
$ mkdocs server
```

If you want to build the docs successfully, there are some requirements:
1. Make sure the repository is public.
2. Go to `setting` -> `Pages` -> `Branch` -> `gh-pages` -> `Save`.
<!-- 3. Go to `setting` -> `Actions` -> `Workflow permissions` -> Change to `Read and write permissions`. -->