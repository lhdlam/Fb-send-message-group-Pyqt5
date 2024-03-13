# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QVBoxLayout, QTableWidgetItem, QPushButton, QListWidgetItem
from PyQt5.QtCore import QThread, pyqtSignal
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from time import sleep
import os
import pandas as pd
import shutil
# from fb_tool_ui import Ui_Form
from msg import Ui_Form
from datetime import datetime
import random
import string
import sys
import random
import numpy as np


if sys.stdout is not None:
    sys.stdout.reconfigure(encoding='utf-8')

class WorkerThread(QThread):
    result_signal = pyqtSignal(str, str, str, str, str, name="workerThreadResult")
    done_signal = pyqtSignal()

    def __init__(self, cookies, ids, passwords, parent=None):
        super(WorkerThread, self).__init__(parent)
        self.cookies = cookies
        self.ids = ids
        self.passwords = passwords
        self.stopped = False

    def run(self):
        for cookie, user_id, password in zip(self.cookies, self.ids, self.passwords):
            if self.stopped:
                break
            try:
                status = self.check_live_cookie(cookie)
            except:
                status = 'Skip'
            if status=='Live':
                result_status = "Done"
            else:
                result_status = 'Skip...'

            self.browser.quit()
            sleep(generate_random_float(1.0,1.5))
            # Delete data chrome
            path_data_fb_delete = os.path.join(self.current_directory, 'facebook', 'profile{}'.format(self.sanitized_id_fb))
            self.delete_folder(path_data_fb_delete)
            # Convert user_id and password to strings before emitting the signal
            user_id_str = str(user_id)
            password_str = str(password)

            self.result_signal.emit(user_id_str, password_str, cookie, status, result_status)
        self.done_signal.emit()
        
    def generate_random_string(self, length=8):
        characters = string.ascii_letters + string.digits  # Ký tự chữ cái và số
        random_string = ''.join(random.choice(characters) for _ in range(length))
        return random_string

    def extract_specific_cookies(self, input_cookie, desired_cookies):
        cookie_elements = input_cookie.split(';')
        extracted_cookies = [element.strip() for element in cookie_elements if any(cookie in element for cookie in desired_cookies)]
        result_cookie = '; '.join(extracted_cookies) + ';'

        return result_cookie

    def set_cookie_script(self, cookie_value):
        desired_cookies = ['datr', 'c_user', 'xs', 'fr']
        cookie_modified = self.extract_specific_cookies(cookie_value, desired_cookies)
        
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

    def delete_folder(self, folder_path):
        print(f"Deleting folder: {folder_path}")
        try:
            shutil.rmtree(folder_path)
            print(f"Folder '{folder_path}' deleted successfully.")
        except OSError as e:
            print(f"Error deleting folder '{folder_path}': {e}")

    def check_live_cookie(self, cookie):

        path_data_fb = 'facebook'

        # # Delete data chrome
        # self.delete_folder(path_data_fb)
        # sleep(generate_random_float(0.7,1.2))
        self.current_directory = os.getcwd()

        # Set up Chrome options
        cookie = str(cookie)
        self.sanitized_id_fb = self.generate_random_string()
        user_data_directory = os.path.abspath(os.path.join(self.current_directory, path_data_fb, f'profile{self.sanitized_id_fb}'))

        # Ensure parent directories exist
        os.makedirs(user_data_directory, exist_ok=True)

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')  # Disable GPU acceleration in headless mode
        options.add_argument(f'--user-data-dir={user_data_directory}')
        options.add_argument('--mute-audio')
        options.add_argument("--disable-notifications")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        

        # Create Chrome WebDriver without setting window size
        self.browser = webdriver.Chrome(options=options)
        self.browser.set_window_size(800, 1200)
        self.browser.get('https://www.facebook.com/')
        sleep(generate_random_float(0.7,1.2))
        script_set_cookie = self.set_cookie_script(cookie)
        self.browser.execute_script(script_set_cookie)
        sleep(generate_random_float(0.7,1.2))
        self.browser.execute_script(script_set_cookie)
        sleep(generate_random_float(0.7,1.2))
        try:
            xpath_check = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div[1]/div'
            check = self.browser.find_element(By.XPATH, xpath_check)
            if check:
                return 'Live'
        except:
                return 'Die'


