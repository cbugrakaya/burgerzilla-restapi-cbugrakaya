import json

from tests.utils.base import BaseTestCase
from tests.utils.common import register_customer, login_customer, login_restaurant


class TestAuthCustomerBlueprint(BaseTestCase):
    def test_customer_register_and_login(self):
        """ Test Customer Auth API registration and login """
        # Test registration
        data = dict(
            fullname="test User",
            email="test@user.com",
            password="test1234"
        )
        
        register_resp = register_customer(self, data)
        register_data = json.loads(register_resp.data.decode())
        
        self.assertEquals(register_resp.status_code, 200)
        self.assertTrue(register_resp.status)
        self.assertEquals(register_data["user"]["fullname"], data["fullname"])

        # Test account login
        login_resp = login_customer(self, data["email"], data["password"])
        login_data = json.loads(login_resp.data.decode())
        
        self.assertEquals(login_resp.status_code, 200)
        self.assertTrue(login_resp.status)
        self.assertEquals(login_data["user"]["email"], data["email"])

    def test_customer_try_to_login_restaurant(self):
        """ Test Customer Auth API to try to login as restaurant """
        # Test registration
        data = dict(
            fullname="test User",
            email="test@user.com",
            password="test1234",
        )

        
        register_resp = register_customer(self, data)
        register_data = json.loads(register_resp.data.decode())
        
        self.assertEquals(register_resp.status_code, 200)
        self.assertTrue(register_resp.status)
        self.assertEquals(register_data["user"]["fullname"], data["fullname"])


        # Test account login as restaurant
        login_resp = login_restaurant(self, data["email"], data["password"])
        login_data = json.loads(login_resp.data.decode())
        self.assertEquals(login_resp.status_code, 405)