"""
PrivateCode is a Python library that provides a decorator to make a function, method, or class private.
This allows the function, method, or class to be accessed only from its own module and raises an exception if called from another module.
Functions are not private at the memory level, but only at the call level.

Example:
    @private
    def my_private_function():
        # This function can only be called from its own module.
        pass
        
"""

__copyright__  = """
MIT License 

Copyright (c) 2024 LixNew; lixnew2@gmail.com

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

__version__ = '1.0.0'
__title__ = 'PrivateCode'
__description__ = "PrivateCode is a Python library that provides a decorator to make a function, method, or class private."
__autor__ = 'LixNew'
__twitter__ = '@LixNew2'
__url__ = "https://github.com/LixNew2/PyCrypTools"

#Import
import inspect

#Decorator
def private(target):
    """
    A decorator that makes a function, method, or class private, allowing it to be called only from its own module.

    Args:
        target: The function, method, or class to be decorated.

    Returns:
        The decorated function, method, or class.

    Raises:
        ValueError: If the decorated function, method, or class is called from a different module.

    Example:
        @private
        def my_private_function():
            # This function can only be called from its own module.
            pass
    """
    
    def wrapper(*args, **kwargs):
        caller_module = inspect.currentframe().f_back.f_globals['__name__'] # Get the name of the module that called the decorated function.
        decorated_module = inspect.getmodule(target).__name__ # Get the name of the module that contains the decorated function.
        
        if caller_module == decorated_module:
            return target(*args, **kwargs) # Call the decorated function.
        else:
            if 'self' in inspect.signature(target).parameters: # Check if the decorated function is a method.
                raise ValueError(f"The method '{target.__name__}' is private and can only be called from its own module.")
            elif inspect.isfunction(target): # Check if the decorated function is a function. 
                raise ValueError(f"The function '{target.__name__}' is private and can only be called from its own module.")
            elif inspect.isclass(target): # Check if the decorated function is a class.
                raise ValueError(f"The class '{target.__name__}' is private and can only be called from its own module.")

    return wrapper