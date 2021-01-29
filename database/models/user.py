
class User(object):

  def __init__(self, email, first_name, last_name):
    """User Model"""
    
    self.email = email
    self.first_name = first_name
    self.last_name = last_name
  

  def to_dict(self):
    return {
      'email': self.email,
      'first_name': self.first_name,
      'last_name': self.last_name
    }

