import json
import logging
from google.cloud import pubsub_v1


class PubsubClient(object):
    def __init__(self):
      self.__publisher = pubsub_v1.PublisherClient.from_service_account_file('service_account.json')

    def send_message(self, topic, data: dict):
      topic_path = self.__publisher.api.topic_path('liu-profile-api-dev', topic)
      response = self.__publisher.publish(topic_path, json.dumps(data).encode('utf-8'))
      logging.debug(f'Response after publish: {response}')
