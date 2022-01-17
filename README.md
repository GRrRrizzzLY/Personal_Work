# How to run test

```shell
export SELENIUM_GRID_URL="GRID_URL_GOES_HERE"
python3.8 -m venv venv
./venv/bin/pip install -r requirements.txt
./venv/bin/pytest test_smoke.py --alluredir allure-reports
```
