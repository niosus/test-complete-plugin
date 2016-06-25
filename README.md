# Test for clang completion
This relates to issue [niosus/EasyClangComplete#4](https://github.com/niosus/EasyClangComplete/issues/4).

I need to find a way to run `libclang` on Windows with Sublime Text 3.

This repo has one script in it: `script.py`. It tries to construct a translation unit from a `test.cpp` file, then tries to reparse it and complete it.

# Current state
Completion works as expected with Python 3.3.5 (closest I have found to the one in sublime text) from Power Shell but from the sublime text causes this:
```
Traceback (most recent call last):
  File "C:\Program Files\Sublime Text 3\sublime_plugin.py", line 78, in reload_plugin
    m = importlib.import_module(modulename)
  File "./python3.3/importlib/__init__.py", line 90, in import_module
  File "<frozen importlib._bootstrap>", line 1584, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1565, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1532, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 584, in _check_name_wrapper
  File "<frozen importlib._bootstrap>", line 1022, in load_module
  File "<frozen importlib._bootstrap>", line 1003, in load_module
  File "<frozen importlib._bootstrap>", line 560, in module_for_loader_wrapper
  File "<frozen importlib._bootstrap>", line 868, in _load_module
  File "<frozen importlib._bootstrap>", line 313, in _call_with_frames_removed
  File "C:\Users\igor\AppData\Roaming\Sublime Text 3\Packages\test_clang\script.py", line 21, in <module>
    tu = TU.from_source(filename=filename)
  File "C:\Users\igor\AppData\Roaming\Sublime Text 3\Packages\test_clang\clang\cindex38.py", line 2372, in from_source
    raise TranslationUnitLoadError("Error parsing translation unit.")
clang.cindex38.TranslationUnitLoadError: Error parsing translation unit.
```

# Install it to sublime text 3
- clone it into `C:\Users\<user>\AppData\Roaming\Sublime Text 3\Packages`
- open Sublime Text 3
- check console for output

# Run it from Power shell
- navigate to the folder where you have cloned it
- run `script.py` with your version of python
