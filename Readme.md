# Simple Test API in python using flask and flask_restful


## Available requests

For now, there are only three requests:
- ```GET /```
    returns a hello world statement
- ```GET /file```
    returns the content of ```file.txt``` (yes, it is hardcoded, this is still a test)
- ```POST /write?content=test```
    writes "test" to ```file.txt```

## Port and IP

for now, the localhost IP 127.0.0.1 and port 5000 are used.

## Plans for the future

- add useful endpoints for testing, for example registration  of smart home devices
- add backend connections to a database
- possibly convert to docker image
