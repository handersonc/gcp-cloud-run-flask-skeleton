gcloud builds submit --tag=gcr.io/liu-onefaculty-prod/onefaculty-oauth2-client --project=liu-onefaculty-prod

gcloud run deploy onefaculty-oauth2-client --image=gcr.io/liu-onefaculty-prod/onefaculty-oauth2-client \
--platform=managed --project=liu-onefaculty-prod --allow-unauthenticated --region=us-central1 \
--set-env-vars=OAUTH2_PROVIDER=https://liu-cas-prod-frontend.appspot.com \