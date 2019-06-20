# Test for clang completion
This relates to issue [niosus/EasyClangComplete#230](https://github.com/niosus/EasyClangComplete/issues/230).

Using libclang with clang 4.0 crashes Sublime Text when trying to complete code interactively.
asdasda
This repo has a script that can be run either from Sublime Text or from powershell.

# Install it to sublime text 3
- clone it into `C:\Users\<user>\AppData\Roaming\Sublime Text 3\Packages`
- open Sublime Text 3
- check console for output

# Run it from command line
- navigate to the folder where you have cloned it
- run `script.py` with your version of python:
  + Power Shell: `PS C:\Users\<user>\AppData\Roaming\Sublime Text 3\Packages\test-complete-plugin> python.exe .\script.py`
  + terminal: `python <path_to_instalation>/sctipt.py`

# Current state
The `script.py` never crashes. It doesn't matter if it is run from sublime text or from powershell. The strange thing is that when we try to manually complete the `test.cpp` provided with this plugin this crashes plugin host.

Outputs:
## Test plugin run from Sublime Text on start ##
```
PARSED TU:  <ctypes.wintypes.LP_c_void_p object at 0x0000014E6FAFB448>
[('C:\\Users\\igor\\AppData\\Roaming\\Sublime Text 3\\Packages\\test-complete-plugin\\test.cpp', '#include <vector>\nint main(int argc, char const *argv[]) {\n  std::vector<int> vec;\n  vec.\n}')]
<CDLL 'C:\Program Files\LLVM\bin\libclang.dll', handle 7fff92f20000 at 14e6faccf98>
path b'C:\\Users\\igor\\AppData\\Roaming\\Sublime Text 3\\Packages\\test-complete-plugin\\test.cpp'
line 4
column 7
len unsaved 1
options 0
<clang.cindex40_new.LP_CCRStructure object at 0x0000014E6FAFBCC8>
```
## Manual trigger of completion from Sublime Text using EasyClangComplete ##
```
PARSED TU: <ctypes.wintypes.LP_c_void_p object at 0x0000014E7000B5C8>
[('C:\\Users\\igor\\AppData\\Roaming\\Sublime Text 3\\Packages\\test-complete-plugin\\test.cpp', '#include <vector>\nint main(int argc, char const *argv[]) {\n  std::vector<int> vec;\n  vec.\n}')]
<CDLL 'C:\Program Files\LLVM\bin\libclang.dll', handle 7fff92f20000 at 14e6fc922e8>
path b'C:\\Users\\igor\\AppData\\Roaming\\Sublime Text 3\\Packages\\test-complete-plugin\\test.cpp'
line 4
column 7
len unsaved 1
options 0
error: plugin_host has exited unexpectedly, plugin functionality won't be available until Sublime Text has been restarted
``` 
