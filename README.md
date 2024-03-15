# FastApi

***
## structure

fastapi-framework/   
|-- common  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- enum.py  
|-- model  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- member  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- login.py  
|-- routers  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- member.py  
|-- templates    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- index.html  
|-- Dockerfile  
|-- requirements.txt  
|-- .gitignore  
|-- main.py  
|-- README.md  

***
## structure summary

common -> some common package or tool, like enum  
model -> define class  
routers -> set api domain and path  
templates -> html   

***

## run server
```
- uvicorn main:app --host 127.0.0.1 --port 8001
```

## create requirements
```
- pip3 install pipreqs
- pipreqs . --encoding=utf8

# if requirements.txt already exists, use --forcre {path} to overwrite, like
- pipreqs --force . --encoding=utf8
```

## install requirements
```
- pip3 install -r requirements.txt
```