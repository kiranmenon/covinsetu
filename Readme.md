# Covinsetu
This repo hosts simple Python scripts based on "requests" module, to query COWIN API.
Using COWIN public API V1.3.1 [https://apisetu.gov.in/public/marketplace/api/cowin]

The script will query on COWIN API and push notification to pushbullet, also print to stdout. Currently it uses "calendayByPin" and "calendarByCenter" APIs.

## Requirements and setups
Python3 

pip 21.1.3 

pip install -r requirements.txt

### configuration
Use config-sample.json as reference to create "config.json"

Generate and provide COWIN API access token and also the pushbullet API token.

### Run via crontab
eg:
@hourly /usr/bin/env bash -c " source ~/my-venv/bin/activate && cd ~covinsetu-master-0.0.1 && python main.py > ~/logs.txt 2>&1 && deactivate"

### Run tests
eg: python -m unittest test_acceptance/test_calendarByPin.py