# Naagmani (The FastAPI python boilerplate)

## To run the project

```bash
cd src/
python main.py make-migrations
python main.py migrate
python main.py run 0.0.0.0 80 --debug
```

## Pre-Commit
The boilerplate already has all the popular pre-commit hooks pre-configured and corresponding configurations are done in the pyproject.toml file. Edit as per your needs.

## Deployment

The boilerplate already has a base docker-compose and Dockerfile for deployment. The DockerComposeDev file is for development environment, it has infisical configured.

## Local Develpment
The docker-compose.yml file can be used to run the postgresql docker container when needed.
