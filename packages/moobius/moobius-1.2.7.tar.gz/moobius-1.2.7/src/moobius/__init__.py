# __init__.py

from moobius.core.sdk import Moobius
from moobius.core.wand import MoobiusWand
from moobius.database.storage import MoobiusStorage
#from moobius import types as Moobius

import sys
if len(sys.argv) > 1: # Quickstart option.
    from . import quickstart
    quickstart.save_starter_ccs()
