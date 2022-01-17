import os
import time

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@allure.step('Performing action: {3}')
def click_it(driver, browser, element, action):
    element.click()
    driver.get_screenshot_as_png()
    driver.save_screenshot('click_it_' + browser + '.png')
    allure.attach.file('click_it_' + browser + '.png', attachment_type=allure.attachment_type.PNG)
    os.remove('click_it_' + browser + '.png')


@allure.step('Performing action (using Java-method): {3}')
def click_it_java(driver, browser, element, action):
    driver.execute_script("arguments[0].click();", element)
    driver.get_screenshot_as_png()
    driver.save_screenshot('click_it_java_' + browser + '.png')
    allure.attach.file('click_it_java_' + browser + '.png', attachment_type=allure.attachment_type.PNG)
    os.remove('click_it_java_' + browser + '.png')


@allure.step('Performing action: {4}')
def fill_the_field(driver, browser, data, element, action):
    element.send_keys(data)
    driver.get_screenshot_as_png()
    driver.save_screenshot('fill_the_field_' + browser + '.png')
    allure.attach.file('fill_the_field_' + browser + '.png', attachment_type=allure.attachment_type.PNG)
    os.remove('fill_the_field_' + browser + '.png')


@allure.step('Performing action: {2}')
def assessment(driver, browser, action):
    i = 3
    while True:
        try:
            try:
                WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "wa_slide_" + str(i))))
                i = i + 2
                time.sleep(2)
            except:
                break
            if driver.find_element_by_id('answer_0').is_displayed():
                driver.get_screenshot_as_png()
                driver.save_screenshot('choose_option_' + browser + '.png')
                allure.attach.file('choose_option_' + browser + '.png', attachment_type=allure.attachment_type.PNG)
                os.remove('choose_option_' + browser + '.png')
            driver.find_element_by_id('answer_0').click()
            try:
                driver.find_element_by_class_name('button_div').click()
            except:
                pass
        except Exception as e:
            if str(e).find('out of bounds of viewport') and driver.find_elements_by_class_name(
                    'spinner-container') != '':
                print('Spinner detected!')
                break


@allure.step('Turning off E-Mail notifications...')
def turn_off_email_notifications(driver, browser):
    driver.get('URL_GOES_HERE')
    driver.find_elements_by_tag_name('fieldset')[2].find_element_by_tag_name('button').click()
    driver.get_screenshot_as_png()
    driver.save_screenshot('turn_off_email_notifications_' + browser + '.png')
    allure.attach.file('turn_off_email_notifications_' + browser + '.png', attachment_type=allure.attachment_type.PNG)
    os.remove('turn_off_email_notifications_' + browser + '.png')
    if driver.find_element_by_class_name('flash-success').is_displayed():
        return True


@allure.step('Performing Log Out...')
def logout(driver, env, browser):
    driver.get(env)
    click_it(driver, browser, driver.find_element_by_class_name('sidenav-toggle'), 'Open Side menu using -burger-.')

    click_it(driver, browser, driver.find_element_by_id('userMenu'), 'Open User menu.')

    click_it(driver, browser, driver.find_element_by_id('userDropdownMenu').find_element_by_link_text('Log Out'),
             'Click "Logout" item in User menu.')
    driver.get_screenshot_as_png()
    driver.save_screenshot('log_out_from_account_' + browser + '.png')
    allure.attach.file('log_out_from_account_' + browser + '.png', attachment_type=allure.attachment_type.PNG)
    os.remove('log_out_from_account_' + browser + '.png')
    if driver.find_element_by_class_name('first-section').is_displayed():
        return True


@allure.step('Test complete successfully. Condition met: {2}.')
def end_successful(driver, browser, condition):
    driver.get_screenshot_as_png()
    driver.save_screenshot('success_' + browser + '.png')
    allure.attach.file('success_' + browser + '.png', attachment_type=allure.attachment_type.PNG)
    os.remove('success_' + browser + '.png')


@allure.step('Test complete successfully. Condition met: {1}.')
def end_successful_after_another_actions(browser, condition):
    allure.attach.file('success_' + browser + '.png', attachment_type=allure.attachment_type.PNG)
    os.remove('success_' + browser + '.png')


@allure.step('Test failure. {2}')
def end_fail(driver, browser, reason):
    driver.get_screenshot_as_png()
    driver.save_screenshot('fail_' + browser + '.png')
    allure.attach.file('fail_' + browser + '.png', attachment_type=allure.attachment_type.PNG)
    os.remove('fail_' + browser + '.png')
