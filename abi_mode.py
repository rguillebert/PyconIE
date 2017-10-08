import cffi

ffi = cffi.FFI()

ffi.cdef(
    """
    int printf(const char *format, ...);
    """
)

lib = ffi.dlopen(None)
arg = ffi.new("char[]", "World")
lib.printf("Hello %s\n", arg)
