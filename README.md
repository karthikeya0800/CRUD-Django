[Deployed webpage](https://crud-app.run.place/django)

# Clone the repository

```
git clone https://github.com/karthikeya0800/CRUD-Django.git
```

To run the application, cd to CRUD-Node and use the following command:

```
docker compose up -d
```

- **Frontend server will run on port 5173**

- **Backend server will run on port 3001**

- **MySQL will run on port 3306**


To stop all the containers, use the following command:

```
docker compose down
```

To delete containers, images, volumes, and unused networks, use the following command:

_Note: Only works on Linux_

```
sh docker-clear.sh
```

If port is in use, change it in docker-compose.yml or use the command below to kill the process. Then **restart the container**.

_Note: Only works on Linux_

```
sh kill-port.sh <port_number>
```

<br>

# App video

[![Watch the video](crud-app.png)](https://youtu.be/v-hkX_6a-XE)
