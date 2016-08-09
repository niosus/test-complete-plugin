# Test for clang completion
This relates to issue [niosus/EasyClangComplete#4](https://github.com/niosus/EasyClangComplete/issues/4).

Now that the parsing of tu and completions seem to be (at least partially) working, there is still a problem with reading diagnostics of the translation unit. They are illustrated in this repo.

This repo has a script that can be run either standalone or from powershell. 

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
Parsing of the translation unit works as expected with Python 3.3.5 (closest I have found to the one in sublime text) from Power Shell and outputs some debug information, number of completions and then diagnostics of errors present in the code.

Calling the script from Sublime Text causes the `plugin_host` of sublime text to stop.