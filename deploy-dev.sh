gcloud builds submit --tag=gcr.io/liu-onefaculty-dev/onefaculty-login --project=liu-onefaculty-dev

gcloud run deploy onefaculty-login --image=gcr.io/liu-onefaculty-dev/onefaculty-login \
--platform=managed --project=liu-onefaculty-dev --allow-unauthenticated --region=us-central1 \
--set-env-vars=OAUTH2_PROVIDER=https://liu-login-dev.appspot.com \