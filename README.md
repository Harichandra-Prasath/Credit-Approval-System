## CREDIT APPROVAL SYSTEM

Backend of Credit Approval system built using django-restframework and postgres as database   

### SETUP

- Clone this repository  
- Create a Virtual environment and Activate it  (Optional)
```bash
python -m venv .venv  
. .venv/bin/activate  
```
- Install the necessary dependencies 
```bash
pip install -r requirements.txt  
``` 
- Create a .env file on the root directory  
```bash
DB_NAME=
DB_USER=
DB_PASSWORD=
HOST=
```
- Make sure the database with DB_NAME exist on your local postgres server   
- Run migrations and migrate it to the database
```bash
python manage.py makemigrations api
python manage.py migrate
```
- Run tests to ensure the reliability  
```bash
python manage.py test
```
- Run the server and populate the database in the background  
```bash
python manage.py runserver && python manage.py populate && fg
```
- If everything went fine, Success message will be logged and server will listen on port 8000  


### Docker

To run it as a container, Simply Run   
```bash
sudo docker compose up
```
If current user is in docker group, Following is enough  
```bash
docker compose up
```

#### Addtional Info for Docker Container

- You will get a warning from dotenv module indicating .env file not found.   
- This is expected as we pass env variables in docker-compose. Please ignore the Warning.  
     
- You might see docker logging some error while populating database.     
- This is due to duplicate loan_ids present in the loan_data.xlsx.  
- These are not fatal and expected. So ignore them.  