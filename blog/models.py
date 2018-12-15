from django.db import models as db

# Create your models here.
class Blog(db.Model):
    title = db.CharField(max_length = 255)
    pub_date = db.DateTimeField(auto_now_add = True)
    body = db.TextField()
    image = db.ImageField(upload_to = 'images/')

    def summary(self):
        return self.body[:30] + "..."

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title

    @staticmethod
    def latest_blogs():
        return Blog.objects.order_by('-pub_date')
