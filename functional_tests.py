from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import unittest
import time

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrive_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn("To-Do", self.browser.title)
        header_text =self.browser.find_element(By.TAG_NAME,'h1').txt
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        inputbox.set_keys('Buy peacock fathers')

        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        self.fail('Finish the test!')

if __name__ == "__main__":
    unittest.main(warnings='ignore')
