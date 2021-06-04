from django.test import TestCase
#from django.urls import resolve
#from RecipeBookApp.views import RecipeBook
#from django.http import HttpRequest
#from django.template.loader import render_to_string
from RecipeBookApp.models import Dish, Creator

class HomePageTest(TestCase):

#	def test_root_url_resolves_to_mainpage_view(self):
#		found = resolve('/')
#		self.assertEqual(found.func, RecipeBook)

	def test_mainpage_returns_correct_view(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'homepage.html')


class ORMTest(TestCase):

	def test_saving_retrieving_list(self):
		newCreator = Creator()
		newCreator.save()
		txtDish1 = Dish()
		txtDish1.CreatorId = newCreator
		txtDish1.dNameofDish = 'Dish one'
		txtDish1.save()
		txtDish2 = Dish()
		txtDish2.CreatorId = newCreator
		txtDish2.dNameofDish = 'Dish two'
		txtDish2.save()
		savedCreator = Creator.objects.first()
		self.assertEqual(savedCreator, newCreator)
		savedDishs = Dish.objects.all()
		self.assertEqual(savedDishs.count(), 2)
		savedDish1 = savedDishs[0]
		savedDish2 = savedDishs[1]
		self.assertEqual(savedDish1.dNameofDish, 'Dish one')
		self.assertEqual(savedDish2.dNameofDish, 'Dish two')
		self.assertEqual(savedDish1.CreatorId, newCreator)
		self.assertEqual(savedDish2.CreatorId, newCreator)



class ViewTest(TestCase):


	def test_listview_uses_listpage(self):
		newCreator = Creator.objects.create()
		response =self.client.get(f'/RecipeBookApp/{newCreator.id}/')
		self.assertTemplateUsed(response, 'next.html')


	def test_pass_list_to_template(self):
		creatorList1 = Creator.objects.create()
		creatorList2 = Creator.objects.create()
		passList = Creator.objects.create()
		response = self.client.get(f'/RecipeBookApp/{passList.id}/')
		self.assertEqual(response.context['CreatorId'], passList)



class CreateListTest(TestCase):

#	def test_save_POST_request(self):
#		self.client.post('/RecipeBookApp/newlist_url', data={'Ingredients': 'New entry'})
#		self.assertEqual(Dish.objects.count(),1)
#		newDish = Dish.objects.first()
#		self.assertEqual(newDish.dNameofDish, 'New entry')

	def test_save_POST_request_2(self):
		self.client.post('/RecipeBookApp/newlist_url', data={'fName': 'New creator', 'fGender': 'New creator gender', 'fEAddress': 'New email address', 'fContactNumber': 'New creator number'})
		self.assertEqual(Creator.objects.count(), 1)
		newCar = Creator.objects.first()
		self.assertEqual(newCar.crName, 'New creator')
		self.assertEqual(newCar.crGender, 'New creator gender')


	def test_redirect_POST_2(self):
		response = self.client.post('/RecipeBookApp/newlist_url', data={'fName': 'New creator', 'fGender': 'New creator gender', 'fEAddress': 'New email address', 'fContactNumber': 'New creator number'})
		newList = Creator.objects.first()
		self.assertRedirects(response, f'/RecipeBookApp/{newList.id}/')




#	def test_redirect_POST(self):
#		response = self.client.post('/RecipeBookApp/newlist_url', data={'Ingredients': 'New entry'})
#		newList = Creator.objects.first()
#		self.assertRedirects(response, f'/RecipeBookApp/{newList.id}/')

class AddDishTest(TestCase):

	def test_add_POST_request_to_existing_list(self):
		CreatorList1 = Creator.objects.create()
		CreatorList2 = Creator.objects.create()
		existingList = Creator.objects.create()
		self.client.post(f'/RecipeBookApp/{existingList.id}/addDish', data={'nNameofDish':'New Dish for existing list','nMainIngredient':'New Dish for existing list','nDifficulty':'New Dish for existing list','nCategory':'New Dish for existing list','nServings':'New Dish for existing list',})#'Ingredients':'New Dish for existing list', 'Procedures':'New Dish existing list'})
		self.assertEqual(Dish.objects.count(),1)
		newDish = Dish.objects.first()
		self.assertEqual(newDish.dNameofDish, 'New Dish for existing list')
		self.assertEqual(newDish.CreatorId, existingList)

	def test_sredirect_to_list_view(self):
		CreatorList1 = Creator.objects.create()
		CreatorList2 = Creator.objects.create()
		CreatorList3 = Creator.objects.create()
		existingList = Creator.objects.create()
		response = self.client.post(f'/RecipeBookApp/{existingList.id}/addDish', data={'nNameofDish':'New Dish for existing list','nMainIngredient':'New Dish for existing list','nDifficulty':'New Dish for existing list','nCategory':'New Dish for existing list','nServings':'New Dish for existing list',})#'Ingredients':'New Dish for existing list', 'Procedures':'New Dish existing list'})
		self.assertRedirects(response, f'/RecipeBookApp/{existingList.id}/')
