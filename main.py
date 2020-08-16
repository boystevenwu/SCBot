from selenium import webdriver
import json
# Global Var: browser, info


def open_preferred(threads):
    """obtain url and thread name, call parse() to generate preferred threads,
       open threads in new windows and output addresses to the console"""

    with open('log.txt', 'r+') as f:
        read_threads = f.read()

        for thread in threads:  # iterate through threads and pass info to analyze
            card = thread.text.split('\n')
            item = parse(thread, card[2].split(' '), read_threads, f)
            if item:  # if the thread is selected
                browser.execute_script(f"window.open('{item}')")
                # to open the thread
                print(item)


def parse(thread, stats, read_list, f):
    """determine the quality of a thread and write url into log"""
    url = 'https://www.scboy.com/'+thread.get_attribute('data-href')

    if int(stats[0]) > info["Except"] \
            and (' ' + url) not in read_list:  # select high-viewed threads
        return url
    elif url not in read_list and int(stats[0]) > info["View"] \
            and (int(stats[1]) >= info["Reply"]
                 or int(stats[2]) >= info["Like"]
                 or int(stats[3]) >= info["Save"]):  # select based on general parameters
        f.write(url + '\n')
        return url
    elif "has_vip" in thread.get_attribute('outerHTML'):  # select where blue vip replies
        return url


def thread_reader():
    """read page info, execute command to open threads"""
    thread_body = browser.find_element_by_xpath(r'//ul[@class="list-unstyled threadlist mb-0"]')
    # main thread body
    thread_list = thread_body.find_elements_by_xpath(r'//li[@class="media thread tap  "]')
    # thread elements

    open_preferred(thread_list)


def login():
    """log into scboy"""

    userid = browser.find_element_by_id("mobile")
    userid.send_keys(info["Userid"])
    # enter the user id

    passwd = browser.find_element_by_id('password')
    passwd.send_keys(info["Passwd"])
    # enter the password

    button = browser.find_element_by_id('submit')
    button.click()
    # submit information


if __name__ == "__main__":
    with open('config.json') as j:
        info = json.load(j)
    browser = webdriver.Chrome()
    # load requirements config and chromedriver

    print("-- log in --")
    browser.get('https://www.scboy.com/?user-login.htm')
    login()
    print("-- Succeed --")
    # log in the site

    for page in range(1, info["Page"]+1):
        print(f"-- Page {page} --")
        browser.get(f'https://www.scboy.com/?forum-1-{page}.htm')
        thread_reader()
        # display threads from the given page

    browser.switch_to.window(browser.window_handles[0])
    browser.get('https://www.scboy.com/?forum-1-1.htm')
    # switch back to the main page and refresh
