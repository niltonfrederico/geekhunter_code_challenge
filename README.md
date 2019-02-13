[![CircleCI](https://circleci.com/gh/kuresto/geekhunter_code_challenge.svg?style=svg)](https://circleci.com/gh/kuresto/geekhunter_code_challenge)

# Abundantia API

`Abundantia` was the Roman Godness of abundance and prosperity. This API was developed for a code challenge by Geek Hunter.

## Requirements

To run locally you will need [docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/) and [docker-compose](https://docs.docker.com/compose/install/). That's it, just it.

## Documentation

You can access the API documentation at http://ec2-3-17-129-246.us-east-2.compute.amazonaws.com.

## How to test locally

I suggest using Python's Virtualenv (https://virtualenv.pypa.io/en/latest/) before doing this steps.

```sh
cd path/to/repo/

# Build development containers
make build

# Run all tests
make test

# Up container
make up
```

## F.A.Q.

### - What was the stack used?
Python 3.6, Django 2.1, Django Rest Framework, MongoDB, Redis, Celery and some other things. It runs fine on MySql too.

### - Well, I was reading the code, why don't use a authentication app?
Even if it is very common for Code Challenges to always use a authentication tool, I found better use the time to do some other nice things... Like the possibility of multiple backends, a nice common code and another things.

### - What is the test coverage %?
About 91%.

### - I read some queries and I think there is better ways to do some...
Well, you are right. But `djongo` (mongodb driver which is compatible to Django ORM without changing a thing) have some limitations with `__date` and subqueries.

### - Where is the environment variables?
In the server, duh.

### - Something you didn't like about this project?
Well... The deploy is being done almost manually. Didn't had the time to write a deploy code.
