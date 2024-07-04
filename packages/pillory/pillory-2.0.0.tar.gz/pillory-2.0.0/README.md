# Pillory

A linter to scrutinize how you are using mocks in Python.

If you often hear or make the comment "patch the import not the definition" or
spend a lot of time explaining or helping people debug mocks, this linter could
help you.

## Usage

Install from PyPI with pip:

```
pip install pillory
```

Pillory needs to be able to find your code and its dependencies _as if_ it were
importing it (but it doesn’t actually import it). This means you need to install
any other dependencies and set up your environment as if you were going to run
your tests. How you do this can vary between projects, but could include making
a virtualenv, `pip install -r requirements.txt`, and `pip install -e .`. If you
don’t do this pillory will find fewer errors than it should, or maybe find
no errors at all, a misleading positive result.

Run pillory on the current directory:

```
python -m pillory
```

Or give a specific files and directories:

```
python -m pillory tests/ test_example.py
```

### Rules

**PM101 patched implementation**
: You patched the implementation of a class or function instead of where it is
imported to in the module under test. e.g. "parsers.Parser" where Parser is
defined instead of "app.Parser" where it is used. This means you may not
have affected the module under test at all, or you have replaced the target in a
way which will affect other code that uses it, which is bad for test isolation
(making sure tests don't affect other tests, each test tests only what it
intends to, and doesn’t rely on how other parts of the code work). There is a
warning about not affecting the right module in the [Python Standard Library
docs][stdlibdocs], but there is an [even better article by Ned
Batchelder][nedbat] explaining how it works and the additional problems with
test isolation.

**PM102 patched is not a top level module attribute**
: You patched something like a method on a class. Because class methods can't be
imported by themselves, this means all uses of the class will be affected, not
just the module under test.

**PM103 patched builtins**
: You patched the builtins module instead of the built-in function in the module
under test. Built-ins are actually added to every module and that's where they
should be patched, to avoid similar issues to patching the implementation. There
is a CPython detail that means the builtins module may be added to the lookup of
each module, so patching the builtins module _can_ work, but it's not guaranteed
and it still has problems with test isolation.

[stdlibdocs]: https://docs.python.org/3/library/unittest.mock.html#where-to-patch
[nedbat]: https://nedbatchelder.com/blog/201908/why_your_mock_doesnt_work.html

## Known issues

* No console script entry point (pillory command), have to use with python -m.
* Does not have a non-zero exit code when errors found.
* Only tested with Python 3.10.
* No config file support.
* No comments to ignore rules.
* Not fast.
* No further explanations for the errors.
* No pretty error handling, just tracebacks.
* Will error when mocking something in the module under test, which is arguably
  "OK".
* No pre-commit integration.

## What's with the name?

I thought it was funny that mock can also mean "make fun of" as well as the
meaning of "mimic" that we use in testing. I imagined the linter cruelly calling
out how you are using mocks incorrectly. Except I couldn't call it "mock", or
"mock mocker", that would be confusing! So I picked a name with a similar
meaning, and starting with a P for that Python feeling.

## Contributing

Thank you for your interest in making a contribution.

Please talk to the maintainer before making a pull request to make sure what you
are adding is wanted.

This project uses the Apache License 2.0. You will be credited in the git
history, but for ease of maintenance copyright stays with the maintainer.

There are linters, formatters, and tests as part of the CI. You can check them
yourself locally too. To set up the linters as a pre-commit hook:

```
# Install the dev dependencies if not done already
pip install -r dev-requirements.txt
# Install the pre-commit hooks
pre-commit install
```

You can run the linters on command with:

```
pre-commit run -a
```

The unit tests are supposed to be fast tests for testing logic in a test driven
developement style. They shouldn't have mocking or accounting for side effects.
You can run them with:

```
python test_pillory.py
```

The example tests have a more complicated setup to include the file system and
command line args. Try to limit the number of example tests. The tests use
doctest to easily check the outputs. You can run them with:

```
python test_example.py -v
```

To run all the different tests and see the coverage given you can use:

```
make
```

The default make target is the coverage report in HTML format. You can look at
the file in a browser, or if you don’t want to leave the terminal but still want
a line by line coverage report, you can use [browsh][browsh] as your browser.
You can run the tests, start a HTTP server, and view the report in browsh with
this oneliner:

```
( make && cd build/htmlcov && python -m http.server 8081 &>/dev/null & browsh http://localhost:8081 ; kill $! )
```

[browsh]: https://www.brow.sh
