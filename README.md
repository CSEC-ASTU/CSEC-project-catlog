# CSEC-project-catlog

## Project Description

This project is used as a catalog for all the projects that student have done in the past. This will help the student promote themselves to get internship easily and also help other students to get the best of their skills.

## Development Environment

Every developer must follow this steps when developing on a new feature.

1. The developer must create a new branch with the below format
    - **task/name/description**
    - example: **task/chapi/authentication**

2. After developing the feature, the developer must request a pull request to the master branch if the test is passed.

3. Developer must follow Standard Coding Style provided by Flake8 and black.


## Datanase Configration for PostgreSQL

```psql
create user muday_user with encrypted password 'muday_password';
create database muday;
grant all privileges on database muday to muday_user;
```
