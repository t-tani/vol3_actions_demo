try:
    from volatility.framework import interfaces, renderers
    from volatility.framework.configuration import requirements
    from volatility.plugins import yarascan
    from volatility.plugins.windows import pslist
    from volatility.plugins.windows import vaddump
    print("Success to import volatility modules")
except ImportError:
    raise ImportError("volatility modules not found.")