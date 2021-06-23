from django.db import models
from datetime import date

class Creator(models.Model):
	crName = models.TextField(default="")
	gender = (('F', 'Female'), ('M', 'Male'),('O','Others'))
	crGender = models.CharField(max_length=1 ,help_text="Creator Gender", choices=gender, default="")
	crEAddress = models.EmailField(default="")
	crContactNumber = models.CharField(default="", max_length=11)
#	uImage = models.TextField(default="")
	class meta:
		db_table = "creator"


class Dish(models.Model):
	CreatorId = models.ForeignKey(Creator, default=None, on_delete=models.DO_NOTHING)
	dNameofDish = models.TextField(default="")
	dMainIngredient = models.TextField(default="")
	dDate = models.DateField(blank=True, default=date(1111, 11, 11), null=True, help_text="Today Date.")
	dDifficulty = models.TextField(default="")
	dCategory = models.TextField(default="")
	dServings = models.TextField(default="")
	class meta:
		db_table = "dish"


class Recipe(models.Model):
	CreatorId = models.ForeignKey(Dish, default=None, on_delete=models.DO_NOTHING)
	rQuantity = models.TextField(default="")
	rUnit = models.TextField(default="")
	rIngredients= models.TextField(default="")
	rProcedures = models.TextField(default="")
	rImage = models.TextField(default="")
	class meta:
		db_table = "recipe"



class Comments(models.Model):
	CreatorId = models.ForeignKey(Dish, default=None, on_delete=models.DO_NOTHING)
	cDate = models.DateField(blank=True, default=date(1111, 11, 11), null=True, help_text="Today Date.")
	cName = models.TextField(default="")
	cComments = models.TextField(default="", max_length=100)
#	uThumbsUp = models.CharField(default="", max_length=100)
#	uThumbsDown = models.CharField(default="", max_length=100)
	class meta:
		db_table = "comments"


#class User(models.Model):
#	CreatorId = models.ForeignKey(Comments, default=None, on_delete=models.DO_NOTHING)
#	uName = models.TextField(default="")
#	uEAddress = models.EmailField(default="")
#	uThumbsUp = models.CharField(default="", max_length=100)
#	uThumbsDown = models.CharField(default="", max_length=100)
#	class meta:
#		db_table = "user"