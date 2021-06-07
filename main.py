from selenium import webdriver
import time
import random, datetime
from key import EMAIL, PASSWORD, CLASS_URL
# from trueKey import EMAIL, PASSWORD, CLASS_URL

def main():
  print("指定時間まで待機中")
  while True:
    now = datetime.datetime.now()

    if now.hour == 8 and now.minute == 50 and now.second == 0:
      driver = webdriver.Chrome("./chromedriver")
      driver.get(CLASS_URL)
      today = str(datetime.date.today())

      # Googleのログイン
      login_id_xpath = '//*[@id="identifierNext"]'
      login_pw_xpath = '//*[@id="passwordNext"]'
      login(driver, login_id_xpath, login_pw_xpath)

      #その日のgoogle formを開く
      classroom_element = driver.find_elements_by_css_selector("span[class='YVvGBb asQXV']")
      for item in classroom_element:
        if (str(datetime.datetime.now().month)+"/"+str(datetime.datetime.now().day) in item.text):
          item.click()
          break

      print("ロード中")
      time.sleep(20)
      google_form_xpath = '//*[@id="yDmH0d"]/div[4]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/a'
      driver.find_element_by_xpath(google_form_xpath).click()
      print("ロード中")
      time.sleep(20)

      #handleを開いたタブの方に変更
      handle_array = driver.window_handles
      driver.switch_to.window(handle_array[1])

      #日付
      form_date_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input'
      driver.find_element_by_xpath(form_date_xpath).send_keys(today)

      #出席番号
      form_student_num_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
      driver.find_element_by_xpath(form_student_num_xpath).send_keys(str(10))

      #名前
      form_name_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
      driver.find_element_by_xpath(form_name_xpath).send_keys("加納 源基")

      #体温
      form_temperature_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[2]/label'
      driver.find_element_by_xpath(form_temperature_xpath).click()

      #体調
      form_condition_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[5]/div[1]'
      driver.find_element_by_xpath(form_condition_xpath).click()

      #どこで授業を受けているか
      form_place_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[2]/label'
      driver.find_element_by_xpath(form_place_xpath).click()

      #送信
      form_submit_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span'
      driver.find_element_by_xpath(form_submit_xpath).click()

      print("送信完了")

def login(driver, login_id_xpath, login_pw_xpath):
  driver.find_element_by_name("identifier").send_keys(EMAIL)
  time.sleep(2)
  driver.find_element_by_xpath(login_id_xpath).click()
  time.sleep(5)
  driver.find_element_by_name("password").send_keys(PASSWORD)
  time.sleep(2)
  driver.find_element_by_xpath(login_pw_xpath).click()
  print("ロード中")
  time.sleep(25)

if __name__ == "__main__":
    main()