class WorkerThread2(QThread):
    result_signal = pyqtSignal(list, name="workerThreadResult2")
    done_signal = pyqtSignal()

    def __init__(self, cookies, link_group, parent=None):
        super(WorkerThread2, self).__init__(parent)
        self.cookies = cookies
        self.link_group = link_group
        self.stopped = False

    def run(self):
        for cookie in zip(self.cookies):
            if self.stopped:
                break
            list_members = self.get_members_group(cookie, self.link_group)
            self.browser.quit()
            sleep(generate_random_float(0.7,1.2))
            # Delete data chrome
            path_data_fb_delete = os.path.join(self.current_directory, 'facebook', f'profile{self.sanitized_id_fb}')
            self.delete_folder(path_data_fb_delete)
            # Convert user_id and password to strings before emitting the signal

            self.result_signal.emit(list_members)
            break
        self.done_signal.emit()
             
        
    def generate_random_string(self, length=8):
        characters = string.ascii_letters + string.digits  # Ký tự chữ cái và số
        random_string = ''.join(random.choice(characters) for _ in range(length))
        return random_string

    def extract_specific_cookies(self, input_cookie, desired_cookies):
        cookie_elements = input_cookie.split(';')
        extracted_cookies = [element.strip() for element in cookie_elements if any(cookie in element for cookie in desired_cookies)]
        result_cookie = '; '.join(extracted_cookies) + ';'

        return result_cookie

    def set_cookie_script(self, cookie_value):
        desired_cookies = ['datr', 'c_user', 'xs', 'fr']
        cookie_modified = self.extract_specific_cookies(cookie_value, desired_cookies)
        
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

    def delete_folder(self, folder_path):
        print(f"Deleting folder: {folder_path}")
        try:
            shutil.rmtree(folder_path)
            print(f"Folder '{folder_path}' deleted successfully.")
        except OSError as e:
            print(f"Error deleting folder '{folder_path}': {e}")

    def get_members_group(self, cookie, link_group):

        path_data_fb = 'facebook'

        # # Delete data chrome
        # self.delete_folder(path_data_fb)
        # sleep(generate_random_float(0.7,1.2))
        self.current_directory = os.getcwd()

        # Set up Chrome options
        cookie = str(cookie)
        self.sanitized_id_fb = self.generate_random_string()
        user_data_directory = os.path.abspath(os.path.join(self.current_directory, path_data_fb, f'profile{self.sanitized_id_fb}'))

        # Ensure parent directories exist
        os.makedirs(user_data_directory, exist_ok=True)

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')  # Disable GPU acceleration in headless mode
        options.add_argument(f'--user-data-dir={user_data_directory}')
        options.add_argument('--mute-audio')
        options.add_argument("--disable-notifications")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        # Create Chrome WebDriver without setting window size
        self.browser = webdriver.Chrome(options=options)
        self.browser.set_window_size(800, 1200)
        self.browser.get('https://www.facebook.com/')
        sleep(generate_random_float(0.7,1.2))
        script_set_cookie = self.set_cookie_script(cookie)
        self.browser.execute_script(script_set_cookie)
        sleep(generate_random_float(0.7,1.2))
        if link_group[-1] == "/":
            path_group = link_group + 'members'
        else:
            path_group = link_group + '/members'
        self.browser.get(path_group)
        sleep(generate_random_float(1.5,2.2))
        for _ in range(40):  # Tùy thuộc vào kích thước nhóm, bạn có thể cần thay đổi số lần cuộn
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(generate_random_float(1.5,2.2))
        sleep(generate_random_float(2.0,2.9))

        # Tìm tất cả các phần tử theo XPath
        # elements = browser.find_elements(By.XPATH, '//div[@class="x1oo3vh0 x1rdy4ex"]')
        elements = WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'x1oo3vh0'))
        )
        # Lặp qua từng phần tử và thực hiện click vào đường dẫn cụ thể
        list_link = []
        for element in elements:
            element_html = element.get_attribute("innerHTML")
            sleep(generate_random_float(0.7,1.2))
            # Sử dụng BeautifulSoup để phân tích HTML
            soup = BeautifulSoup(element_html, 'html.parser')

            # Tìm tất cả các thẻ 'a' trong phần tử
            all_links = soup.find_all('a')

            # In tất cả các đường dẫn (href)
            for link in all_links:
                href_value = link.get('href')
                list_link.append(href_value)

        list_set = list(set(list_link))
        return list_set

