from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

# with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
#     long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Render JS for dynamic Websites for Web Scraping'
LONG_DESCRIPTION = 'A package that allows to Render JS for dynamic Websites for Web Scraping'

# Setting up
setup(
    name="requestsRenderJs",
    version=VERSION,
    author="Ghulam Mustafa",
    author_email="ghulammustafapy@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    # long_description=long_description,
    packages=find_packages(),
    install_requires=['selenium', 'webdriver-manager'],
    keywords=['python', 'web scraping', 'requests_HTML', 'python render js', 'selenium', 'webdriver'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)