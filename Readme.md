
# Run tests
eg: python -m unittest test_acceptance/test_calendarByPin.py

# Run via crontab
eg:
@hourly /usr/bin/env bash -c " source ~/my-venv/bin/activate && cd ~covinsetu-master-0.0.1 && python main.py > ~/logs.txt 2>&1 && deactivate"