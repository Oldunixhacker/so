# Stack Overflow Command Line
This is the Stack Overflow CLI, which Stack Overflow refused to write.
I had to write it because I'm a developer, but `stackoverflow.com` is going
weird and I almost have no way to do SO-related stuff from my CLI.

For more info, see [the Stack Apps listing](https://stackapps.com/questions/9375/placeholder-stackoverflow-cli)
or the [docs](https://tylerms887.github.io/so).
## Features
* Use a small simple editor (`micro`)
* Works properly in scripts
* Runs on any major operating system (Windows, macOS, Un\*x)
## Usage
### Log in
[Authenticate](https://api.stackexchange.com/docs/authentication) your Stack Overflow account with OAuth 2.0 to use SE API v2:
```shell
$ so login
# Logging in...
# Review your browser
# Logged in as (username)!
```
### Ask a question
Ask a new question and it will appear on Stack Overflow:
```shell
$ so question ask
# (?) Title (15+ chars): I got syntaxerror
# (!) Many questions with a similar title received bad feedback (e.g. downvotes,
#     comments). Please update your title to be more descriptive.
# (?) Title (15+ chars): SyntaxError: '(' was never closed
# >>> Checking for similar questions...
# 
# (?) Body [Press enter to launch micro]
# (?) Tags (up to 5, at least 1 required): [python] [python-3.x] [brackets]
# (i) Asked question successfully.
```
If `micro` was not found, this throws an error. Install the `micro` editor
if you do not have it, as this app depends on it. To avoid this, use
the `--nano` option.
### More info
Learn how to use `so`:
```shell
# Usage: so command [subcommand] [options]
#
# Options:
#     -v, --version       Print the version and exit. Same as "so version".
#     -h, --help, -?      Print this message and exit. Same as "so help".
#     --nano              If nano was found, use it for editing text.
#     --no-color          Do not display any colors.
#     --meta              Target MSO (Meta Stack Overflow) instead of
#                         Stack Overflow.
#
# Commands: (indented commands are subcommands of their intended command)
#     question            Manage questions
#       ask               Ask a question
#       review-edit       Review edits [Minimum reputation: 2k]
#     answer              Manage answers
#     help                Show this message
#
# This program is a work-in-progress. Please fork the project on github:
# https://github.com/TylerMS887/so
```
## Python 3 Support
Python 3.6+ is supported. The binaries do not require Python at all, but running
or compiling the scripts requires Python. Older versions are not supported (for one reason:
F-strings).
## Python 2 Support
Python 2.x is not supported. When compiling, make sure you have Python 3.
If you have both, remember to execute Python 3 instead of Python 2.
