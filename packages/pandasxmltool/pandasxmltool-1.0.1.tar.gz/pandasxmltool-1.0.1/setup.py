from setuptools import setup, find_packages
import os


def read(fname):
    """Utility function to get README.rst into long_description.
    ``long_description`` is what ends up on the PyPI front page.
    """
    with open(os.path.join(os.path.dirname(__file__),fname), encoding="utf8") as f:
        contents = f.read()

    return contents


VERSION = '1.0.1'
DESCRIPTION = 'Pandas and XML Measurement Tool'
LONG_DESCRIPTION = read("README.md")

# Setting up
setup(
    # the name must match the folder name
    name="pandasxmltool",
    version=VERSION,
    license='BSD',
    author="ROInsight",
    author_email="<roinsight.com@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        # add any additional packages
    ],
    url="",
    keywords=['python', 'audit'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Interpreters",
        "Topic :: Software Development :: Version Control :: Git",
    ]
)