class WorkerThread3(QThread):
    result_signal = pyqtSignal(int, name="workerThreadResult3")
    done_signal = pyqtSignal()

    def __init__(self, images,list_members,list_cookie, msg_value, parent=None):
        super(WorkerThread3, self).__init__(parent)
        self.images = images
        self.list_members = list_members
        self.list_cookie = list_cookie
        self.msg_value = msg_value

        self.stopped = False

    def run(self):
        # chia list member truoc khi truyen vao cho moi cookie xu ly
        list_member_new  = np.array_split(self.list_members,len(self.list_cookie))
        ##########
        for index, cookie in enumerate(self.list_cookie):
            if self.stopped:
                break
            # list_member_divide = list_member[index:index+]
            conver_list_member = list_member_new[index].tolist()
            run_send_msg = self.send_msg(cookie, conver_list_member, self.images, self.msg_value)
            sleep(generate_random_float(0.7,1.2))
            self.browser.quit()
            sleep(generate_random_float(0.7,1.2))
            # Delete data chrome
            path_data_fb_delete = os.path.join(self.current_directory, 'facebook', f'profile{self.sanitized_id_fb}')
            self.delete_folder(path_data_fb_delete)
            sleep(generate_random_float(0.7,1.2))
            
        self.done_signal.emit()
        
    def generate_random_string(self, length=8):
        characters = string.ascii_letters + string.digits  # Ký tự chữ cái và số
        random_string = ''.join(random.choice(characters) for _ in range(length))
        return random_string

    def extract_specific_cookies(self, input_cookie, desired_cookies):
        cookie_elements = input_cookie.split(';')
        extracted_cookies = [element.strip() for element in cookie_elements if any(cookie in element for cookie in desired_cookies)]
        result_cookie = '; '.join(extracted_cookies) + ';'

        return result_cookie

    def set_cookie_script(self, cookie_value):
        desired_cookies = ['datr', 'c_user', 'xs', 'fr']
        cookie_modified = self.extract_specific_cookies(cookie_value, desired_cookies)
        
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

    def delete_folder(self, folder_path):
        print(f"Deleting folder: {folder_path}")
        try:
            shutil.rmtree(folder_path)
            print(f"Folder '{folder_path}' deleted successfully.")
        except OSError as e:
            print(f"Error deleting folder '{folder_path}': {e}")


    def send_msg(self,cookie, list_members, images, msg_value):
        path_data_fb = 'facebook'
        # # Delete data chrome
        # self.delete_folder(path_data_fb)
        # sleep(generate_random_float(0.7,1.2))
        self.current_directory = os.getcwd()

        # Set up Chrome options
        cookie = str(cookie)
        self.sanitized_id_fb = self.generate_random_string()
        user_data_directory = os.path.abspath(os.path.join(self.current_directory, path_data_fb, f'profile{self.sanitized_id_fb}'))

        # Ensure parent directories exist
        os.makedirs(user_data_directory, exist_ok=True)

        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        # options.add_argument('--disable-gpu')  # Disable GPU acceleration in headless mode
        options.add_argument(f'--user-data-dir={user_data_directory}')
        options.add_argument('--mute-audio')
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-unicode")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        

        # Create Chrome WebDriver without setting window size
        self.browser = webdriver.Chrome(options=options)
        self.browser.set_window_size(800, 1200)
        self.browser.get('https://www.facebook.com/')
        sleep(generate_random_float(0.5,1.2))
        script_set_cookie = self.set_cookie_script(cookie)
        self.browser.execute_script(script_set_cookie)
        sleep(generate_random_float(0.5,1.2))
        for member in list_members:
            path_member = 'https://www.facebook.com' + member
            self.browser.get(path_member)
            sleep(generate_random_float(2.0,3.9))
            try:
                # add friend
                friend_path = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div/div"
                add_fr = self.browser.find_element(By.XPATH, friend_path)
                add_fr.click()
            except:
                pass
            try:
                sleep(generate_random_float(1.0,2.9))
                xpath_msg = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div[1]/div[2]/div/div/div/div[4]/div/div/div[1]/div/div/div'
                # xpath_msg = "//div[@aria-label='Nhắn tin']"
                check_msg = self.browser.find_element(By.XPATH, xpath_msg)
                check_msg.click()
                sleep(generate_random_float(4.0,6.5))
                if len(images)!=0:
                    xpath_image = "//input[@type='file']"
                    add_friend = self.browser.find_element(By.XPATH, xpath_image)
                    sleep(generate_random_float(1.0,1.5))
                    add_friend.send_keys(images)
                # # Chọn ô nhập tin nhắn
                # message_input = driver.find_element_by_xpath("//div[@role='textbox']")
                if len(msg_value) != 0:
                    xpath_chat = "//div[@role='textbox']"
                    chat = self.browser.find_element(By.XPATH, xpath_chat)
                    # Gửi tin nhắn với ảnh
                    msg_array = msg_value.split('\n')
                    for msg in msg_array:
                        sleep(generate_random_float(1.0,1.9))
                        chat.send_keys(msg, Keys.ENTER)
                sleep(generate_random_float(1.0,1.9))                 
                print("Done")
                self.result_signal.emit(1)
            except Exception as e:
                print("Skip...")
                continue
        return "Done Send"

