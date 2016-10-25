"__author__ = 'Martin Fiser'"
"__credits__ = 'Keboola 2016, Twitter: @VFisa'"


import os
import sys
import pip
import requests
import json
import traceback
from keboola import docker


## Environment setup
abspath = os.path.abspath(__file__)
script_path = os.path.dirname(abspath)
os.chdir(script_path)
#print script_path

## initialize application
cfg = docker.Config('/data/')
params = cfg.get_parameters()

## access the supplied values
# storage_id = cfg.get_parameters()["storage_id"]
# project_id = cfg.get_parameters()["project_id"]


try:
    pip.main(['install', '--disable-pip-version-check', '--no-cache-dir', 'networkx'])
    import networkx as nx
    print ("Test sucess!")
except ValueError as err:
    ## Python 2 code
    print >>sys.stderr, str(err)
    ## Python 3 code:
    #print(err, file=sys.stderr)
    sys.exit(1)
except Exception as err:
    ## Python 2 code
    print >>sys.stderr, str(err)
    traceback.print_exc()
    ## Python 3 code:
    #print(err, file=sys.stderr)
    #traceback.print_exc(file=sys.stderr)
    sys.exit(2)
