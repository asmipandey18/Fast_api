## Introduction to FastAPI

### step 1:
- create a repo
- create .venv (use uv package manager)
- install fastapi
- install unicorn[standard]

## step 2:
- create a file name as main.py
- add a GET endpoint and create a funtion for welcome to elevate-x

## step 3:
- run the server using Uvicorn:

   ```uvicorn main:app --reload```

Command used for Univcorn main:app
- host (bind socket to this host)
- port (default 8000)
- reload (enable auto reload)
- version (it displays uvicorn version)
- help (show the message & exit)

### starting uvicorn server from the program itelf

### Path parameters
- e.g ``` https://localhost:8000/hello/asmi```

this path ```/hello/asmi``` 