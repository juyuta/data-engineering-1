#!/bin/bash
set -e

echo "Installing dependencies..."
pip install -r /opt/airflow/requirements.txt

echo "Initializing Airflow DB..."
airflow db init

echo "Creating admin user..."
airflow users create \
    --username admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com \
    --password admin

echo "Starting Airflow Webserver..."
exec airflow webserver