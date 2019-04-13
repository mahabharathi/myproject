from django.db import models

# Create your models here.
class Job(models.Model):

    # Image field is mentioned like this
    image=models.ImageField(upload_to='images/')

    # Summary field is mentioned like this
    summary=models.CharField(max_length=200)

    def __str__(self):
        return self.summary

# To view the summary of the content to editing easier self.summary is called
