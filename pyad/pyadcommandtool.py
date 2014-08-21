__author__ = 'Despatcher'
import sys
import pydoc
import pyad

def output_help_to_file(filepath, request):
    f = file(filepath, 'w')
    sys.stdout = f
    pydoc.help(pyad)
    f.close()
    sys.stdout = sys.__stdout__
    return

output_help_to_file(r'pyadcommands.txt', 're')