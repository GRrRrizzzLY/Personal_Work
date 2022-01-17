import pytest

from src.tests import login, logout, registration, resource_page, start_track, why_it_works


@pytest.mark.usefixtures("driver_init_1")
class ChromeTest:
    pass


class TestChrome(ChromeTest):

    @pytest.mark.smoke
    def test_login_2477_id(self):
        login.login(self.driver)

    def test_logout_263_id(self):
        logout.logout(self.driver)

    def test_registration_3579_id(self):
        registration.registration(self.driver)

    def test_resource_page_276_id(self):
        resource_page.resource_page(self.driver)

    def test_start_track_2345_id(self):
        start_track.start_track(self.driver)

    def test_why_it_works_3792_id(self):
        why_it_works.why_it_works(self.driver)


# TODO: check element visibility before taking screenshot
# TODO: check Assessment Flow - why it fail with spinner..?

'''
    def test_cs_assessment(self):

        timestamp = datetime.datetime.now().strftime('%m_%d_%Y_%H_%M_%S')
        env = conftest.STAGE_B2C
        browser = self.driver.session_id

        self.driver.get(env)

        try:

            steps.click_it(self.driver, browser,
                           self.driver.find_element_by_class_name('first-section_buttons').find_element_by_xpath(
                               'button'),
                           'Click on "Get Started Today" Button on Onboarding modal.')

            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "button"))).click()

            steps.assessment(self.driver, browser, 'Complete onboarding assessment')

            username = conftest.USERNAME + '_lvtest_chrome_' + timestamp
            steps.fill_the_field(self.driver, browser, username, self.driver.find_element_by_name('username'),
                                 'Fill "Username" field.')

            email = conftest.USERNAME + '+lvtest_' + timestamp + conftest.FAKE_MAIL
            steps.fill_the_field(self.driver, browser, email, self.driver.find_element_by_name('email'),
                                 'Fill "E-Mail" field.')

            steps.fill_the_field(self.driver, browser, conftest.PASSWORD, self.driver.find_element_by_name('password'),
                                 'Fill "Password" field.')

            steps.fill_the_field(self.driver, browser, conftest.PASSWORD, self.driver.find_element_by_name('cpassword'),
                                 'Fill "Confirm Password" field.')

            steps.click_it_java(self.driver, browser, self.driver.find_element_by_id('tos_checkbox'),
                                'Enable "I agree to Terms and Conditions and Privacy Policy" checkbox.')

            steps.click_it(self.driver, browser,
                           self.driver.find_element_by_class_name('signup').find_element_by_class_name('button'),
                           'Click on "Continue" Button on Sign Up modal.')

            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "private_text")))
            steps.click_it(self.driver, browser, self.driver.find_element_by_id('private_text'),
                           'Choosing \"Private mode\".')

            steps.click_it(self.driver, browser,
                           self.driver.find_element_by_class_name('button-section').find_element_by_class_name(
                               'button'), 'Click on "Continue" Button on Choose Your Privacy Settings modal.')

            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.LINK_TEXT, 'See our full list of tracks')))
            steps.click_it(self.driver, browser, self.driver.find_element_by_link_text('See our full list of tracks'),
                           'Click on "See all tracks."')

            steps.click_it(self.driver, browser,
                           self.driver.find_elements_by_class_name('slide-header')[0].find_element_by_xpath('button'),
                           'Clicking on "Forward" element.')

            steps.click_it(self.driver, browser,
                           self.driver.find_elements_by_class_name('slide-header')[1].find_element_by_xpath(
                               'button[2]'), 'Clicking on "Forward" element.')

            steps.click_it(self.driver, browser, self.driver.find_element_by_class_name('finish'),
                           'Clicking on "Finish" element.')

            steps.click_it(self.driver, browser, self.driver.find_element_by_class_name('action'),
                           'Clicking on first "Start Free Track" button.')

            steps.click_it(self.driver, browser, self.driver.find_element_by_link_text('My Stats'),
                           'Clicking on "My Stats" button in Top Navigation Menu.')

            steps.click_it(self.driver, browser, self.driver.find_elements_by_class_name('js-menu_item')[3],
                           'Clicking on "My Strengths" button.')

            steps.click_it(self.driver, browser,
                           self.driver.find_element_by_class_name('button-wrapper').find_element_by_tag_name('button'),
                           'Clicking on "Start assessment" button.')

            driver.find_elements_by_class_name('carousel-slide')[1].get_attribute('data-item-index')
            'ul/li[3]/p[1]'

            end_flag = False
            element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'track_title')))
            if element.is_displayed():
                self.driver.save_screenshot('success_' + browser + '.png')
                end_flag = True

            if not steps.turn_off_email_notifications(self.driver, browser):
                raise Exception('Error occurred while turning off E-Mail notifications')

            if not steps.logout(self.driver, env, browser):
                raise Exception('Error occurred while Log out.')

            if end_flag:
                steps.end_successful_after_another_actions(browser, 'Explore Tracks page presented.')
                assert True

        except TimeoutError:
            steps.end_fail(self.driver, browser, 'No element was found after awaiting.')
            assert False

        except NoSuchElementException as e:
            steps.end_fail(self.driver, browser, str(e))
            assert False

        except Exception as e:
            steps.end_fail(self.driver, browser, str(e))
            assert False
'''
