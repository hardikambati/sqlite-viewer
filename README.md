## Spinning up the server

### Using docker run command

```
docker run -p <PORT>:8080 -v $(pwd)/<DB_NAME>:/code/app.db hardikambati/sqlite-viewer
```

### Using in docker-compose.yaml
```
version: "3"

services:

  sqlite_reader:
    image: hardikambati/sqlite-viewer
    ports:
      - <PORT>:8080
    volumes:
      - ./<DB_NAME>:/code/app.db
```