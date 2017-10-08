import cffi

ffi = cffi.FFI()

ffi.cdef(
    """
    void process();
    """
)

lib = ffi.dlopen("/path/to/rust/lib.so")
lib.process()
