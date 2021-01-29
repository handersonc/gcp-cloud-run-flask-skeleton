from google.cloud import datastore
from google.oauth2 import service_account

class DatastoreClient(object):

  def __init__(self):
    self.client = datastore.Client.from_service_account_json('service_account.json')
    

