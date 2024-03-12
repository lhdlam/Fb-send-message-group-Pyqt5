from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os
import pandas as pd
import shutil
from concurrent.futures import ThreadPoolExecutor
from selenium.webdriver.common.keys import Keys


def delete_folder(folder_path):
    try:
        shutil.rmtree(folder_path)
        print(f"Folder '{folder_path}' deleted successfully.")
    except OSError as e:
        print(f"Not Found: {e}")

def set_cookie_script(cookie_value):
    script = f"""
        function setCookie(cookie) {{
            var list = cookie.split("; ");
            for (var i = list.length - 1; i >= 0; i--) {{
                var [cname, cvalue] = list[i].split("=");
                var d = new Date();
                d.setTime(d.getTime() + (7 * 24 * 60 * 60 * 1000));
                var expires = ";domain=.mbasic.facebook.com;expires=" + d.toUTCString();
                document.cookie = cname + "=" + cvalue + "; " + expires;
            }}
        }}

        function hex2a(hex) {{
            var str = '';
            for (var i = 0; i < hex.length; i += 2) {{
                var v = parseInt(hex.substr(i, 2), 16);
                if (v) str += String.fromCharCode(v);
            }}
            return str;
        }}

        setCookie("{cookie_value}");
        location.href = 'https://mbasic.facebook.com';
    """
    return script

def send_friend_request(browser, profile_id):


    try:
        full_xpath = '/html/body/div/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr/td[1]/a'
        add_friend = browser.find_element(By.XPATH, full_xpath)
        add_friend.click()
        print(f"Done id={profile_id}")
    except:
        print(f"Element not found for id={profile_id}. Skipping...")

            

def process_profile(index, cookies, list_id, id_fbs, passwords):
    for index, id_fb in enumerate(id_fbs):
        path_data_fb = 'facebook'

        # Delete data chrome
        delete_folder(path_data_fb)
        sleep(1)
        current_directory = os.getcwd()
        user_data_directory = os.path.join(current_directory, 'facebook', f'profile{id_fb}')

        # Set up Chrome options
        options = webdriver.ChromeOptions()
        options.add_argument(f'user-data-dir={user_data_directory}')
        options.add_argument('--mute-audio')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        # Create Chrome WebDriver
        browser = webdriver.Chrome(options=options)
        browser.set_window_size(800, 1200)
        # Log in with cookie
        browser.get("https://mbasic.facebook.com/")
        sleep(3)
        script_set_cookie = set_cookie_script(cookies[index])
        browser.execute_script(script_set_cookie)
        sleep(2)
        full_xpath_login = '/html/body/div/div/div[2]/div/table/tbody/tr/td/div[2]/div/div[2]/form/ul/li[3]/input'
        btn_login = browser.find_element(By.XPATH, full_xpath_login)
        if btn_login:
            cvt_id = str(id_fb)
            id_login = cvt_id.split('|')[0]
            
            full_xpath_username = '/html/body/div/div/div[2]/div/table/tbody/tr/td/div[2]/div/div[2]/form/ul/li[1]/input'
            find_username = browser.find_element(By.XPATH, full_xpath_username)
            find_username.send_keys(id_login)
            
            full_xpath_pass = '/html/body/div/div/div[2]/div/table/tbody/tr/td/div[2]/div/div[2]/form/ul/li[2]/section/input'
            find_pass = browser.find_element(By.XPATH, full_xpath_pass)  
            find_pass.send_keys(passwords[index])
            
            btn_login.click()
            sleep(1)
#/html/body/div/div/div[2]/div/form/div[1]/article/div[2]/table/tbody/tr/td/input
#/html/body/div/div/div[2]/div/form/div[1]/article/div[2]/table/tbody/tr/td/input
#/html/body/div/div/div[2]/div/form/div[1]/article/div[2]/table/tbody/tr/td/input
        # Send friend requests
        for profile_id in list_id:
            if len(str(profile_id)) == 15:
                browser.get(f"https://mbasic.facebook.com/profile.php?id={profile_id}")
            else:
                browser.get(f"https://mbasic.facebook.com/{profile_id}")
            sleep(2)
            send_friend_request(browser, profile_id)

    # Close the browser
    browser.quit()
def main(excel_id_friend, excel_cookie, threads):

    # Get data excel
    excel_id_friend = 'list_friend.ods'
    excel_cookie = '10Lam.xlsx'

    df_list_friend = pd.read_excel(excel_id_friend)
    global list_id
    list_id_friend = df_list_friend['id'].tolist()

    df_list_cookie = pd.read_excel(excel_cookie)
    list_id_fb = df_list_cookie.iloc[:, 0].tolist()
    list_password = df_list_cookie.iloc[:, 1].tolist()
    list_cookie = df_list_cookie.iloc[:, 2].tolist()
    
    total_cookies = len(list_cookie)
    threads = 3
    
    # Calculate a balanced chunk size
    chunk_size = total_cookies // threads

    # Divide the list into chunks
    chunks = [list_cookie[i:i + chunk_size] for i in range(0, total_cookies, chunk_size)]

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [
            executor.submit(
                process_profile,
                index,
                chunk,
                list_id_friend,
                list_id_fb[index * chunk_size:(index + 1) * chunk_size],
                list_password[index * chunk_size:(index + 1) * chunk_size]
            )
            for index, chunk in enumerate(chunks)
        ]

        for future in futures:
            future.result()

if __name__ == "__main__":

    excel_id_friend = 'list_friend.ods'
    excel_cookie = '10Lam.xlsx'
    threads = 5
    main(excel_id_friend, excel_cookie, threads)
