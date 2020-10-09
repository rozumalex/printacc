# printacc 
[![Build Status](https://travis-ci.com/rozumalex/printacc.svg?branch=main)](https://travis-ci.org/github/rozumalex/printacc)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/rozumalex/printacc/blob/master/LICENSE)

Print Accounting System

---

## Installation Guide
To run printacc on your device, please follow the instruction.

### Install pyenv
Follow the [instructions](https://github.com/pyenv/pyenv#installation)

### Install Python 3.6
```
pyenv install 3.6.12
```

### Clone the project to your local machine
```
git clone https://github.com/rozumalex/printacc
```

### Install poetry and dependencies
***Note:*** you should change the directory to project's folder to install dependencies

```
pip install --pre poetry -U
poetry install
```

### Install PostgreSQL, then create database and user
```
sudo apt-get install postgres libpq-dev python-dev -y
sudo -u postgres psql

CREATE DATABASE printacc_db;
CREATE USER printacc_user with encrypted password 'printacc_pass';
GRANT ALL PRIVILEGES ON DATABASE printacc_db TO printacc_user;
ALTER USER printacc_user createdb;
```
***Note:*** then press Ctrl+D

### Create .env file
```
cd printacc
nano .env
```
### And insert following values:
```
DEBUG=on
SECRET_KEY="dev"
DATABASE_URL=psql://printacc_user:printacc_pass@127.0.0.1:5432/printacc_db
```

### Apply migrations to database
```
python manage.py migrate
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/rozumalex/printacc/blob/master/LICENSE) file for details.

