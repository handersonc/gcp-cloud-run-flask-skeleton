from database.datastore_client import DatastoreClient
from google.cloud import datastore
from database.models.user import User

class UserRepository(DatastoreClient):

  kind = 'User'

  def __init__(self):
    DatastoreClient.__init__(self)

  def create(self, user: User):
    key = self.client.key(self.kind, user.email)
    entity = datastore.Entity(key=key)
    entity.update(user.to_dict())
    self.client.put(entity)
  
  def get(self, key):
    return self.client.get(key)
  
  def list(self):
    return self.client.query(kind=self.kind).fetch()
