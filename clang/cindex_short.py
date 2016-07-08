from ctypes import *

c_object_p = POINTER(c_void_p)


class ClangObject(object):
    def __init__(self, obj):
        assert isinstance(obj, c_object_p) and obj
        self.obj = self._as_parameter_ = obj

    def from_param(self):
        return self._as_parameter_


class CachedProperty(object):
    def __init__(self, wrapped):
        self.wrapped = wrapped
        try:
            self.__doc__ = wrapped.__doc__
        except:
            pass

    def __get__(self, instance, instance_type=None):
        if instance is None:
            return self

        value = self.wrapped(instance)
        setattr(instance, self.wrapped.__name__, value)

        return value


class Index(ClangObject):
    @staticmethod
    def create(excludeDecls=False):
        return Index(conf.lib.clang_createIndex(excludeDecls, 0))

    def __del__(self):
        conf.lib.clang_disposeIndex(self)


class TranslationUnit(ClangObject):
    @classmethod
    def from_source(cls, filename, args=None, unsaved_files=None, options=0,
                    index=None):
        if args is None:
            args = []

        if unsaved_files is None:
            unsaved_files = []

        if index is None:
            index = Index.create()

        args_array = None
        if len(args) > 0:
            args_array = (c_char_p * len(args))()
            for i, v in enumerate(args):
                args_array[i] = v.encode('utf-8')

        unsaved_array = None

        if filename is not None:
            filename = filename.encode('utf-8')

        ptr = conf.lib.clang_parseTranslationUnit(index,
            filename, args_array,
            len(args), unsaved_array,
            len(unsaved_files), options)

        if not ptr:
            raise Exception("Error parsing translation unit.")

        return cls(ptr, index=index)

    def __init__(self, ptr, index):
        assert isinstance(index, Index)
        ### Patch from: http://reviews.llvm.org/D17226
        self.index = index
        ClangObject.__init__(self, ptr)


def register_function(lib, item, ignore_errors):
    # A function may not exist, if these bindings are used with an older or
    # incompatible version of libclang.so.
    try:
        func = getattr(lib, item[0])
    except AttributeError as e:
        msg = str(e) + ". Please ensure that your python bindings are "\
                       "compatible with your libclang.so version."
        if ignore_errors:
            return
        raise Exception(msg)

    if len(item) >= 2:
        func.argtypes = item[1]

    if len(item) >= 3:
        func.restype = item[2]

    if len(item) == 4:
        func.errcheck = item[3]


def register_functions(lib, ignore_errors):
    def register(item):
        return register_function(lib, item, ignore_errors)

    for function in functionList:
        register(function)


class Config:
    library_path = None
    library_file = None
    compatibility_check = True
    loaded = False

    @staticmethod
    def set_library_path(path):
        """Set the path in which to search for libclang"""
        if Config.loaded:
            raise Exception("library path must be set before before using "
                            "any other functionalities in libclang.")

        Config.library_path = path

    @staticmethod
    def set_library_file(filename):
        """Set the exact location of libclang"""
        if Config.loaded:
            raise Exception("library file must be set before before using "
                            "any other functionalities in libclang.")

        Config.library_file = filename

    @CachedProperty
    def lib(self):
        lib = self.get_cindex_library()
        register_functions(lib, not Config.compatibility_check)
        Config.loaded = True
        return lib

    def get_filename(self):
        if Config.library_file:
            return Config.library_file

        from .utils import ClangUtils
        from os import path
        filename = ClangUtils.libclang_name

        if Config.library_path:
            filename = path.join(Config.library_path, filename)

        return filename

    def get_cindex_library(self):
        try:
            print("filename = ", self.get_filename())
            library = cdll.LoadLibrary(self.get_filename())
        except OSError as e:
            msg = str(e) + ". To provide a path to libclang use " \
                           "Config.set_library_path() or " \
                           "Config.set_library_file()."
            raise Exception(msg)

        return library

conf = Config()


functionList = [
    ("clang_createIndex",
        [c_int, c_int],
        c_object_p),
    ("clang_parseTranslationUnit",
       [Index, c_char_p, c_void_p, c_int, c_void_p, c_int, c_int],
       c_object_p)
]
