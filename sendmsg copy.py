from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import os
from time import sleep
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import random
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

def generate_random_float(a, b):
    return random.uniform(a, b)

cookie_modified = "ps_l=0;ps_n=0;wd=1055x867;sb=73DbZUpOj5aYAzHqUsVUObs3;datr=73DbZWaXPrkRVYm3xZ2YS1hl;c_user=100085686515774;xs=1%3A18v5JgADQeDvnA%3A2%3A1708880244%3A-1%3A8991;fr=08VnPGtvvqszba69d.AWW9DjozG1wmwYUsrxXxZM5vkpI.Bl23Dv..AAA.0.0.Bl23F3.AWUQ53A2df4;presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1708880252301%2C%22v%22%3A1%7D;"

path_data_fb = 'facebook'

# # Delete data chrome
# delete_folder(path_data_fb)
# sleep(1)
current_directory = os.getcwd()

user_data_directory = os.path.abspath(os.path.join(current_directory, path_data_fb, 'profile111111'))

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
sleep(1)
browser.get('https://www.facebook.com/')
sleep(1)
script_set_cookie = set_cookie_script(cookie_modified)
browser.execute_script(script_set_cookie)
sleep(1)
# browser.execute_script(script_set_cookie)
# sleep(1)
# # browser.get('https://www.facebook.com/groups/539140943914264/members')
# # sleep(2)
# # for _ in range(30):  # Tùy thuộc vào kích thước nhóm, bạn có thể cần thay đổi số lần cuộn
# #     browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# #     time.sleep(2)

# # # Tìm tất cả các phần tử theo XPath
# # # elements = browser.find_elements(By.XPATH, '//div[@class="x1oo3vh0 x1rdy4ex"]')
# # elements = WebDriverWait(browser, 10).until(
# #     EC.presence_of_all_elements_located((By.CLASS_NAME, 'x1oo3vh0'))
# # )
# # print(elements)
# # # Lặp qua từng phần tử và thực hiện click vào đường dẫn cụ thể
# # list_link = []
# # for element in elements:
# #     try:
# #         element_html = element.get_attribute("innerHTML")
# #         # print(element_html)
# #         sleep(1)
# #         # Sử dụng BeautifulSoup để phân tích HTML
# #         soup = BeautifulSoup(element_html, 'html.parser')

# #         # Tìm tất cả các thẻ 'a' trong phần tử
# #         all_links = soup.find_all('a')

# #         # In tất cả các đường dẫn (href)
# #         for link in all_links:
# #             href_value = link.get('href')
# #             list_link.append(href_value)
# #     except Exception as e:
# #         print(f"Không thể thực hiện click: {e}")
# # print(list_link)
# list_set = list(set(list_link))
# print(list_set)
# print(len(list_set))
        # browser.get("https://www.facebook.com/groups/539140943914264/members")
browser.get("https://www.facebook.com/groups/539140943914264/user/100001879659433/")
sleep(1)
try:
    sleep(generate_random_float(1.0,1.9))
    xpath_msg = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div[1]/div[2]/div/div/div/div[4]/div/div/div[1]/div/div/div'
    # xpath_msg = "//div[@aria-label='Nhắn tin']"
    check_msg = browser.find_element(By.XPATH, xpath_msg)
    check_msg.click()
    sleep(generate_random_float(1.0,1.9))
    

    # sleep(generate_random_float(4.0,6.5))

    xpath_image = "//input[@type='file']"
    add_friend = browser.find_element(By.XPATH, xpath_image)
    sleep(generate_random_float(1.0,1.5))
    # print("list_images",list_images)
    add_friend.send_keys("C:\\Users\\ADMIN\\Downloads\\image.jpg")

    # # Chọn ô nhập tin nhắn
    # message_input = driver.find_element_by_xpath("//div[@role='textbox']")
    xpath_chat = "//div[@role='textbox']"
    chat = browser.find_element(By.XPATH, xpath_chat)
    
    # Gửi tin nhắn với ảnh
    chat.send_keys("Xin chào anh/chị", Keys.ENTER)
    sleep(generate_random_float(1.0,1.9))
    chat.send_keys("Giá chỉ 12K/1 trái, 14k/trái", Keys.ENTER)
    sleep(generate_random_float(1.0,1.9))
    chat.send_keys("Dừa xiêm đỏ nguyên chất bến tre", Keys.ENTER)
    sleep(generate_random_float(1.0,1.9))
    chat.send_keys("Dung tích nước trên 330ml", Keys.ENTER)
    """
    ⚠️ Xin chào anh/chị
    ▶️ Giá chỉ 12K/1 trái, 14k/trái
    ▶️ Dừa xiêm đỏ nguyên chất bến tre
    ▶️ Dung tích nước trên 330ml
    🌟Anh/chị đặt hàng cho em xin số điện thoại và địa chỉ để em lên đơn ạ.
    ✔️Phí ship 4k/km
    """

    # sleep(generate_random_float(4.0,6.5))

    # xpath_image = "//input[@type='file']"
    # add_friend = browser.find_element(By.XPATH, xpath_image)
    # sleep(generate_random_float(1.0,1.5))
    # # print("list_images",list_images)
    # add_friend.send_keys("C:\\Users\\ADMIN\\Downloads\\image.jpg")
    sleep(generate_random_float(1.0,2.5))
    # send_xpath = "/html/body/div[1]/div/div[1]/div/div[5]/div[1]/div[1]/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/span[2]/div"
    send_xpath = "/html/body/div[1]/div/div[1]/div/div[5]/div[1]/div[1]/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/span[2]/div"
    send_msg = browser.find_element(By.XPATH, send_xpath)
    # sleep(generate_random_float(1.0,1.5))
    send_msg.click()
    # Chờ ảnh được tải lên
    sleep(generate_random_float(0.5,1.2))
except Exception as e:
    print(e)
sleep(1000)

# Đóng trình duyệt sau khi hoàn thành
browser.quit()
sleep(100)

# Đóng trình duyệt
browser.quit()
