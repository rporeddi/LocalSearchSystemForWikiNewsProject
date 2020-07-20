from django.db import models


# Create your models here.
# Creating Item table

class Item(models.Model):
    itemname = models.CharField(primary_key=True, max_length=200)
    itemsummary = models.CharField(max_length=45)
    lastupdated = models.DateField(max_length=45)

    class Meta:
        db_table = 'Item'


# Creating custom field type that can store a data contains text and images in MySQL
class BlobField(models.Field):
    description = "Blob"
    def db_type(self, connection):
        return 'blob'


# Creating Item Details table
class ItemDetails(models.Model):
    serialnumber = models.AutoField(primary_key = True)
    Item = models.ForeignKey('Item', on_delete=models.CASCADE, db_column='itemname')
    article = BlobField(blank=True)
    collaberation = BlobField(blank=True)
    opinions = BlobField(blank=True)
    sources = models.TextField(blank=True)
    relatedarticles = models.TextField(blank=True)
    externallinks = models.TextField(blank=True)

    class Meta:
        db_table = 'ItemDetails'


class Items(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, null=True)
    content = models.CharField(max_length=1000, null=True)

    class Meta:
        db_table = 'Items'
