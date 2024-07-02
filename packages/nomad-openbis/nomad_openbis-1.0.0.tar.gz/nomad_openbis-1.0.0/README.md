# nomad-openbis

Nomad's internal-only handler for interacting with PyBIS. Caution: do not use this package directly.

If you want to integrate openbis in nomad, please refer to the nomad [documentation](https://nomad-lab.eu/prod/v1/staging/docs/howto/manage/eln.html#integration-of-third-party-elns) on integration of third party ELNs.

### Install

You should create a virtual environment.
We recommend using Python 3.9.

```sh
python3 -m venv .pyenv
source .pyenv/bin/activate
pip install --upgrade pip
pip install -e '.[dev]'
```

### Testing

You can run automated tests with `pytest`:

```sh
pytest -svx tests
```

### Run linting

```sh
ruff check .
```

### Run auto-formatting

This is entirely optional. To add this as a check in github actions pipeline, uncomment the `ruff-formatting` step in `./github/workflows/actions.yaml`.

```sh
ruff format .
```

### License

Distributed under the terms of the `MIT`\_ license, "nomad-openbis" is free and open source software
