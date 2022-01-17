from selenium.common.exceptions import NoSuchElementException

import conftest
from src import steps


def login(driver):
    env = conftest.STAGE_B2C
    browser = driver.session_id

    driver.implicitly_wait(10)

    try:
        steps.logout(driver, env, browser)
    except:
        pass

    driver.get(env)

    try:

        steps.click_it_java(driver, browser,
                            driver.find_element_by_class_name('first-section_buttons').find_element_by_xpath(
                                'a'),
                            'Click on Log In Button on Landing page.')

        steps.fill_the_field(driver, browser, conftest.EMAIL_PRESET, driver.find_element_by_id('email'),
                             'Entering E-Mail.')

        steps.fill_the_field(driver, browser, conftest.PASSWORD_PRESET,
                             driver.find_element_by_id('password'), 'Entering Password.')

        steps.click_it_java(driver, browser, driver.find_element_by_id('submit_in'),
                            'Click on Log In Button on Login page.')

        try:
            if driver.find_element_by_id('watson-assessment-intro'):
                steps.click_it(driver, browser, driver.find_element_by_class_name('button-close'),
                               'Remove Happiness CheckIn modal.')
        except:
            pass

        end_flag = False
        if driver.find_element_by_id('track_info_block').is_displayed():
            driver.save_screenshot('success_' + browser + '.png')
            end_flag = True

        if not steps.logout(driver, env, browser):
            raise Exception('Error occurred while Log out.')

        if end_flag:
            steps.end_successful(driver, browser, 'Track Info block appear')
            assert True
        else:
            steps.end_fail(driver, browser, 'No element was found after awaiting.')

    except TimeoutError:
        steps.end_fail(driver, browser, 'No element was found after awaiting.')
        assert False

    except NoSuchElementException as e:
        steps.end_fail(driver, browser, str(e))
        assert False

    except Exception as e:
        steps.end_fail(driver, browser, str(e))
        assert False
