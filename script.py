""" Usage: call with <filename>
"""
import sys
import platform
from os import path
sys.path.append(path.dirname(__file__))
from clang import cindex40_new
# from clang import cindex38
from clang import utils

cindex = cindex40_new
TU = cindex.TranslationUnit
ClangUtils = utils.ClangUtils
filename = path.abspath(path.join(path.dirname(__file__), "test.cpp"))
clang_dir = ClangUtils.find_libclang_dir("clang++")
if not cindex.Config.loaded:
    cindex.Config.set_library_path(clang_dir)
print("Clang directory = ", clang_dir)
print("Platform: ", platform.architecture())
print("Python version: ", platform.python_version())
clang_flags = ['-x', 'c++', '-std=c++11']
content = """#include <vector>
int main(int argc, char const *argv[]) {
  std::vector<int> vec;
  vec.
}"""
unsaved = [(filename, content)]
tu = TU.from_source(filename=filename, unsaved_files=unsaved, args=clang_flags)
if tu is not None:
    print("YAY! Parsed TranslationUnit")
else:
    print("something went wrong")
tu.reparse()
compl_obj = tu.codeComplete(path=filename, unsaved_files=unsaved, line=4, column=7)
print(len(compl_obj.results))

tu.reparse()
compl_obj = tu.codeComplete(path=filename, unsaved_files=unsaved, line=4, column=7)
print(len(compl_obj.results))

for diag in tu.diagnostics:
    print("here")
    print(diag)
