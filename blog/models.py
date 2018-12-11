from django.db import models as db

# Create your models here.
class Blog(db.Model):
    title = db.CharField(max_length = 255)
    pub_date = db.DateTimeField(auto_now_add = True)
    body = db.TextField()
    image = db.ImageField(upload_to = 'images/')
