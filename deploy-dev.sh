gcloud builds submit --tag=gcr.io/project-id/service --project=project-id

gcloud run deploy service --image=gcr.io/project-id/service \
--platform=managed --project=project-id --allow-unauthenticated --region=us-central1