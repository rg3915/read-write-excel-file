# read-write-excel-file

Read and Write Excel file with [openpyxl](https://openpyxl.readthedocs.io/en/stable/) on [Django](https://www.djangoproject.com/) application.

## This project was done with:

* Python 3.6
* Django 2.2.10

## How to run project?

* Clone this repository.
* Create virtualenv with Python 3.
* Active the virtualenv.
* Install dependences.
* Run the migrations.

```
git clone https://github.com/rg3915/read-write-excel-file.git
cd read-write-excel-file
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
```