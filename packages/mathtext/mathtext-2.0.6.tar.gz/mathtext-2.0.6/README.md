---
title: MathText
app_file: app.py
sdk: gradio
sdk_version: 3.15.0
license: agpl-3.0
---

## MathText NLU

Natural Language Understanding for math symbols, digits, and words with a Gradio user interface and REST API.

## Setup your Python environment

Launch a `terminal` on linux (or the `git-bash` application on Windows).
Then create a virtualenv with whatever python version you have available on your system.

Any python version greater than `3.7` should work.
Most of us on Linux systems use Python `3.9`: 

```bash
git clone git@gitlab.com:tangibleai/community/mathtext
cd mathtext
pip install --upgrade virtualenv poetry
python -m virtualenv .venv
ls -hal
```

You should see a new `.venv/` directory.
It will contain your python interpreter and a few `site-packages` like `pip` and `distutils`.

Now activate your new virtual environment by sourcing `.venv/bin/activate` (on Linux) or `.venv/scripts/activate` (on Windows).

```bash
source .venv/bin/activate || source .venv/scripts/activate
```

## Developer installation

Once you have a shiny new virtual environment activated you can install the `mathtext` in `--editable` mode.
This way, when you edit the files and have the package change immediately.

Make sure you are already within your cloned `mathtext` project directory.
And makes sure your virtual environment is activated.
You should see the name of your virtual environment in parentheses within your command line prompt, like `(.venv) $`.
Then when you install MathText it will be available to any other application within that environment.

```bash
pip install --editable .
```

## User installation

If you don't want to contribute to the MathText source code and you just want to import and run the MathText modules, you can install it from a binary wheel on PyPi.

```bash
pip install mathtext
```

## Usage

### Sentiment classification




### Directory structure with notes
```text
mathtext
    mathtext: mathtext code
        data: training and test sets for various tasks
        models: scripts to create models and store in/retrieve from object storage
        utils: utility functions
            checkers.py: T/F evaluations
            converters.py: Change the data type from one to another
            extractors.py: Looks for specific values or value types in a message
            formatters.py: Attempts to format text in a standardized way
        api_gradio.py: gradio api
        predict_intent.py: functions to run multilabel recognizer on message
        text_processing.py: evaluations that use sequences of utils
    scripts: setup scripts
        api_scaling.sh: makes calls to local api
        api_scaling.py: makes async http requests to the local api
        build.sh
        plot_calls.py: Functions for plotting data
        pyproject.template
    tests: various tests
        __init.py
        test_cases_all.py
    .git*: various git files
    app.py: ties all of the api components together for huggingface
    LICENSE.md: license
    pyproject.toml: pyproject file
    README.md: this
    requirements.txt: project dependencies
```            