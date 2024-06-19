# Backend-Technical-Challenge-
# Savannah Informatics Limited Backend Challenge
Backend challenge code

This project has six tasks:
- Creating a PytChon/Go service
- Designing Customer and Orders database
- Adding a REST or GraphQL API to input / upload customers and orders
- Implementing authorization and authentication using OpenID Connect
- Sending an alert SMS to customer when a new order is added
- Writing unit tests with coverage checking, set up CI and automated CD and finally deploy to either PAAS/FAAS/IAAS

## Technology Stack
- Python
- Django Web Framework
- Django Rest Framework
- Heroku
- Whitenoise
- Postgresql
- Pytest

## Basic Commands
### Test coverage
First, navigate to project's root directory
`cd mysite`


To run the tests, check your test coverage, and generate a simplified coverage report:

`$ pytest`

To generate an HTML report:

`coverage html`

`open htmlcov/index.html`

## Running the project locally
First, clone the repository to your local machine:

`git clone https://github.com/vincenttommi/Backend-Technical-Challenge-.git`


Install the requirements:

`pip3 install -r requirements.txt`

Create the database by running migrations:

`python3 manage.py migrate`

Run the development server:

`python3 manage.py runserver`

The project will be avalable at **127.0.0.1:8000**

## Deployment
This project was automatically deployed to Heroku via gitlab CI/CD jobs