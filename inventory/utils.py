from .models import Notification


def create_notification(message, notification_type='message', link=None):
    Notification.objects.create(
        message=message,
        notification_type=notification_type,
        link=link
    )
