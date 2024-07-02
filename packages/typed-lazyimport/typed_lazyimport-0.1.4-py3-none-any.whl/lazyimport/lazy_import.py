from __future__ import annotations
from typing import TYPE_CHECKING, Union
from types import ModuleType
import importlib
import logging

logger = logging.getLogger('LazyImporter')


class LazyLoader:
    """Loads the library on first attribute access of the library this proxy instance is in charge of.
       This behavior allows for cheap module name aliasing, without triggering loading of the actual library.

       Caveat: doing `dir(library)` will not show the attributes of the real library until at least one
       property has been accessed. Instead you'll see the attributes of this proxy object."""

    def __init__(self, parent:Lib):
        self._parent = parent

    def __getattr__(self, attr:str):
        if isinstance(self._parent._lib, str):                              # if library has not yet been loaded
            logger.debug(f'lazy import: {self._parent._lib}')
            self._parent._lib = importlib.import_module(self._parent._lib)  # swap the lib name for the actual library
        return getattr(self._parent._lib, attr)                             # return the requested attribute value


class Lib:
    """Field descriptor that lazily imports the named library on first attribute access.

    Example use:
    ```
    # e.g. mylibs.py
    class MyLibs:
        Image = Lib('PIL.Image')  # string has the same syntax as a normal import
        mylib = Lib('mylib')
    ```

    And then use them in the code

    ```
    from mylibs import MyLibs as L
    Image = L.Image,        # analog to plain "import ..."
    Flork = L.mylib.Flork   # analog to "from ... import ... as ..." syntax
    Flork(Image.open('seagull.png'))
    ```
    """

    def __init__(self, name:str):
        assert isinstance(name, str), "Library name must be a string"       # fail fast to catch bug immediately
        self._lib:Union[str, ModuleType] = name

    def __get__(self, obj, objtype=None):
        if isinstance(self._lib, str):     # defer importing of the library initially
            return LazyLoader(self)
        return self._lib                   # when the library has already been imported, just return it.


if TYPE_CHECKING:
    import cv2  # noqa: F401
    import matplotlib  # noqa: F401
    import matplotlib.pyplot as pyplot  # noqa: F401
    import numpy  # noqa: F401
    import pandas  # noqa: F401
    import pytorch_lightning  # noqa: F401
    import sklearn  # noqa: F401
    import torch  # noqa: F401
    import torchvision  # noqa: F401


class Libs:
    """Provides lazy importing of expensive to import libraries.

       Example use:
       ```
       from lazy_import import Libs as L
       torch = L.torch           # does not trigger an import of torch
       print(torch.__version__)  # does trigger torch to be imported, and the attribute value returned
       ```

       To see when importing takes place, enable debug level logging"""

    cv2:cv2 = Lib('cv2')  # type: ignore[valid-type] # noqa: F811
    matplotlib:matplotlib = Lib('matplotlib')  # type: ignore[valid-type] # noqa: F811
    numpy:numpy = Lib('cv2')  # type: ignore[valid-type] # noqa: F811
    pandas:pandas = Lib('pandas')  # type: ignore[valid-type] # noqa: F811
    pyplot:pyplot = Lib('matplotlib.pyplot')  # type: ignore[valid-type] # noqa: F811
    pytorch_lightning:pytorch_lightning = Lib('pytorch_lightning')  # noqa: F811
    sklearn:sklearn = Lib('sklearn')  # noqa: F811
    torch:torch = Lib('torch')  # type: ignore[valid-type] # noqa: F811
    torchvision:torchvision = Lib('torchvision')  # noqa: F811
