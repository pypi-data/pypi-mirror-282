import setuptools
# used by python -m build
# python -m build needs pyproject.toml or setup.py
setuptools.setup(
     # TODO: Please update the name
     name='recruitment-employer-monster-com-indeed-com-vacancy-scraper-local', # https://pypi.org/project/recruitment-employer-monster-com-indeed-com-vacancy-scraper-local restpi?
     version='0.0.4',
     author="Circles",
     author_email="info@circles.life",
     description="PyPI Package for Circles Local RestAPI recruitment Python",
     long_description="This is a package for sharing common RestAPI recruitment function used in different repositories",
     long_description_content_type="text/markdown",
     url="https://github.com/javatechy/dokr",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: Other/Proprietary License",
         "Operating System :: OS Independent",
     ],
 )
