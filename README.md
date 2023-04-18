# Pokemon API
This is a project that uses two Docker containers and an Nginx server to host them. The first container is a PostgreSQL database that stores the data, while the second container is a FastAPI API that provides an interface for accessing and manipulating the data stored in the database. Each container has its own Dockerfile that defines its build and runtime configuration. A Docker Compose file is used to define the environment for the project, including the containers and their configurations, as well as the Nginx server that acts as a reverse proxy. The Nginx server forwards incoming requests to the appropriate container, while the Docker Compose file includes the necessary configuration for setting up the connections between the containers and the Nginx server. By running the Docker Compose file, you can launch the entire project, including the database, API, and Nginx server, all in a single environment. This setup makes it easy to deploy, manage, and scale the project by adding more containers or adjusting their configurations.

## Run Containerized Project
```
$ docker-compose up -d
```

## Run Project Locally

- Run the Database
```
$ cd database
$ docker build -t pokebase .
$ docker run -p 5433:5432
```
- In the main.py update the database connection url as follows

![image](https://user-images.githubusercontent.com/99210748/232352630-b5a6c1bf-31a8-4202-b468-54e59bddae59.png)

- Run the API
```
$ pip install -r requirements.txt
$ uvicorn api.main:app --reload 
```
