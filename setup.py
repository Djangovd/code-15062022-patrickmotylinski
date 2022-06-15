from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'BMI take-home test'
LONG_DESCRIPTION = 'BMI Take-home test submission by Patrick Motylinski'

# Setting up
setup(
    name="vamstartakehometest",
    version=VERSION,
    author="Patrick Motylinski",
    author_email="<patrick.motylinski@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    url="https://github.com/Djangovd/code-15062022-patrickmotylinski",
    license='MIT',
    python_requires='>=3.8',
    install_requires=[],
    packages=find_packages()
)
