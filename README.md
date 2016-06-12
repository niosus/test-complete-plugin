# Test for clang completion
This relates to issue niosus/EasyClangComplete#4.

I need to find a way to run `libclang` on Windows with Sublime Text 3.

This repo has one script in it: `script.py`. It tries to construct a translation unit from a `test.cpp` file and then tries to reparse it and complete it.

# Current state
Works from Powershell but not from within Sublime Text 3.
