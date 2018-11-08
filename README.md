# hyrespace
# Recruitment system api

## 1. set up
Let's build a virtual environment by Pipenv<br>
1. install pipenv<br>
    `$ pip install pipenv`
2. build the environment in virtual area  
    `$ pipenv install`
3. active your virtual environment  
    `$ pipenv shell`
4. exit your virtual environment  
    `$ exit` 
5. if you get error **"TypeError: 'module' object is not callable"**, you can try this command before step 2  
    `$ pipenv run pip install pip==18.0`
        
## 2. How to access data by this API?
* `POST`obtain the token at first:<br>
curl -X POST -d "username=<>&password=<>" http://localhost:8000/api-token-auth/<br>
* `PUT`and take update 'location' as an example:<br>
curl -X PUT -H "Authorization: JWT <token>" -d "key=value" url <br>
* you can also `GET` data:<br>
curl -H "Authorization: JWT <token>" url  
<br>the token will expire in 1 hour<br>
it also can be used in Postman<br>

![Image text](https://raw.githubusercontent.com/Par-sad/hyrespace/master/img-folder/inro1.jpg)  
