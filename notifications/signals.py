from django.dispatch import Signal

notify = Signal(providing_args=[
    'recipient', 'actor', 'verb', 'action_object', 'target', 'description',
    'timestamp', 'level', 'user_role', 'notify_type',
])
