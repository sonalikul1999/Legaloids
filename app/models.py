from django.db import models
import datetime
from django.conf import settings
TIME_FORMAT = '%d.%m.%Y'

class BlogData(models.Model):
	Blog_Date=models.DateField(("Date"), default=datetime.date.today)
	Blog_ID=models.CharField(max_length=100)
	Blog_Title=models.CharField(max_length=100)
	Blog_Category=models.CharField(max_length=100)
	Blog_Body=models.CharField(max_length=2000)
	Blog_Image=models.ImageField(upload_to="blogimages/")
	class Meta:
		db_table="BlogData"