import os
import sys
import subprocess as sp

p = sp.Popen(["TempoDetector", "single", sys.argv[-1]],stdout=sp.PIPE)
output = p.communicate()[0]
print output.split()[1]