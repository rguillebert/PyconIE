from cffi import FFI
ffibuilder = FFI()

ffibuilder.set_source("_example",
    """
    #include <sys/types.h>
    #include <pwd.h>
    """,
    libraries=[])

ffibuilder.cdef("""
    struct passwd {
        char *pw_name;
        ...;
    };
    struct passwd *getpwuid(int uid);
""")

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
