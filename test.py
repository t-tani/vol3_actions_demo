try:
    from volatility.framework import interfaces, renderers
    from volatility.framework.configuration import requirements
    from volatility.plugins import yarascan
    print("interfaces, renderers, requirements -> ok!")
except ImportError:
    print("Failed 0x01")
try:
    from volatility.plugins.windows import pslist
    from volatility.plugins.windows import vaddump
    print("Success to import volatility modules")
except ImportError:
    print("Failed 0x02")