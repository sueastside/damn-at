import os
import sys
import subprocess as sp

p = sp.Popen(["TempoDetector", "single", "coldplay.m4a"],stdout=sp.PIPE)
output = p.communicate()[0]
print output.split()[1]