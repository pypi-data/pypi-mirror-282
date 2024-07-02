# cvss-converter

A python program to convert older cvss versions to more modern ones.

# How to administrate Pypi

## Pre-requisites:

You should have the .pypirc file installed at the ~/ (home) directory

```
[distutils]
index-servers =
    poc-wheel-dev-standard
    testpypi
    pypi

[poc-wheel-dev-standard]
repository: https://asia-southeast1-python.pkg.dev/carto-poc/poc-wheel-dev-standard/
username: _json_key_base64
password: ewogICJjbGllbnRfZW1haWwiOiAiZ2l0aHViLXN...[redacted]

[testpypi]
repository: https://test.pypi.org/legacy/
username: __token__
password: pypi-AgENdGV...[redacted]

[pypi]
repository: https://upload.pypi.org/legacy/
username: __token__
password: pypi-AgEIcHl...[redacted]
```

\*Please note that `pypi_setup_and_upload.sh` requires a manual copy and paste at the last line.
