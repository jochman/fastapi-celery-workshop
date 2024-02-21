# fastapi-celery-workshop

To run this project, you need docker.

```sh
docker compose up
```

## Local Development

For local development, there are running scripts in root dir, worker and api.

1. add execute permissions `chmod +x run.sh run_worker.sh run_api.sh`
1. run docker-compose without api and worker `./run.sh`
1. run worker `./run_worker.sh`
1. run api `./run_api.sh`

The api and worker will automatically reload when files in their folder are changed.