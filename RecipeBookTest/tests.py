from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#import unittest
import time
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException

cWait = 3

class PageTest(LiveServerTestCase):


	def wait_row_in_recipe(self, row_text):
		start_time = time.time()
		while time.time()-start_time<cWait:
			time.sleep(0.2)
			try:
				table = self.browser.find_element_by_id('recipe')
				rows = table.find_element_by_tag_name('tr')
				return
			except(AssertionError, WebDriverException) as e:
				if time.time()-start_time>cWait:
					raise e





	def setUp(self):
		self.browser = webdriver.Firefox()

#	def tearDown(self):
#		self.browser.quit()


	def test_start_list_one_user(self):
#		self.browser.get('http://localhost:8000')
		self.browser.get(self.live_server_url)
		self.assertIn('Recipe Book', self.browser.title)

		formButton = self.browser.find_element_by_id('formButton')
		formButton.click()
		time.sleep(.1)
		
		creator = self.browser.find_element_by_id('fName')
		creator.click()
		creator.send_keys('Jesper Johansson')
		time.sleep(.1)
		fGender = self.browser.find_element_by_id('fGender')
		fGender.click()
		fGender.send_keys('Smeerensburg, North Pole')
		time.sleep(.1)

		fEAddress = self.browser.find_element_by_id('fEAddress')
		fEAddress.click()
		fEAddress.send_keys('Smeerensburg, North Pole')
		time.sleep(.1)

		fContactNumber = self.browser.find_element_by_id('fContactNumber')
		fContactNumber.click()
		fContactNumber.send_keys('Smeerensburg, North Pole')
		time.sleep(.1)

		Continue = self.browser.find_element_by_id('Continue')
		Continue.click()
		time.sleep(.2)
#		self.check_for_row_in_listtable('1: Mickey Mouse in Disney Wonderland')

		Ingredients = self.browser.find_element_by_id('nNameofDish')
		Ingredients.click()
		Ingredients.send_keys('Red Shoes White')

		Procedures = self.browser.find_element_by_id('nMainIngredient')
		Procedures.click()
		Procedures.send_keys("King White's Palace")

		Create = self.browser.find_element_by_id('Create')
		Create.click()

	



	def test_other_users_different_urls(self):
#		self.browser.get('http://localhost:8000')
		self.browser.get(self.live_server_url)
		time.sleep(.1)

		formButton = self.browser.find_element_by_id('formButton')
		formButton.click()
		time.sleep(.1)


		creator = self.browser.find_element_by_id('fName')
		creator.click()
		creator.send_keys('Jenny Castillo')
		time.sleep(.1)

		fGender = self.browser.find_element_by_id('fGender')
		fGender.click()
		fGender.send_keys('Smeerensburg, North Pole')
		time.sleep(.1)

		fEAddress = self.browser.find_element_by_id('fEAddress')
		fEAddress.click()
		fEAddress.send_keys('Smeerensburg, North Pole')
		time.sleep(.1)

		fContactNumber = self.browser.find_element_by_id('fContactNumber')
		fContactNumber.click()
		fContactNumber.send_keys('Smeerensburg, North Pole')
		time.sleep(.1)


		Continue = self.browser.find_element_by_id('Continue')
		Continue.click()
		time.sleep(.2)

		Ingredients = self.browser.find_element_by_id('nNameofDish')
		Ingredients.click()
		Ingredients.send_keys('Raya Jinping')
		time.sleep(.1)
		Procedures = self.browser.find_element_by_id('nMainIngredient')
		Procedures.click()
		Procedures.send_keys('Kumandra Xi Palace')
		time.sleep(.1)
		Create = self.browser.find_element_by_id('Create')
		Create.click()
#		viewlist_url = self.browser.current_url
#		self.assertRegex(viewlist_url, '/RecipeBookApp/.+')



#		self.browser.quit()
#		self.browser = webdriver.Firefox()
#		self.browser.get(self.live_server_url)
#		pageBody = self.browser.find_element_by_tag_name('body').text
#		self.assertNotIn('Raya Jinping', pageBody)
#		time.sleep(.1)
#		Ingredients = self.browser.find_element_by_id('Ingredients')
#		Ingredients.click()
#		Ingredients.send_keys('Tony Stark')
#		time.sleep(.1)
#		Procedures = self.browser.find_element_by_id('Procedures')
#		Procedures.click()
#		Procedures.send_keys('Stark industries')
#		time.sleep(.1)
#		Continue = self.browser.find_element_by_id('Continue')
#		Continue.click()
#		user2_url =self.browser.current_url
#		self.assertRegex(user2_url, 'RecipeBookApp/.+')
#		self.assertNotEqual(viewlist_url, user2_url)
#		pageBody = self.browser.find_element_by_tag_name('body').text
#		self.assertNotIn('Raya Jinping', pageBody)
#		self.assertIn('Tony Stark', pageBody)




#if __name__=='__main__':
#	unittest.main()