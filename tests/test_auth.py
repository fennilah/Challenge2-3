import unittest
from app import *



class Test_Auth_Endpoints(unittest.TestCase):

    "Tests auth, signup, login, add entry and delete"

    def setUp(self):
        self.app=.app(config_name='test'):
        self.client.post =.app.client(self)
        self.singup_url ='/mydiary-api/v1/auth/signup'
        self.login_url ='/mydiary-api/v1/auth/login'
        self.addEntry_url ='/mydiary-api/v1/auth/edit'
        self.deleteEntry_url ='/mydiary-api/v1/auth/delete'
        self.client_signup_auth = {'fname': 'lname' ,
                'email':'mydiaryemail@api.com',
                'password': 'cpassword'}
        self.client_login_auth = {'username': 'test',
                'email':'mydiaryemail@api.com',
                'password': 'test'}
        
    def test_singup_auth(self):
        results = self.client.post('self.singup_url', data=self.client, content_type='application/json')
        self.assertEquals(results.status_code, 200)
        assert "Account Created Successfully" in str(results.data)

    def test_login_auth(self):
        results = self.client.post('self.login_url', data=self.client, content_type='application/json')
        self.assertEquals(results.status_code, 200)
        assert "Login Successful" in str(results.data)   

    def test_edit_auth(self):
        results = self.client.post('self.addEntry_url', data=self.client, content_type='application/json')
        self.assertEqual(results.status_code, 200)
        assert "Entry Created Successfully" in str(results.data)

    def test_delete_auth(self):
        results = self.client.post('self.deleteEntry_url', data=self.client, content_type='application/json')
        self.assertEquals(results.status_code, 200)
        assert "Entry deleted Successfully" in str(results.data)         

        
   