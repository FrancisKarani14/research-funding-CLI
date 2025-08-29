
# 📂 Project Collaboration CLI

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red.svg)
![Alembic](https://img.shields.io/badge/Alembic-Migrations-green.svg)
![Click](https://img.shields.io/badge/CLI-Click-yellow.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey.svg)

A **command-line interface (CLI) application** that allows a project procurement organization to manage projects, funding agencies, researchers, and managers. Users can also assign researchers and funding agencies to specific projects.

---

## 📑 Table of Contents

* [✨ Features](#-features)
* [🛠 Technologies](#-technologies)
* [⚙️ Setup Instructions](#️-setup-instructions)
* [📖 Usage](#-usage)
* [👨‍💻 Author](#-author)
* [📜 License](#-license)

---

## ✨ Features

* Interactive **welcome menu** with an exit option
* Helpful **navigation prompts** to guide users
* Feedback messages showing whether an **operation was successful** or not
* Ability to:

  * Add a project
  * Add a funding agency
  * Add a researcher
  * Add a manager
  * Assign researchers and funding agencies to projects

---

## 🛠 Technologies

* Python
* SQLAlchemy – ORM
* Alembic – Database migrations
* Click – CLI handling
* Pipenv – Environment & dependency management

---

## ⚙️ Setup Instructions

### Requirements

* Laptop or PC
* Stable internet connection
* GitHub account & Git installed
* Python **3.10+**

### Clone the Repository

```bash
git clone git@github.com:FrancisKarani14/research-funding-CLI.git
```

### Navigate into the Project Directory

```bash
cd research-funding-CLI
```

### Install Dependencies

```bash
pipenv install
```

### Activate Virtual Environment

```bash
pipenv shell
```

### Run the Application

```bash
python3 cli.py
```

---

## 📖 Usage

Once inside the CLI, follow the **menu instructions** to add projects, funding agencies, researchers, and managers.

Example menu:

```
Welcome to Project Collaboration CLI
1. Add Project
2. Add Researcher
3. Add Funding Agency
4. Add Manager
5. Assign Researcher to Project
6. Assign Funding Agency to Project
7. Exit
```

---

## 👨‍💻 Author

**Francis Karani**

* GitHub: [FrancisKarani14](https://github.com/FrancisKarani14)
* LinkedIn: [Ng'ang'a Karani](https://www.linkedin.com/in/ng-ang-a-karani-5a5106373/?originalSubdomain=ke)

---

## 📜 License

MIT License

```
Copyright (c) 2025 Francis Karani

Permission is hereby granted, free of charge, to any person obtaining a copy  
of this software and associated documentation files (the "Software"), to deal  
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
copies of the Software, and to permit persons to whom the Software is  
furnished to do so, subject to the following conditions:  

The above copyright notice and this permission notice shall be  
included in all copies or substantial portions of the Software.  

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN  
THE SOFTWARE.
```

---



