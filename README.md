AquaTrack 🏊‍♂️

AquaTrack is a simple Python CLI app that helps coaches and swim teams manage swimmers and track their meet results.

 Features

- Add, view, and delete swimmers
- Add and view swim results
- Connects to a SQLite database using SQLAlchemy ORM
- User-friendly command-line interface

 Technologies

- Python 3
- SQLAlchemy
- Pipenv (for environment management)

Setup

{bash}
- pipenv install
- pipenv shell
- python lib/seed.py  (populate the database)
- python lib/cli.py   (run the application)

(in my recording the delete funcion wasnt working but I fixed it after)
