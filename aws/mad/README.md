# Master Acceptance Database Example Application

Sample application based on the Master Acceptance Database, a number of the tables have been extracted and fields have been created in a postgres database and the resources exposed via a rest CRUD API.

## Create a virtual environment or use your existing virtual environment and install dependencies

`mkvirtualenv mad`

`workon mad`

`pip install -r requirements.txt`

## Start development environment

`make start-dev`

## Start dev stack in detached mode

`make dev-up`

## Create database schema in development environment

`make dev-schema`

## Create development data

`make dev-data`

## Clean development environment

`make dev-clean`

## Run unit tests

`make unit-test`