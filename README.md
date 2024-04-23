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
1. Home Page of the Website
   ![Screenshot (331)](https://github.com/HarshilShah1804/Electoral_Bonds_Website/assets/143382356/9fa6c5e6-ec82-41a8-9c33-6e5a0e9ca32a)

2. Answer of Question 1 for *bond number* 11448.
   ![Screenshot (332)](https://github.com/HarshilShah1804/Electoral_Bonds_Website/assets/143382356/bc1445ab-1bb2-445f-b788-4bb6ec1248e6)

3. Answer of Question 2 for company *AALYA CONSTRUCTIONS*
![Screenshot (333)](https://github.com/HarshilShah1804/Electoral_Bonds_Website/assets/143382356/b293f1e6-7503-4f87-a7ee-9ac5e52c3698)

4. Answer of Question 3 for party *JAMMU AND KASHMIR NATIONAL CONFERENCE*
   ![Screenshot (334)](https://github.com/HarshilShah1804/Electoral_Bonds_Website/assets/143382356/2dfc36c6-0d2c-43b5-8960-ed4fad0c476d)

5. Answer of Question 4 for party *GOA FORWARD PARTY*
![Screenshot (335)](https://github.com/HarshilShah1804/Electoral_Bonds_Website/assets/143382356/15ecc448-ecef-47d1-b1da-a117681ed7cf)

6. Answer of Question 5 for company *ABHISHEK TIBREWAL*
![Screenshot (336)](https://github.com/HarshilShah1804/Electoral_Bonds_Website/assets/143382356/0e6a8fbd-b8b1-4d95-af94-e3b32b224a21)

7. Answer of Question 6:
![Screenshot (337)](https://github.com/HarshilShah1804/Electoral_Bonds_Website/assets/143382356/cab120a5-db74-45ad-8dfd-6cf6355fde76)
