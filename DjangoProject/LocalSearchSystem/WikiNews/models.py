from django.db import models


# Create your models here.
# Creating Item table



# Creating custom field type that can store a data contains text and images in MySQL
class BlobField(models.Field):
    description = "Blob"
    def db_type(self, connection):
        return 'blob'



class WikiNewsItem(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length=500, null=True)
    text = models.TextField()
    image = models.TextField()
    lastUpdated = models.DateField(null=True)

    def __unicode__(self):
        return "{}".format(self.title)

    class Meta:
        db_table = 'WikiNewsItem'