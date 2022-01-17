import datetime

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import conftest
from src import steps


def registration(driver):
    timestamp = datetime.datetime.now().strftime('%m_%d_%Y_%H_%M_%S')
    env = conftest.STAGE_B2C
    browser = driver.session_id

    try:
        steps.logout(driver, env, browser)
    except:
        pass

    driver.get(env)

    try:

        steps.click_it(driver, browser,
                       driver.find_element_by_class_name('first-section_buttons').find_element_by_xpath(
                           'button'),
                       'Click on "Get Started Today" Button on Onboarding modal.')

        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "button"))).click()

        steps.assessment(driver, browser, 'Complete onboarding assessment')

        username = conftest.USERNAME + '_lvtest_' + timestamp
        steps.fill_the_field(driver, browser, username, driver.find_element_by_name('username'),
                             'Fill "Username" field.')

        email = conftest.USERNAME + '+lvtest_chrome_' + timestamp + conftest.FAKE_MAIL
        steps.fill_the_field(driver, browser, email, driver.find_element_by_name('email'),
                             'Fill "E-Mail" field.')

        steps.fill_the_field(driver, browser, conftest.PASSWORD, driver.find_element_by_name('password'),
                             'Fill "Password" field.')

        steps.fill_the_field(driver, browser, conftest.PASSWORD, driver.find_element_by_name('cpassword'),
                             'Fill "Confirm Password" field.')

        steps.click_it_java(driver, browser, driver.find_element_by_id('tos_checkbox'),
                            'Enable "I agree to Happify\'s Terms and Conditions and Privacy Policy" checkbox.')

        steps.click_it(driver, browser,
                       driver.find_element_by_class_name('signup').find_element_by_class_name('button'),
                       'Click on "Continue" Button on Sign Up modal.')

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "private_text")))
        steps.click_it(driver, browser, driver.find_element_by_id('private_text'),
                       'Choosing \"Private mode\".')

        steps.click_it(driver, browser,
                       driver.find_element_by_class_name('button-section').find_element_by_class_name(
                           'button'), 'Click on "Continue" Button on Choose Your Privacy Settings modal.')

        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.LINK_TEXT, 'See our full list of tracks')))
        steps.click_it(driver, browser, driver.find_element_by_link_text('See our full list of tracks'),
                       'Click on "See all tracks."')

        steps.click_it(driver, browser,
                       driver.find_elements_by_class_name('slide-header')[0].find_element_by_xpath('button'),
                       'Clicking on "Forward" element')

        steps.click_it(driver, browser,
                       driver.find_elements_by_class_name('slide-header')[1].find_element_by_xpath(
                           'button[2]'), 'Clicking on "Forward" element')

        steps.click_it(driver, browser, driver.find_element_by_class_name('finish'),
                       'Clicking on "Finish" element')

        end_flag = False
        if driver.current_url.find('explore_tracks') > 0:
            driver.save_screenshot('success_' + browser + '.png')
            end_flag = True

        if not steps.turn_off_email_notifications(driver, browser):
            raise Exception('Error occurred while turning off E-Mail notifications')

        if not steps.logout(driver, env, browser):
            raise Exception('Error occurred while Log out.')

        if end_flag:
            steps.end_successful_after_another_actions(browser, 'Explore Tracks page presented.')
            assert True

    except TimeoutError:
        steps.end_fail(driver, browser, 'No element was found after awaiting.')
        assert False

    except NoSuchElementException as e:
        steps.end_fail(driver, browser, str(e))
        assert False

    except Exception as e:
        steps.end_fail(driver, browser, str(e))
        assert False
