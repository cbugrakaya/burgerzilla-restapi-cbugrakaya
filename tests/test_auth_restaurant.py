import json

from tests.utils.base import BaseTestCase
from tests.utils.common import register_restaurant, login_restaurant, login_customer

class TestAuthRestaurantBlueprint(BaseTestCase):
    def test_restaurant_register_and_login(self):
        """ Test Auth API registration and login """
        # Test registration
        data = dict(
            fullname="test User",
            email="test@user.com",
            password="test1234",
            restaurant_name="test restaurant"
        )

        register_resp = register_restaurant(self, data)
        register_data = json.loads(register_resp.data.decode())

        print( register_data)
        self.assertEquals(register_resp.status_code, 200)
        self.assertTrue(register_resp.status)
        self.assertEquals(register_data["user"]["fullname"], data["fullname"])

        # Test account login
        login_resp = login_restaurant(self, data["email"], data["password"])
        login_data = json.loads(login_resp.data.decode())

        self.assertEquals(login_resp.status_code, 200)
        self.assertTrue(login_resp.status)
        self.assertEquals(login_data["user"]["email"], data["email"])

    def test_restaurant_try_to_login_customer(self):
        """ Test Restaurant Auth API to try to login as customer """
        # Test registration
        data = dict(
            fullname="test User",
            email="test@user.com",
            password="test1234",
            restaurant_name="test restaurant"
        )

        register_resp = register_restaurant(self, data)
        register_data = json.loads(register_resp.data.decode())

        print( register_data)
        self.assertEquals(register_resp.status_code, 200)
        self.assertTrue(register_resp.status)
        self.assertEquals(register_data["user"]["fullname"], data["fullname"])

        # Test account login as customer
        login_resp = login_customer(self, data["email"], data["password"])
        login_data = json.loads(login_resp.data.decode())
        self.assertEquals(login_resp.status_code, 405)