# code-15062022-patrickmotylinski - Vamstar Take Home Test

This repository contains my solution to the Vamstar take-home test.

The code is arranged as follows:  
- `<proj. root>/src` : contains source code (class that addresses the questions 1 and 2)
- `<proj. root>/tests` : contains the unit tests
- `<proj. root>/data` : contains the supplied data in the form of a `.json` file

Please note: in Question 2: we count everyone who is overweight or more (i.e. obese etc.) as being overweight

## Installation
The code has not been registered on PyPI, thus only local installations are possible. This code was developed using python v. 3.9.7

### Build wheel
'~> python setup.py bdist_wheel'  
  
### Install wheel
The corresponding wheel will be located in the `dist` folder.  
`~> pip install <dir containing wheel>/<wheel name>.whl`

## Disclaimer
Please note: I have been struggling with importing this module in ipython. Using 'pip freeze' I can see the package is installed, but I cannot import it.

For what it is worth, the questions in the exercise can be solved/answered by running the '<proj. root>/main.py' script.
