# DnA-NeverSummer

### Setting up the database
In mysql shell with GRANT permissions
##### change hostname
> CREATE USER 'user1'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Password@123';  

##### give privileges 
> GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD on *.* TO 'user1'@'localhost' WITH GRANT OPTION;

##### create the database
> create database neversummer0;

##### Setup the tables
// copy paste db.sql into mysql 

### Filling Dummy data
Run the following command, `data` folder contains 
> python3 init.py  

### Run the application
> python3 MiniWorld.py

You will presented with three roles, `Precog` (data analytics), `Game Designer` and `BotWork` to choose from. Based on the role you will be given the queries they can run

Please enter valid input, we tried to reduce sql injections and invalid  inputs as much as possible but we might have slipped some here and there.

## Collaborators :
- Divij
- Bhargav
- Ishwar
