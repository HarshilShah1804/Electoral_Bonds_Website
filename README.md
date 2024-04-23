# Electoral Bonds Webiste
This repository is created as a part of the course ES 113 - Data Centric Computing at Indian Institute of Technology, Gandhinagar, under Professor Mayank Singh. 
This repository contains data for the website made for analysing data about electoral bonds purchase and redemption details.

## Setup Details
1. Download the repository as a ZIP file.
2. Using MySQL Workbench, import the data from the *dump_data* sql dump file.
3. Execute this code on the Workbench. You can change the username *testing123* and password *pwd*.
```mysql
CREATE USER 'testing123'@'localhost' IDENTIFIED BY 'pwd';
GRANT ALL PRIVILEGES ON *.* TO 'testing123'@'localhost' WITH GRANT OPTION;
```
4. Open the file app.py. If you have modified the password or username, change the username and password to the one set by you in the lines:
```python
app.config['MYSQL_USER'] = 'testing123'
app.config['MYSQL_PASSWORD'] = 'pwd'
```

5. Run the python file.
6. Open the browser and search ```127.0.0.1```. The Website will be loaded.

## Screenshots of the UI.
