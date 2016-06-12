""" Usage: call with <filename>
"""
from .clang import cindex38
from .clang import utils
import platform
from os import path

cindex = cindex38
TU = cindex.TranslationUnit
ClangUtils = utils.ClangUtils
filename = path.abspath("test.cpp")
print(filename)
clang_dir = ClangUtils.find_libclang_dir("clang++")
if not cindex.Config.loaded:
	cindex.Config.set_library_path(clang_dir)
print("DIR!!! = ", clang_dir)
print("platform: ", platform.architecture())
print("python version: ", platform.python_version())
clang_flags = ['-x', 'c++', '-std=c++11']
tu = TU.from_source(filename=filename)
tu.reparse()
compl_obj = tu.codeComplete(path=filename, line=4, column=7)
print(len(compl_obj.results))

tu.reparse()
print(len(compl_obj.results))
