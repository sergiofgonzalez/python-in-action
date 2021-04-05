# 01 &mdash; Python basics
> TBD

## Introduction
We will be using Python 3. The easiest way to start for Python beginners is to download and install Anaconda from https://anaconda.com.

The Anaconda packages will be installed under `home/<username>/anaconda3`.

Once installed, you can do:

```bash
$ python
Python 3.8.3 (default, Jul  2 2020, 16:21:59)
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Typing *CTRL+D* or `exit()` will let you exit the REPL interactive session.

The *REPL* will also allow you to enter multi-line inputs, like the canonical hello world:

```python
>>> def sayHelloWorld():
...   print("Hello, world!")
...
>>> sayHelloWorld()
Hello, world!
>>>
```

Or simple mathematical functions:

```python
>>> def f(x):
...   return x * x
...
>>> f(5)
25
>>>
```

## Creating and Running Script Files
Installed Python extension in VSCode typying *CTRL+P* and then: `ext install ms-python.python`. Then I had to click on the status line at the bottom to switch from the default Python environment to the Python *conda* distribution.

Also, wanted to remove the `"(base)"` from the prompt, so I did: `conda config --set auto_activate_base false`

## Running Jupyter Notebooks
A Jupyter Notebook is a graphical interface for coding in Python.

To open the Jupyter Notebook interface type `python -m notebook`.


## Style Guide

This section summarizes the official style guide for Python code as described in [PEP 8 &mdash; Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

The principle for style guide is to give a series of simple rules that should be used to improve the readability of the code and make it consistent across libraries and projects.

It is also important to understand that this style guide should be taken as a pragmatic document: under certain circumstances it should be OK to break the rules for the sake of simplicity, or even readability.

Configuration:
+ Enable PyLint (very permissive on vscode)
+ Enable Pycodestyle

Google style guide:
https://google.github.io/styleguide/pyguide.html

Enable ide, then run in command line in CI/CD

## Structure of the projects

https://docs.python-guide.org/writing/structure/

Requirements file:

files contain a list of items to be installed using pip install like:

```
python -m pip install -r requirements.txt
```

It is just a list of pip install arguments placed in a file. You should not rely in any particular order.

pip freeze can be used to ensure repeatable installations. 3rd party libraries should use exact versions to ensure repeatable builds, as we cannot ensure that 3rd party modules follow semver.

For our own modules, we will use semver.

## Docker guidelines

Release cycle is maintained in https://devguide.python.org/#status-of-python-branches

Stable version seems to be 3.8, in bugfix mode. It will be maintained until Oct 2024 and will accept bugfixes and security fixes over the stable version.

Docker runtimes should be created from there.

We can create our own base image to control runtime, procedures, etc. Therefore, crawlers should use FROM [our own image].

3.9 is also accepted as an stable version.

Secrets management
: access keys, connection strings should be externalized and handled as secrets

This is a great guide
https://www.docker.com/blog/containerized-python-development-part-1/

Use multi-stage builds for prod, not needed for dev.





## FAQs

### 1. When I type `python --version` I get 2.x.y instead of 3.x.y, how do I fix this?
Type `conda activate` to activate the Python version from the Conda distribution

### 2. How do update the Anaconda distribution?
Type `conda update conda`

## Useful References

+ [Anaconda Individual Distribution User's Guide](https://conda.io/projects/conda/en/latest/user-guide/index.html)

