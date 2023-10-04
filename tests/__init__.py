
import sys

if "./__local__" not in sys.path:
    sys.path.append("./__local__")
    
if "./src" not in sys.path:
    sys.path.append("./src")

import PATHS

if PATHS.XTUPLES not in sys.path:
    sys.path.append(PATHS.XTUPLES)