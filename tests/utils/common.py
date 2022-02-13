import json


def login_customer(self, email, password):
    """Login a customer"""
    return self.client.post('/auth/customer/login', data=json.dumps(dict(email=email,password=password)), content_type='application/json')

def register_customer(self, data):
    """Register a new customer"""
    return self.client.post('/auth/customer/register', data=json.dumps(data), content_type='application/json')


def login_restaurant(self, email, password):
    """Login a restaurant"""
    return self.client.post('/auth/restaurant/login', data=json.dumps(dict(email=email,password=password)), content_type='application/json')


def register_restaurant(self, data):
    """Register a new restaurant"""
    return self.client.post('/auth/restaurant/register', data=json.dumps(data), content_type='application/json')


