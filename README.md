## Development

GCP Cloud Run Schekeleton -> One of the best services to host your workloads on Google, based on Dockers completely managed service, so only focus on your code :).

#### Install virtualenv
python3 -m pip install virtualenv

#### Create virtualenv
```bash
python3 -m virtualenv -p python3 venv
```

#### Activate virtualenv
```bash
source venv/Scripts/activate
```

#### Install requirements
```bash
pip install -r requirements.txt
```

#### Run
```bash
python app.py
```


## Run on Docker (locally)

#### Install Docker
https://docs.docker.com/docker-for-windows/

#### Build image

```bash
docker image build -t [IMAGE-NAME] .
```

#### Run container

```bash
docker container run --env-file=.env --rm --publish=8080:8080 --name=[CONTAINER-NAME] [IMAGE-NAME]
```

#### Stop container

```bash
docker container stop [CONTAINER-NAME]
```

#### Delete container

```bash
docker container rm [CONTAINER-NAME]
```

#### Delete image

```bash
docker image rm [IMAGE-NAME]
```


## Run on Google Cloud Run

#### Install gcloud
https://cloud.google.com/sdk/docs/downloads-interactive

#### Build container image

```bash
gcloud builds submit --tag=gcr.io/[PROJECT-ID]/[IMAGE-NAME] --project=[PROJECT-ID]
```

#### Deploy container image

```bash
gcloud run deploy [SERVICE-NAME] --image=gcr.io/[PROJECT-ID]/[IMAGE-NAME] --platform=managed --project=[PROJECT-ID] --allow-unauthenticated --region=us-central1
```

#### Create queue

> gcloud tasks queues create blackboard-tasks --project liu-profile-api-v2-staging
