gcloud builds submit --tag=gcr.io/liu-onefaculty-qa/onefaculty-oauth2-client --project=liu-onefaculty-qa

gcloud run deploy onefaculty-oauth2-client --image=gcr.io/liu-onefaculty-qa/onefaculty-oauth2-client \
--platform=managed --project=liu-onefaculty-qa --allow-unauthenticated --region=us-central1 \
--set-env-vars=OAUTH2_PROVIDER=https://liu-login-qa.appspot.com \