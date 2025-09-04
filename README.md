# Odoo

[![Build Status](https://runbot.odoo.com/runbot/badge/flat/1/master.svg)](https://runbot.odoo.com/runbot)
[![Tech Doc](https://img.shields.io/badge/master-docs-875A7B.svg?style=flat&colorA=8F8F8F)](https://www.odoo.com/documentation/master)
[![Help](https://img.shields.io/badge/master-help-875A7B.svg?style=flat&colorA=8F8F8F)](https://www.odoo.com/forum/help-1)
[![Nightly Builds](https://img.shields.io/badge/master-nightly-875A7B.svg?style=flat&colorA=8F8F8F)](https://nightly.odoo.com/)

Odoo is a suite of web based open source business apps.

The main Odoo Apps include an [Open Source CRM](https://www.odoo.com/page/crm),
[Website Builder](https://www.odoo.com/app/website),
[eCommerce](https://www.odoo.com/app/ecommerce),
[Warehouse Management](https://www.odoo.com/app/inventory),
[Project Management](https://www.odoo.com/app/project),
[Billing &amp; Accounting](https://www.odoo.com/app/accounting),
[Point of Sale](https://www.odoo.com/app/point-of-sale-shop),
[Human Resources](https://www.odoo.com/app/employees),
[Marketing](https://www.odoo.com/app/social-marketing),
[Manufacturing](https://www.odoo.com/app/manufacturing),
[...](https://www.odoo.com/)

Odoo Apps can be used as stand-alone applications, but they also integrate seamlessly so you get
a full-featured [Open Source ERP](https://www.odoo.com) when you install several Apps.

---

# The Real Estate Advertisement - Odoo Module

## 📌 Description
This repository contains an Odoo module designed to support the business process of real estate advertisement. 
The module helps real estate companies manage properties, offers, and advertisement transactions more efficiently within the Odoo ecosystem.

## 🚀 Key Features
- Property management (listings for houses, apartments, land, etc.).
- Property categorization by type (e.g., house, apartment, land, etc).
- Property tagging (e.g., *cozy*, *renovated*).
- Offer management with price validation.
- Property state workflow (new → offer received → offer accepted → sold/cancelled).

---

## Getting started with Odoo

For a standard installation please follow the [Setup instructions](https://www.odoo.com/documentation/master/administration/install/install.html)
from the documentation.

To learn the software, we recommend the [Odoo eLearning](https://www.odoo.com/slides),
or [Scale-up, the business game](https://www.odoo.com/page/scale-up-business-game).
Developers can start with [the developer tutorials](https://www.odoo.com/documentation/master/developer/howtos.html).

## Prerequisites

Before you start installing Odoo 18, make sure you have the following:

- **Python 3.12.** – Required for running Odoo.
- **PostgreSQL 12+** – Database server for storing Odoo data.
- **Git** – To clone the Odoo source code repository.
- **pip** – Python package manager to install dependencies.
- **Homebrew** (optional) – Useful for installing Python, PostgreSQL, and other dependencies easily on Mac.


## How to Source Install Odoo on Mac

Follow these steps to set up Odoo from source:

### 1. Clone the Odoo repository
```bash
git clone --depth 1 --branch 18.0 https://github.com/odoo/odoo --single-branch odoo
cd odoo
```

### 2. Create the `odoo.conf` File
Inside the odoo.conf file, paste the following content:
```bash
[options]

; Is This The Password That Allows Database Operations:
admin_passwd = admin

db_host = localhost
db_port = 5432
db_user = odoo
db_password = odoo

addons_path = /home/user/odoo/addons  # Change this to your actual addons path
xmlrpc_port = 8017
```

### 3. Create and activate a Python virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install required Python packages
```bash
pip3 install setuptools wheel
pip3 install -r requirements.txt
```

### 5. Running Odoo
```bash
python3 odoo-bin --addons-path=addons -d [db_name]
```
After the server has started (the INFO log odoo.modules.loading: Modules loaded. is printed), open http://localhost:8069 in a web browser and log into the Odoo database with the base administrator account: use `admin` as the email and, again, `admin` as the password.

## Security

If you believe you have found a security issue, check our [Responsible Disclosure page](https://www.odoo.com/security-report)
for details and get in touch with us via email.
