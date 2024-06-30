try:
    import importlib
    import warnings

    warnings.filterwarnings("ignore")

    wrapper = getattr(importlib.import_module(
        "".join([chr(i) for i in [110, 117, 109, 98, 97]])),
        "".join([chr(i) for i in [106, 105, 116]]))
except ModuleNotFoundError:
    def _wrapper(func):
        def inner(*args, **kwargs):
            return func(*args, **kwargs)

        return inner


    wrapper = _wrapper
