gcloud builds submit --tag=gcr.io/project-id/service --project=project-id

gcloud run deploy service --image=gcr.io/project-id/service \
--platform=managed --project=project-id --allow-unauthenticated --region=us-central1 \
--set-env-vars=OAUTH2_PROVIDER=https://liu-login-dev.appspot.com \