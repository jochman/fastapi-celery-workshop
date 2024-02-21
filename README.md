# fastapi-celery-workshop

To run this project, you need docker.

```sh
docker compose up
```

## Challenge

Theres a function called `calculate_pi` in `worker/pi_calc.py`.

1. Create a task in worker/app.py to run that function
1. Add an endpoint in api/app.py to access this function

results can be found in the branch `calculate-pi`

## Local Development

For local development, there are running scripts in root dir, worker and api.

1. add execute permissions `chmod +x run.sh run_worker.sh run_api.sh`
1. run docker-compose without api and worker `./run.sh`
1. run worker `./run_worker.sh`
1. run api `./run_api.sh`

The api and worker will automatically reload when files in their folder are changed.
