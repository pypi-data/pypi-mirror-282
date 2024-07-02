import pathlib
from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Semantic Caching with Python'
LONG_DESCRIPTION = pathlib.Path("README.md").read_text()
LONG_DESCRIPTION_CONTENT_TYPE = "text/markdown"
project_urls = {'Documentation': 'https://github.com/ErayEroglu/python-semantic-caching'}
license = 'MIT'
setup(
    name="py_semantic_caching",
    version=VERSION,
    author="Eray Eroğlu",
    author_email="erayeroglu07@email.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,  # This line is added to specify the content type
    packages=find_packages(),
    install_requires=[],
    
    keywords=['python', 'first package'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
    ]
)