class AddFriendFacebook(QMainWindow):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.worker_thread = None 

        self.my_ui_control()
        self.current_directory = os.getcwd()
        path_folder = os.path.join(self.current_directory, 'facebook')
        self.delete_folder(path_folder)
        self.create_folder(path_folder)
        
        self.result = 0

    def create_folder(self, folder_path):
        try:
            # Create the folder
            os.makedirs(folder_path)
            print(f"Folder '{folder_path}' has been created.")

        except Exception as e:
            print(f"An error occurred: {e}")

    def delete_folder(self, folder_path):
        print(f"Deleting folder: {folder_path}")
        try:
            shutil.rmtree(folder_path)
            print(f"Folder '{folder_path}' deleted successfully.")
        except OSError as e:
            print(f"Error deleting folder '{folder_path}': {e}")

    def my_ui_control(self):
        self.ui.lbl_cookie.setText('')
        self.ui.lbl_cookie_page.setText('')
        self.ui.lbl_notification.setText('')
        
        self.ui.tabWidget.setCurrentIndex(0)

        self.ui.btn_run.setEnabled(False)
        self.ui.btn_stop.setEnabled(False)
        self.ui.btn_export.setEnabled(False)


        self.ui.btn_cookie.clicked.connect(self.import_cookie)
        self.ui.btn_run.clicked.connect(self.run)

        self.ui.btn_stop.clicked.connect(self.stop_threads)
        self.ui.btn_export.clicked.connect(self.export_to_excel)


        self.ui.tableWidget.setColumnWidth(0, 175)
        self.ui.tableWidget.horizontalHeader().resizeSection(0, 175)  
        self.ui.tableWidget.setColumnWidth(1, 175)
        self.ui.tableWidget.horizontalHeader().resizeSection(1, 175) 
        self.ui.tableWidget.setColumnWidth(2, 175)
        self.ui.tableWidget.horizontalHeader().resizeSection(2, 175)  
        self.ui.tableWidget.setColumnWidth(3, 175)
        self.ui.tableWidget.horizontalHeader().resizeSection(3, 175) 
        self.ui.tableWidget.setColumnWidth(4, 175)
        self.ui.tableWidget.horizontalHeader().resizeSection(4, 175)

        #################################################################
        self.ui.lbl_notification_page.setText('')
        self.ui.btn_cookie_page.clicked.connect(self.import_cookie_page)
        self.ui.btn_run_page.clicked.connect(self.run_page)
        self.ui.btn_export_page.clicked.connect(self.export_to_excel_page)
        self.ui.tableWidget_page.setColumnWidth(0, 400)
        self.ui.tableWidget_page.horizontalHeader().resizeSection(0, 400) 


        #################################################################
        self.ui.btn_import_list_member.clicked.connect(self.import_members)
        self.ui.btn_image.clicked.connect(self.import_image) 
        self.ui.btn_import_cookie.clicked.connect(self.import_cookie_msg) 
        self.ui.btn_run_msg.clicked.connect(self.run_msg) 
        self.ui.btn_stop_msg.clicked.connect(self.stop_msg)

        self.ui.lbl_notification_msg.setText('')
        self.ui.lbl_members_link.setText('')
        self.ui.lbl_cookie_link.setText('')
        self.ui.lbl_images_msg.setText('')
        self.ui.txt_msg.setText('')


        self.ui.btn_run_msg.setEnabled(False)
        self.ui.btn_stop_msg.setEnabled(False)


    def import_members(self):
        self.file_path_members, _ = QFileDialog.getOpenFileName(None, "Select ID FB File", "", "Text Files (*.ods *.xlsx *.xls);;All Files (*)")
        if self.file_path_members:
            self.ui.lbl_members_link.setText(self.file_path_members)

    def import_image(self):
        self.file_path_images, _ = QFileDialog.getOpenFileName(None, "Select Image Files", "", "Image Files (*.jpg *.png);;All Files (*)")
        if self.file_path_images:
            self.ui.lbl_images_msg.setText(self.file_path_images)

    def import_cookie_msg(self):
        self.file_path_cookie_msg, _ = QFileDialog.getOpenFileName(None, "Select ID FB File", "", "Text Files (*.ods *.xlsx *.xls);;All Files (*)")
        if self.file_path_cookie_msg:
            self.ui.lbl_cookie_link.setText(self.file_path_cookie_msg)
            self.ui.btn_run_msg.setEnabled(True)
            self.ui.btn_stop_msg.setEnabled(True)

    def run_msg(self):
        try:
            # self.ui.btn_stop.setEnabled(True)
            # self.ui.btn_export.setEnabled(True)
            self.ui.lbl_notification.setText('Running')
            # self.ui.tableWidget.setRowCount(0)  
            df_list_members = pd.read_excel(self.file_path_members)
            # global list_id_friend
            self.list_members = df_list_members.iloc[:, 0].tolist()

            df_list_cookie = pd.read_excel(self.file_path_cookie_msg)
            # self.list_id_fb = df_list_cookie.iloc[:, 0].tolist()
            # self.list_password = df_list_cookie.iloc[:, 1].tolist()
            self.list_cookie = df_list_cookie.iloc[:, 2].tolist()

            msg_value = self.ui.txt_msg.toPlainText()

                
            number_tab = self.ui.txt_thread_msg.text()
            if len(number_tab) == 0:
                self.ui.lbl_notification_msg.setText("Please enter Thread !!!")
            else:
                if len(msg_value) == 0:
                    self.ui.lbl_notification_msg.setText("Please enter message !!!")
            if len(number_tab) != 0 and len(msg_value) != 0:
                self.ui.lbl_notification_msg.setText("Running...")
                thread = int(number_tab)
                list_member_conver = np.array_split(self.list_members, thread)
                list_cookie_conver = np.array_split(self.list_cookie, thread)

                chunks = [
                    (
                        self.file_path_images,
                        list_member_conver[i].tolist(),
                        list_cookie_conver[i].tolist(),
                        msg_value
                    )
                    for i in range(0, thread)
                ]

                self.worker_threads = []
                for chunk in chunks:
                    worker_thread = WorkerThread3(*chunk)
                    worker_thread.result_signal.connect(self.on_thread_result_msg)
                    worker_thread.done_signal.connect(self.on_thread_done_3)
                    self.worker_threads.append(worker_thread)
                    worker_thread.start()
                    # Check if the license key is still valid
                    expiration_date_str = "16/03/2024"
                    if self.is_license_key_valid(expiration_date_str):
                        # Key is valid
                        print("License key is still valid.")
                    else:
                        # Key has expired
                        print("License key has expired.")
                        self.ui.lbl_notification.setText('License key has expired...')
        except:
            self.ui.lbl_notification.setText('Error: Check input !!!')

    def stop_msg(self):
        for worker_thread in self.worker_threads:
            worker_thread.terminate()

        for worker_thread in self.worker_threads:
            worker_thread.wait()

        self.worker_threads = []

    def export_to_excel(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Excel Files (*.xlsx);;All Files (*)", options=options)

        if file_name:
            # Lấy header từ QTableWidget
            headers = []
            for column in range(self.ui.tableWidget.columnCount()):
                header_item = self.ui.tableWidget.horizontalHeaderItem(column)
                headers.append(header_item.text() if header_item else f'Column {column + 1}')

            # Lấy dữ liệu từ QTableWidget
            data = [headers]
            for row in range(self.ui.tableWidget.rowCount()):
                row_data = []
                for column in range(self.ui.tableWidget.columnCount()):
                    item = self.ui.tableWidget.item(row, column)
                    if item is not None:
                        row_data.append(item.text())
                    else:
                        row_data.append('')
                data.append(row_data)

            df = pd.DataFrame(data)

            df.to_excel(file_name, index=False, header=False)


    def export_to_excel_page(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Excel Files (*.xlsx);;All Files (*)", options=options)

        if file_name:
            # Lấy header từ QTableWidget
            headers = []
            for column in range(self.ui.tableWidget_page.columnCount()):
                header_item = self.ui.tableWidget_page.horizontalHeaderItem(column)
                headers.append(header_item.text() if header_item else f'Column {column + 1}')

            # Lấy dữ liệu từ QTableWidget
            data = [headers]
            for row in range(self.ui.tableWidget_page.rowCount()):
                row_data = []
                for column in range(self.ui.tableWidget_page.columnCount()):
                    item = self.ui.tableWidget_page.item(row, column)
                    if item is not None:
                        row_data.append(item.text())
                    else:
                        row_data.append('')
                data.append(row_data)

            df = pd.DataFrame(data)

            df.to_excel(file_name, index=False, header=False)

    def import_cookie(self):
        self.file_path_cookie, _ = QFileDialog.getOpenFileName(None, "Select Cookie File", "", "Text Files (*.ods *.xlsx *.xls);;All Files (*)")
        if self.file_path_cookie:
            self.ui.lbl_cookie.setText(self.file_path_cookie)
        self.ui.btn_run.setEnabled(True)

    def import_cookie_page(self):
        self.file_path_cookie_page, _ = QFileDialog.getOpenFileName(None, "Select ID FB File", "", "Text Files (*.ods *.xlsx *.xls);;All Files (*)")
        if self.file_path_cookie_page:
            self.ui.lbl_cookie_page.setText(self.file_path_cookie_page)

    def is_license_key_valid(self, expiration_date_str):
        expiration_date = datetime.strptime(expiration_date_str, "%d/%m/%Y")
        current_time = datetime.now()
        return current_time < expiration_date



    def run(self):
        try:
            if len(self.file_path_cookie) ==0:
                self.ui.lbl_notification.setText('Please import account!')
            if len(self.ui.txt_thread.text()) ==0:
                self.ui.lbl_notification.setText('Please enter number tab!')
                
            if len(self.file_path_cookie) !=0 and len(self.ui.txt_thread.text()) !=0:
                self.ui.btn_stop.setEnabled(True)
                self.ui.btn_export.setEnabled(True)
                self.ui.lbl_notification.setText('Running...')
                # df_list_friend = pd.read_excel(self.file_path_id)
                # global list_id_friend
                # list_id_friend = df_list_friend.iloc[:, 0].tolist()

                df_list_cookie = pd.read_excel(self.file_path_cookie)
                self.list_id_fb = df_list_cookie.iloc[:, 0].tolist()
                self.list_password = df_list_cookie.iloc[:, 1].tolist()
                self.list_cookie = df_list_cookie.iloc[:, 2].tolist()

                self.ui.tableWidget.setRowCount(0) 

                number_tab = self.ui.txt_thread.text()
                thread = int(number_tab)
                list_cookies_convert = np.array_split(self.list_cookie, thread)
                ist_id_fb_convert = np.array_split(self.list_id_fb, thread)
                list_password_convert = np.array_split(self.list_password, thread)
                chunks = [
                    (
                        list_cookies_convert[i].tolist(),
                        ist_id_fb_convert[i].tolist(),
                        list_password_convert[i].tolist()
                    )
                    for i in range(0, thread)
                ]

                self.worker_threads = []
                for chunk in chunks:
                    worker_thread = WorkerThread(*chunk)
                    worker_thread.result_signal.connect(self.on_thread_result)
                    worker_thread.done_signal.connect(self.on_thread_done)
                    self.worker_threads.append(worker_thread)
                    worker_thread.start()
                    # Check if the license key is still valid
                    expiration_date_str = "16/03/2024"
                    if self.is_license_key_valid(expiration_date_str):
                        # Key is valid
                        print("License key is still valid.")
                    else:
                        # Key has expired
                        print("License key has expired.")
                        self.ui.lbl_notification.setText('License key has expired...')
        except:
            self.ui.lbl_notification.setText('Error: Check input !!!')


    def run_page(self):
        try:
            if len(self.file_path_cookie_page) ==0:
                self.ui.lbl_notification_page.setText('Please import account!')
            if len(self.ui.txt_group_page.toPlainText()) ==0:
                self.ui.lbl_notification_page.setText('Please enter link group!')
            if len(self.file_path_cookie_page) !=0 and len(self.ui.txt_group_page.toPlainText()) !=0:
                self.ui.btn_stop_page.setEnabled(True)
                self.ui.btn_export_page.setEnabled(True)
                self.ui.lbl_notification_page.setText('Running')
                self.ui.tableWidget_page.setRowCount(0)  

                df_list_cookie = pd.read_excel(self.file_path_cookie_page)
                self.list_cookie = df_list_cookie.iloc[:, 2].tolist()
                link_group = self.ui.txt_group_page.toPlainText()
                if "?" in link_group:
                    link_group = link_group.split("?")[0]

                self.ui.tableWidget.setRowCount(0) 

                chunk_size = len(self.list_cookie) // 1
                chunks = [
                    (
                        self.list_cookie[i:i + chunk_size],
                        link_group,
                    )
                    for i in range(0, len(self.list_cookie), chunk_size)
                ]

                self.worker_threads = []
                for chunk in chunks:
                    worker_thread = WorkerThread2(*chunk)
                    worker_thread.result_signal.connect(self.on_thread_result_page)
                    worker_thread.done_signal.connect(self.on_thread_done_2)
                    self.worker_threads.append(worker_thread)
                    worker_thread.start()
                    # Check if the license key is still valid
                    expiration_date_str = "16/03/2024"
                    if self.is_license_key_valid(expiration_date_str):
                        # Key is valid
                        print("License key is still valid.")
                    else:
                        # Key has expired
                        print("License key has expired.")
                        self.ui.lbl_notification.setText('License key has expired...')
        except:
            self.ui.lbl_notification.setText('Error: Check input !!!')
            
    def on_thread_done(self):
        # self.stop_threads()
        # self.ui.lbl_notification.setText('Done')
        if all(thread.isFinished() for thread in self.worker_threads):
                    print("All threads are done.")
                    self.ui.lbl_notification.setText('Done')

    def on_thread_done_2(self):
        # self.stop_threads()
        # self.ui.lbl_notification_page.setText('Done')
        if all(thread.isFinished() for thread in self.worker_threads):
                    print("All threads are done.")
                    self.ui.lbl_notification_page.setText('Done')


    def on_thread_done_3(self):
        # self.stop_threads()
        self.ui.lbl_notification_msg.setText("Sending {} message".format(self.result))
        if all(thread.isFinished() for thread in self.worker_threads):
                    print("All threads are done.")
                    # Add any additional actions to perform when all threads are done
                    self.ui.lbl_notification_msg.setText("Done send {} message".format(self.result))

    def stop_threads(self):
        for worker_thread in self.worker_threads:
            worker_thread.terminate()

        for worker_thread in self.worker_threads:
            worker_thread.wait()

        self.worker_threads = []
        self.ui.lbl_notification_msg.setText("Done send {} message".format(self.result))

    def on_thread_result(self, id, password, cookie, status, result_status):
        row_position = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row_position)
        self.ui.tableWidget.setItem(row_position, 0, QTableWidgetItem(str(id)))
        self.ui.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(password)))
        self.ui.tableWidget.setItem(row_position, 2, QTableWidgetItem(str(cookie)))
        self.ui.tableWidget.setItem(row_position, 3, QTableWidgetItem(status))
        self.ui.tableWidget.setItem(row_position, 4, QTableWidgetItem(result_status))


    def on_thread_result_page(self, list_members):
        for row_position, link_member in enumerate(list_members):
            # row_position = self.ui.tableWidget.rowCount()
            self.ui.tableWidget_page.insertRow(row_position)
            self.ui.tableWidget_page.setItem(row_position, 0, QTableWidgetItem(link_member))
        # len_menbers = len(list_members)

    def on_thread_result_msg(self, count):
        self.result += count

def generate_random_float(a, b):
    return random.uniform(a, b)   

def chunk_list(input_list, chunk_size):
    return [input_list[i:i + chunk_size] for i in range(0, len(input_list), chunk_size)]

def format_folder(folder_path):
    try:
        # Check if the folder exists
        if os.path.exists(folder_path):
            # If the folder exists, remove all its contents
            for item in os.listdir(folder_path):
                item_path = os.path.join(folder_path, item)
                if os.path.isfile(item_path):
                    os.remove(item_path)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
            print(f"Folder '{folder_path}' has been cleaned.")

        else:
            # If the folder doesn't exist, create it
            os.makedirs(folder_path)
            print(f"Folder '{folder_path}' has been created.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cmt_facebook = AddFriendFacebook()
    cmt_facebook.show()
    sys.exit(app.exec_())
