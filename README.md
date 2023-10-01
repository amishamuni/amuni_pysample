
## amuni_pysample

Looking to up skill and have some fun building a personal AI, I started to get more serious about Python. This repo is part rant, part jotting down the choices I made after reading articles from people who know a lot more.  

#### A sample repo for python

This template will play with and use the following:  
[requirements.txt](https://pip.pypa.io/en/stable/reference/requirements-file-format/) to specify the dependencies required.    

[pyproject.toml](https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/) to specify project metadata and build tools in a tool agnostic format.   

[Black](https://black.readthedocs.io/en/stable/) as a code formatter, [mypy](https://mypy.readthedocs.io/en/stable/) as a type checker, [Ruff](https://pypi.org/project/ruff/) as a fast linter, [pyroma](https://pypi.org/project/pyroma/) as a packaging linter.  

[Build tools](https://peps.python.org/pep-0517/#terminology-and-goals) with pip as build frontend, setuptools as build backend.

[pytest](https://docs.pytest.org/en/7.4.x/) for a test suite.  

[pre-commit](https://pre-commit.com/) as a pre-commit tool, to automate checks to be run on your code before a commit.

[Github actions](https://docs.github.com/en/actions) to automate building, testing and deploying code.  

[TestPyPI](https://test.pypi.org/) and [PyPI](https://pypi.org/) to distribute the package as per recommended process, via [twine](https://pypi.org/project/twine/)  


#### Further reading  

<https://packaging.python.org/en/latest/flow/>  
<https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/>  
<https://docs.python.org/3/tutorial/index.html>  
<https://stackoverflow.com/questions/60719286/actions-for-creating-venv-in-python-and-clone-a-git-repo>  
<https://setuptools.pypa.io/en/latest/userguide/development_mode.html>  
<https://pip.pypa.io/en/latest/topics/local-project-installs/>  

#### The Python diaries

Everything is a decision, and there is no single recommendation that would cater to the vast majority of beginners, guiding them with best practices. What I had done in the past was simple scripts and tools, and I wanted to learn how a bigger python project should be structured, with a view to being able to easily build and package. And this to me looks harder than it should be!

![The ecosystem from xkcd](https://m.xkcd.com/1987/)
