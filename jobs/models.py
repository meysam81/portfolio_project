from django.db import models as db

# Create your models here.
class Job(db.Model):
    image = db.ImageField(upload_to = 'images/')
    summary = db.CharField(max_length = 200)
