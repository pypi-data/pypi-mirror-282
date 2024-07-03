# PrivateCode

[![Downloads](https://img.shields.io/pepy/dt/PrivateCode)](https://pypi.org/project/PrivateCode/)
[![Version](https://img.shields.io/pypi/v/PrivateCode)](https://pypi.org/project/PrivateCode/)
[![Python Version](https://img.shields.io/pypi/pyversions/PrivateCode)](https://pypi.org/project/PrivateCode/)

PrivateCode is a Python library that provides a decorator to make a function, method, or class private. 
This allows the function, method, or class to be accessed only from its own module and raises an exception if called from another module.
**WARNING** : Functions are not private at the memory level, but only at the call level.

## Set up
----
### Install

~~~python
pip install PrivateCode
~~~

### Upgrade
~~~~python
pip install --upgrade PrivateCode
~~~~

## Support

If you want to contact me for questions, bugs, or problems or other: lixnew2@gmail.com

## Python version

PrivateCode was written for Python 3.

## Decorator

### Make a function, method, or class private
~~~python
@private
~~~

## Decorator Documentation

### `private`
A decorator that makes a function, method, or class private, allowing it to be called only from its own module.

#### Arguments:
- `target`: The function, method, or class to be decorated.

#### Returns:
- The decorated function, method, or class.

#### Raises:
- `ValueError`: If the decorated function, method, or class is called from a different module.

#### Example:
~~~python
@private
def my_private_function():
    # This function can only be called from its own module.
    pass

class MyClass:
    @private
    def my_private_method(self):
        # This method can only be called from its own module.
        pass

@private
class MyPrivateClass:
    # This class can only be instantiated from its own module.
    pass
~~~