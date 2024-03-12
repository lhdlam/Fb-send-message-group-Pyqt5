from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import os
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

sys.stdout.reconfigure(encoding='utf-8')

def set_cookie_script(cookie_value):
    desired_cookies = ['datr', 'c_user', 'xs', 'fr']
    cookie_modified = extract_specific_cookies(cookie_value, desired_cookies)
    
    script = f"""
        javascript:void(function() {{
            function setCookie(cookie) {{
                var list = cookie.split('; ');
                for (var i = list.length - 1; i >= 0; i--) {{
                    var cname = list[i].split('=')[0];
                    var cvalue = list[i].split('=')[1];
                    var d = new Date();
                    d.setTime(d.getTime() + (7 * 24 * 60 * 60 * 1000));
                    var expires = ';domain=.facebook.com;expires=' + d.toUTCString();
                    document.cookie = cname + '=' + cvalue + '; ' + expires;
                }}
            }}

            var cookieValue = '{cookie_modified}';
            setCookie(cookieValue);
            location.href = 'https://facebook.com';
        }})();
    """
    return script

def extract_specific_cookies(input_cookie, desired_cookies):
    cookie_elements = input_cookie.split(';')
    extracted_cookies = [element.strip() for element in cookie_elements if any(cookie in element for cookie in desired_cookies)]
    result_cookie = '; '.join(extracted_cookies) + ';'

    return result_cookie


path_data_fb = 'facebook'

# # Delete data chrome
# delete_folder(path_data_fb)
# sleep(1)
current_directory = os.getcwd()

user_data_directory = os.path.abspath(os.path.join(current_directory, path_data_fb, 'profile1234'))

# Ensure parent directories exist
# os.makedirs(user_data_directory, exist_ok=True)
options = webdriver.ChromeOptions()

# options.add_argument('--headless')
# options.add_argument('--disable-gpu')  # Disable GPU acceleration in headless mode
options.add_argument(f'--user-data-dir={user_data_directory}')
options.add_argument('--mute-audio')
options.add_argument("--disable-notifications")
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# Create Chrome WebDriver without setting window size
browser = webdriver.Chrome(options=options)
browser.set_window_size(800, 1000)
browser.get('https://www.facebook.com/')
sleep(1)
cookie_modified = "sb=YTfbZdO5D3UCz4HFojuY_K_n;wd=1055x867;datr=YTfbZQnDtpcWTApJXS_Y8gJE;ps_n=0;ps_l=0;locale=en_US;c_user=61556714790600;xs=11%3AqK25WDf1-9zH5w%3A2%3A1708865488%3A-1%3A-1;fr=0HPgXcxMghsJJwUxR.AWWGyvWenyKPgAgyhtWVJ7ZQf_w.Bl2zdh..AAA.0.0.Bl2zfS.AWWc6158b2E;presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1708865499255%2C%22v%22%3A1%7D;"
script = set_cookie_script(cookie_modified)
browser.execute_script(script)
sleep(2)

for i in range(1,2):    
    try:
        # browser.get("https://www.facebook.com/groups/539140943914264/members")
        browser.get("https://www.facebook.com/groups/539140943914264/user/100080300083301")
        sleep(1)
        # xpath_msg = '/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div[2]/div[1]/div[1]/div[2]/div/div/div/div[4]/div/div/div[1]/div/div/div'
        xpath_msg = "//div[@aria-label='Nhắn tin' or @aria-label='Message']"
        check_msg = browser.find_element(By.XPATH, xpath_msg)
        check_msg.click()
        sleep(1)
        # # Chọn ô nhập tin nhắn
        # message_input = driver.find_element_by_xpath("//div[@role='textbox']")
        xpath_chat = "//div[@role='textbox']"
        chat = browser.find_element(By.XPATH, xpath_chat)
        # Gửi tin nhắn với ảnh
        chat.send_keys("qweqweqweqweqwqweqwe")
        sleep(2)

        xpath_image = "//input[@type='file']"
        add_friend = browser.find_element(By.XPATH, xpath_image)
        add_friend.send_keys("C:\\Users\\ADMIN\\Pictures\\avt.png")
        sleep(1)
        add_friend.send_keys("C:\\Users\\ADMIN\\Pictures\\ac1.jpg")
        sleep(1)
        add_friend.send_keys("C:\\Users\\ADMIN\\Pictures\\logo.png")
        # Chờ ảnh được tải lên
        sleep(1000)

    except Exception as e:
        print("Error, Next...")
        print(e)
        continue

# browser.get("https://www.facebook.com/messages/t/100086370831883?locale=vi_VN")
# sleep(3)

# # # Chọn ô nhập tin nhắn
# # message_input = driver.find_element_by_xpath("//div[@role='textbox']")
# xpath_chat = "//div[@role='textbox']"
# chat = browser.find_element(By.XPATH, xpath_chat)
# # Gửi tin nhắn với ảnh
# chat.send_keys("qweqweqweqweqwqweqwe")
# sleep(2)

# xpath_image = "//input[@type='file']"
# add_friend = browser.find_element(By.XPATH, xpath_image)
# add_friend.send_keys("C:\\Users\\ADMIN\\Pictures\\avt.png")
# sleep(1)
# add_friend.send_keys("C:\\Users\\ADMIN\\Pictures\\ac1.jpg")
# sleep(1)
# add_friend.send_keys("C:\\Users\\ADMIN\\Pictures\\logo.png")
# Chờ ảnh được tải lên
time.sleep(10000)

# Đóng trình duyệt
browser.quit()
