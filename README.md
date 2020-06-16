# Example_Apps

- Simple App deployment Examples
- Python Flask example with MySQL

# How to run

- python import_csv.py
- python app.py

# Gunicorn

- gunicorn --bind 0.0.0.0:5000  --log-level=debug app:app
- gunicorn --timeout 120 -w 4 --bind 0.0.0.0:4146 -k gevent --log-level=debug app:app

