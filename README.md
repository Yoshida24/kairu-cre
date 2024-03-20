# structured-ai
複数の得意分野を持つAIをオーケストレーションし回答を導き出す

## Usage

depends on:
- Python: 3.11
- pip: 24.0
- GNU Make: 3.81

support:
- OS: M1 Macbook Air Sonoma 14.4


## Gettig Started
First of all, install VSCode recommended extensions. This includes Linter, Formatter, and so on. Recommendation settings is written on `.vscode/extensions.json`.

Then, make virtual env and activate it:

```bash
python -m venv .venv
. .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run below script to create `.env`

```bash
if [ ! -f .env ]; then
    cp .env.sample .env
    echo 'Info: .env file has successfully created. Please rewrite .env file'
else
    echo 'Info: Skip to create .env file. Because it is already exists.'
fi
```

Then, set OpenAI API Key.

Now you can run script:

```bash
# load environment variables from .env to your shell.
set -a && source ./.env && set +a
make run
```

> **Note**
>
> This project *does not* depends on `dotenv-python`. Instead, using below script.
> `set -a && source ./.env && set +a`

## Jupyter

```bash
jupyter lab
```

## Develop App
On usual develop, first you activate `venv` first like below.

```bash
source .venv/bin/activate
```

Save requirements:

```bash
pip freeze > requirements.txt
```

Deactivate venv:

```bash
deactivate
```
