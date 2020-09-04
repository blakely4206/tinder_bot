from selenium import webdriver
from time import sleep

class Tinder_Bot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login_phone(self):
        phone_number = input("What is your phone number? ")

        self.driver.get('https://tinder.com')

        sleep(2)

        login_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
        login_btn.click()

        sleep(2)

        phone_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[3]/button')
        phone_btn.click()

        sleep(2)

        phone_txt = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div[2]/div/input')
        phone_txt.send_keys(phone_number)
        phone_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/button')
        phone_btn.click()

        while(True):
            code = input("Enter Tinder Code:")
            break

        boxes = [
            self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div[3]/input[1]'),
            self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div[3]/input[2]'),
            self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div[3]/input[3]'),
            self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div[3]/input[4]'),
            self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div[3]/input[5]'),
            self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div[3]/input[6]')
        ]

        for i in range(len(code)):
            boxes[i].send_keys(code[i])

        confirm_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/button')
        confirm_btn.click()

        sleep(2)

    def swipe_left(self):
        heart_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        heart_btn.click()

    def swipe_right(self):
        x_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        x_btn.click()

   # def run(self):
     #   while True:
      #      sleep(2)
      #      try:
     #           self.swipe_left()
    #        except Exception:
      #          try:
     #               self.close_popup()
     #           except Exception:
     #               self.match()

  #  def close_popup(self):
        #todo

   # def match(self):
        #todo

bot = Tinder_Bot()
bot.login_phone()


