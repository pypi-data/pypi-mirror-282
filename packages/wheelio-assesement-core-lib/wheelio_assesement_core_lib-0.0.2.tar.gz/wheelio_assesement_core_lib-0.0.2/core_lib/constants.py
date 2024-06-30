import os

RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'rabbitmq')
STATUS_CREATE_QUEUE = os.getenv('STATUS_CREATE_QUEUE', 'status_create')
STATUS_UPDATE_QUEUE = os.getenv('STATUS_UPDATE_QUEUE', 'status_update')
NOTIFY_FRIENDS_QUEUE = os.getenv('NOTIFY_FRIENDS_QUEUE', 'notify_friends')
FRIEND_REQUESTS_QUEUE = os.getenv('FRIEND_REQUESTS_QUEUE', 'friend_requests')
FRIEND_ACCEPTANCE_QUEUE = os.getenv('FRIEND_ACCEPTANCE_QUEUE', 'friend_acceptance')