from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from task import ImagetopdfDeleteImagesTrigger,ImagetopdfDeletePDFTrigger



# Execute the functions in the task.py file at specific intervals

def start():
	scheduler = BackgroundScheduler()
	scheduler.add_job(ImagetopdfDeleteImagesTrigger, 'interval', seconds=600)
	scheduler.add_job(ImagetopdfDeletePDFTrigger, 'interval', seconds=600)
	scheduler.start()