# py_output_compare

a python package that create to help compare output of 2 python script, I apply this to help grading student code compare to teacher

# note to myself

## to make it auto login to twine

1. create `pip.ini` at `%APPDATA%\pip\pip.ini`, then add following content

> content of `pip.ini`

```ini
index = https://%TWINE_USERNAME%:%TWINE_PASSWORD%@pypi.example.com/pypi
index-url = https://%TWINE_USERNAME%:%TWINE_PASSWORD%@pypi.example.com/simple
cert = C:\Program Files\Python\Python39\Lib\site-packages\certifi\cacert.pem
```

use `pip config list` to see setting

2. run `.cmd` file with this content

```
setx TWINE_USERNAME your_username
setx TWINE_PASSWORD your_password
```
