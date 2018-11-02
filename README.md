# hyrespace
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
* obtain the token at first:<br>
curl -X POST -d "username=<>&password=<>" http://localhost:8000/api-token-auth/<br>
* and take update 'location' as an example:<br>
curl -X PUT -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NDA5NTU3ODYsImVtYWlsIjoiaHNienpoekAxMjYuY29tIiwidXNlcm5hbWUiOiJob2dhbiIsInVzZXJfaWQiOjF9.GL1qYeG1RR9Tp5oFogMK1Rm_rQeeulEx1w5DUrtJEB8" -d "location=Sydney" http://127.0.0.1:8000/users/studentprofiles/1/
<br><br>
curl -X PUT -H "Authorization: JWT <token>" -d "location=Sydney" url

<br>the token will expire in 60 seconds<br>
it also can be used in Postman<br>

![Image text](https://raw.githubusercontent.com/Par-sad/hyrespace/master/img-folder/inro1.jpg)  
