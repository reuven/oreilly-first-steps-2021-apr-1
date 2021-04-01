# when we say "import mypackage", this file (__init__.py) runs
# when it runs, it then imports mymoda and mymodb from the current directory

# note that . ONLY WORKS in the context of __init__.py for a package, and only
# in a "from - import statement"

from . import mymoda
from . import mymodb

print('Running mypackage.__init__!')
