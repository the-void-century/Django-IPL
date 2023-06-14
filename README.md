# Django IPL- Project

## Introduction

- A full stack application that displays various statistics related to the Indian Premier league.

## How to install

- Install python

        sudo apt-get install python

- Install all the dependencies

        pip install -r requirements.txt

## How to run

        python manage.py runserver\

## APIs to get JSON files

- For the main page

        localhost:8000/stats

- For the JSON file of problem 1:

        http://localhost:8000/stats/matches-per-year

- For the JSON file of problem 2:

        http://localhost:8000/stats/won-per-year-per-team

- For the JSON file of problem 3:

        http://localhost:8000/stats/extra-runs-conceded

- For the JSON file of problem 4:

        http://localhost:8000/stats/top-ten-economical-bowlers


# APIs for the charts

- Add `/chart` after a URL to get their respective charts, Example:

        http://localhost:8000/stats/match-per-year/chart


## Credits

- Utsav Dhall