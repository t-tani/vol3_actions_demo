import os
import sys
path=[path for path in sys.path if "site-packages" in path][0]
vollib=[path for path in os.listdir(path) if "volatility" in path][0]
sys.path.append(path+"/"+vollib)
print(os.pathdir(path+"/"+vollib))
cmd = "::set-env name=PYTHONPATH:"+":".join(sys.path)
print(cmd)