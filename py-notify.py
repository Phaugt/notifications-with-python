from pynotifier import Notification

Notification(
	title='pythonexplainedto.me',
	description='Notification with python!',
	icon_path='icons/logo.ico', # On Windows .ico is required, on Linux - .png
	duration=5,                              # Duration in seconds
	urgency=Notification.URGENCY_CRITICAL
).send()
