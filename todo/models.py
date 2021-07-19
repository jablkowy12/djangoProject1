from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField('title', max_length=255)
    description = models.TextField('description', null=True, blank=True)
    pub_date = models.DateTimeField('date published')
    done = models.BooleanField('done', default=False)

    def __str__(self):
        return self.title
