import pytest

from src.tests import login, logout, registration, resource_page, start_track, why_it_works


@pytest.mark.usefixtures("driver_init_2")
class FirefoxTest:
    pass


class TestFirefox(FirefoxTest):

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
