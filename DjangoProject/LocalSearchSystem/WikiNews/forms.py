from django import  forms
from django.forms import Form


def EditItemForm(Form):
    edititemid = forms.IntegerField(label='Item Id')
    edititemtitle = forms.CharField(label='Item Name' ,max_length=255)
