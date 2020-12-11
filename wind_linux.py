import os
from pynotifier import Notification


if os.name == 'nt':

    Notification(
            title='pythonexplainedto.me',
            description='Notification with pynotifier',
            icon_path='logo.ico', # On Windows .ico is required, on Linux - .png
            duration=5,                              # Duration in seconds
            urgency=Notification.URGENCY_CRITICAL
    ).send()

else:
        Notification(
            title='pythonexplainedto.me',
            description='Notification with pynotifier',
            icon_path='logo.png', # On Windows .ico is required, on Linux - .png
            duration=5,                              # Duration in seconds
            urgency=Notification.URGENCY_CRITICAL
    ).send()
