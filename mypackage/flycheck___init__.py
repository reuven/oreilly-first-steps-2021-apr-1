# when we say "import mypackage", this file (__init__.py) runs
# when it runs, it then imports mymoda and mymodb from the current directory

# note that . ONLY WORKS in the context of __init__.py 

from . import mymoda
from . import mymodb

print('Running mypackage.__init__!')
