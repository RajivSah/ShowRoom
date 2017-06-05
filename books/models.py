import os
from django.db import models

#Testing the git push
# Create your models here.
class Publisher(models.Model):
	name=models.CharField(max_length=30)
	address=models.CharField(max_length=50)
	city=models.CharField(max_length=60)
	state_province=models.CharField(max_length=50)
	country=models.CharField(max_length=30)
	website=models.URLField()
	
	def __str__(self):
		return self.name;

class  Author(models.Model):
	first_name=models.CharField(max_length=30)
	last_name=models.CharField(max_length=50)
	email=models.EmailField(blank=True, null=True, verbose_name="E-Mail")

	def __str__(self):
		return "%s %s" %(self.first_name,self.last_name);

class Categories(models.Model):
        cat_name=models.CharField(max_length=100, primary_key=True)     
	
	def __str__(self):
                return "%s" %(self.cat_name);


class pop_features(models.Model):
        feature=models.CharField(max_length=100, primary_key=True)
	
	def __str__(self):
                return "%s" %(self.feature);



class Book(models.Model):
	ISBN=models.CharField(max_length=50, primary_key=True)
	title=models.CharField(max_length=100)
	description=models.TextField(max_length=5000)
	authors=models.ManyToManyField(Author)
	publisher=models.ForeignKey(Publisher)
	publication_date=models.DateField(blank=True, null=True)	
	category=models.ManyToManyField(Categories)
	features=models.ManyToManyField(pop_features, blank=True)
	date_added=models.DateField(blank=True, null=True)	
	image=models.ImageField(null=True, blank=True, upload_to='img', default='img/def.jpg')
	

	def filename(self):
		return self.image.name;

	def __str__(self):
		return self.title;
