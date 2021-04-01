# when we say "import mypackage", this file (__init__.py) runs
# when it runs, it then imports m
from . import mymoda
from . import mymodb

print('Running mypackage.__init__!')
