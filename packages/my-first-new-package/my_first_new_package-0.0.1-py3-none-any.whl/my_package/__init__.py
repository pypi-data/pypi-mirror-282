# mypackage/__init__.py

# Importing contents from module1 and module2 to make them accessible from mypackage
from .module1 import function1, Class1
from .module2 import function2, Class2

# List of symbols to be imported when using `from mypackage import *`
__all__ = ['function1', 'Class1', 'function2', 'Class2']
