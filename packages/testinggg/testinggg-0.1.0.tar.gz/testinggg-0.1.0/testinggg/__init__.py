# __init__.py

# Import the C++ extension module (libadd_module.so on Linux or pybindstuff.pyd on Windows)
# from .pybindstuff import add

# import pybindstuff

# from .libadd_module import add

# Define a Python function that wraps around the C++ function
# def add(a, b):
#     """
#     Adds two numbers using the C++ function exposed through pybind11.

#     Parameters:
#     - a (int): First operand.
#     - b (int): Second operand.

#     Returns:
#     - int: Sum of a and b.
#     """
#     return pybindstuff.add(a, b)

# add_modpy/__init__.py

# import importlib.util
# import sys
# import os

# # Path to the directory containing this __init__.py file
# module_path = os.path.dirname(__file__)

# # Load the shared library dynamically
# spec = importlib.util.spec_from_file_location("libadd_module", os.path.join(module_path, "libadd_module.so"))
# libadd_module = importlib.util.module_from_spec(spec)
# sys.modules["libadd_module"] = libadd_module
# spec.loader.exec_module(libadd_module)

# # Import the function directly
# from libadd_module import add

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__),'.'))

from pybindstuff import fibonacci_cpp, add_py, MyClass
