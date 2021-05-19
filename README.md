# AppSec candidate exercise - Python application

## Install

Install [Docker](https://docs.docker.com/get-docker/).

Build the application image:
```bash
docker build -t test-python .
```

## Run

Run the application:
```bash
docker run --rm -it -p 127.0.0.1:8080:80 test-python
```
**Warning:** this starts a vulnerable application! For security reasons it should not be accessible by 3rd parties.

Visit http://127.0.0.1:8080 to access the application.
