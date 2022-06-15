import os

# Names
INPUTS = "input"
TEST_INPUTS = "test_input"
SRC = "src"
ENV = "env"
DATA = "data"
TESTDATA = "test_data"
TESTS = "tests"

datafile_suffix = "json"
datafile_cache_suffix = "pkl"

# Directories
ENV_DIR = os.path.dirname( __file__ )
PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
SRC_DIR = os.path.join(PROJECT_DIR, SRC)
ENV_DIR = os.path.join(PROJECT_DIR, ENV)
DATA_DIR = os.path.join(PROJECT_DIR, DATA)

# Files
DATAFILE = os.path.join(DATA_DIR, DATA + "." + datafile_suffix)
TESTDATAFILE = os.path.join(DATA_DIR, TESTDATA + "." + datafile_suffix)
