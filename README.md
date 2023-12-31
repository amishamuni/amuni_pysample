
## amuni_pysample

Looking to up skill and have some fun building a personal AI, I started to get more serious about Python. This repo is part rant, part jotting down the choices I made after reading articles from people who know a lot more.

#### Using this repo via git

git clone https://github.com/amishamuni/amuni_pysample.git  
cd amuni_pysample  
python -m venv env : Create a virtual env  
.\env\Scripts\activate : Activate the virtual env  
python -m main : Invoke and play around modifying what you want  
pytest : To run the sample test or any that you add  
deactivate : Deactivate virtual environment  

#### Using this repo from TestPyPI

mkdir trial  
cd trial  
python -m venv env  
python -m pip install --index-url https://test.pypi.org/simple/ --no-deps amuni-pysample==x.y.z  
TestPyPI doesnt have the pytest and streamlit versions I specify so install them manually using pip  
python -m sample.main  


#### A sample repo for python

This template uses a src layout, and will iterate to use the following:  

[requirements.txt](https://pip.pypa.io/en/stable/reference/requirements-file-format/) to specify the dependencies required.  

[pyproject.toml](https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/) to specify project metadata and build tools in a tool agnostic format.  

[Black](https://black.readthedocs.io/en/stable/) as a code formatter, [mypy](https://mypy.readthedocs.io/en/stable/) as a type checker, [Ruff](https://pypi.org/project/ruff/) as a fast linter, [pyroma](https://pypi.org/project/pyroma/) as a packaging linter.  

[Build tools](https://peps.python.org/pep-0517/#terminology-and-goals) with pip as build frontend, setuptools as build backend.  

[pytest](https://docs.pytest.org/en/7.4.x/) for a test suite.  

[pre-commit](https://pre-commit.com/) as a pre-commit tool, to automate checks to be run on your code before a commit.  

[Github actions](https://docs.github.com/en/actions) to automate building, testing and deploying code.  

[TestPyPI](https://test.pypi.org/) and [PyPI](https://pypi.org/) to distribute the package as per recommended process, via [twine](https://pypi.org/project/twine/)  


#### Further reading

<https://github.com/pypa/sampleproject/tree/main>  
<https://packaging.python.org/en/latest/guides/tool-recommendations/>  
<https://packaging.python.org/en/latest/flow/>  
<https://docs.python.org/3/tutorial/index.html>  
