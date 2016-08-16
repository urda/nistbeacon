# Contributing to nistbeacon

:+1::tada: First off, thanks for taking the time to contribute! :tada::+1:

#### Table Of Contents

- [What should I know before I get started?](#what-should-i-know-before-i-get-started)
  - [Configuring Your Environment](#configuring-your-environment)
- [How Can I Contribute?](#how-can-i-contribute)
  - [Reporting Bugs](#reporting-bugs)
  
## What should I know before I get started?

You should become familiar with the following:

- [Python 3](https://docs.python.org/3/)
- The famous [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/)
- NIST Randomness Beacon Documentation:
  - [NIST Randomness Beacon Homepage](http://www.nist.gov/itl/csd/ct/nist_beacon.cfm)
  - [NIST Randomness Beacon API Overview](https://beacon.nist.gov/home)
  - [NIST Randomness Beacon API XSD](https://beacon.nist.gov/record/0.1/beacon-0.1.0.xsd)

### Configuring Your Environment

Setting up your local environment can be a tough with some projects. This project aims
to have a simple and quick environment setup process.

You should already have configured a local `virtualenv` with `python 3` as the interpreter.
Once you have your local `virtualenv` ready to go, simply install the full dev tool package using `pip`:

```bash
pip install -r requirements-dev.txt
```

If you have have problems installing `pycrypto`, you may need `python3-dev` or a similar library on your
machine. For Ubuntu and other linux systems `apt-get install python3-dev` will usually set you straight.
Once you have it installed try running your `pip install` command again. **If this still does not work**
please add a note in this [GitHub Issue](https://github.com/urda/nistbeacon/issues/4) and then open
a new issue!

If you would like to verify your local environment, you can try testing the project with:

```bash
make
```

:heavy_exclamation_mark: **Important Note!** You will need an internet connection to
execute the full test suite.

Which will run the same testing steps that [Travis CI](https://travis-ci.org/urda/nistbeacon)
will run. You can also just run `make test` if you would like to just run the python tests.

## How Can I Contribute?

### Reporting Bugs

To err is human, and bugs do happen in projects! We might see bugs from missing documentation,
installation problems, and of course bugs in the actual project itself. Reporting these bugs
will make it easier for future users to enjoy `nistbeacon`. Please feel free to open a bug
report when you run across problems.

#### Template For Submitting Bug Reports

```markdown
[Short description of problem here]

**Reproduction Steps:**

1. [First Step]
2. [Second Step]
3. [Other Steps...]

**Expected behavior:**

[Describe expected behavior here]

**Observed behavior:**

[Describe observed behavior here]

**nistbeacon version:** [Enter version here]
**OS and version:** [Enter OS name and version here]

**Installed packages:**

[List your `pip freeze` output here]

```


