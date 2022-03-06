from django.apps import AppConfig
from pathlib import Path
import sys         
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR)+'/imagetopdf/')
import schedule


class ImagetopdfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'imagetopdf'
    def ready(self):
        schedule.start()

