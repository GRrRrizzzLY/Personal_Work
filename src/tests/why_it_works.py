from selenium.common.exceptions import NoSuchElementException

import conftest
from src import steps


def why_it_works(driver):
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

        steps.click_it(driver, browser, driver.find_element_by_link_text('Instant Play'),
                       'Click on Instant Play link in Top Menu.')

        steps.click_it(driver, browser, driver.find_element_by_class_name('slick-track'),
                       'Click on activity.')

        steps.click_it(driver, browser, driver.find_element_by_class_name('js-why-it-works'),
                       'Click on "Why it works?" link.')

        href = driver.find_elements_by_tag_name('sup')[0].find_element_by_tag_name('a').get_attribute('href')

        steps.click_it(driver, browser,
                       driver.find_elements_by_tag_name('sup')[0].find_element_by_tag_name('a'),
                       'Click on first link on new modal.')

        driver.switch_to.window(driver.window_handles[1])

        end_flag = False
        if driver.current_url == href:
            driver.save_screenshot('success_' + browser + '.png')
            end_flag = True

        if not steps.logout(driver, env, browser):
            raise Exception('Error occurred while Log out.')

        if end_flag:
            steps.end_successful_after_another_actions(browser,
                                                       'Link from "Why it works?" equals to opened web page link')
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
