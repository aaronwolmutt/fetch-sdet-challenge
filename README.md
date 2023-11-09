# Fetch SDET Challenged

This is a Python poetry app to solve fetch rewards Software Development Engineer in test challenge. The app uses selenium to perform the UI testing and implement the algorithm described in the challange.

Requires Python ^3.9 and poetry to be installed on the system. 

Install poetry on Mac: 

```zsh
 $ pipx install poetry
```

For more info on installing poetry see: https://python-poetry.org/

Also make sure the location of your poetry binaries are on your $PATH

Use this command or add the following to your shell config

```zsh
$ export PATH=/Users/awolmutt/.local/bin:$PATH
```

### Set up the environment

```zsh
$ export POETRY_CHALLENGE_URL="http://sdetchallenge.fetch.com/"
```

### Install the project dependencies

```zsh
$ poetry install
```

### Run the unit tests

```
$ poetry run pytest
```

### Run the full suite

```
$ poetry run start
```