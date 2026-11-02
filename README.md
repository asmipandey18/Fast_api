|-- app
|   |__ __init__.py
    |main.py
    |__ server
        |__ app.py
        |__ database.py
        |__ models
        |__ routes
- requirements.txt


folders: 
- app
    - server
        - models
        - routes


step
1. install libraries
2. define entry point (main.py)
3. i need to define the app
4. simply build an application for storing student data with following CRUD operations
    - get student (GET)
    - add student (POST)
    - get student by id (GET)
    - update student by id (PUT)
    - delete student by id (DELETE)

5. Before moving ahead, we need to know about the data
    - data model (how the data is being stored in the database)
    - we are using pydantic schema design for validating the data..
    - to implement this, in app/server/models, we need to create a file named as student.py
    - add the data model in the file

6. make sure mongo db is installed in your system
    - if you dont have mongodb, you can install either in a way
        - download mongodb image from docker and up the database (preferred)
        - install mongodb in your system

        Install mongodb using docker using following command
        ```docker run -d --name mongodb -p 27017:27017 mongo:5.0.6```

7. we need to connect the database to our codebase
   - 
