try:
    from volatility.framework import interfaces, renderers
    from volatility.framework.configuration import requirements
    from volatility.plugins import windows
    from volatility.plugins import yarascan
    from volatility.plugins.windows import pslist

    print("interfaces, renderers, requirements -> ok!")
except ImportError:
    print("Failed 0x01")
try:
    from volatility.plugins.windows import vadinfo
    print("Success to import volatility modules")
except ImportError:
    print("Failed 0x02")