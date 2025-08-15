# python-playwright-example

## Prerequisites

- Python v3.13.5
- pip
- Create and active the virtual environment
- Install Python requirements
- Set a specific location for managing browser binaries (Optional)
- Download Playwright browser binaries

```
$ python -m venv venv
$ source venv/bin/activate
$ pip install --upgrade pip
$ pip install -r requirements.txt
$ export PLAYWRIGHT_BROWSERS_PATH=$HOME/pw-browsers
$ python -m playwright install
```

- Check Python code

```
$ pylint scripts
```

## Scripts

- Usage
```  
$ pytest
$ pytest ./scripts/test_example.py
$ pytest --headed
$ pytest --browser webkit --browser firefox
$ pytest --html=reports/report.html
```