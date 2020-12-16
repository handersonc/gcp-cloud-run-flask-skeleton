gcloud builds submit --tag=gcr.io/liu-onefaculty-staging/onefaculty-oauth2-client --project=liu-onefaculty-staging

gcloud run deploy onefaculty-oauth2-client --image=gcr.io/liu-onefaculty-staging/onefaculty-oauth2-client \
--platform=managed --project=liu-onefaculty-staging --allow-unauthenticated --region=us-central1 \
--set-env-vars=OAUTH2_PROVIDER=https://liu-login-staging.appspot.com \