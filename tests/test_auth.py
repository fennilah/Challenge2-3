import unittest,json

class Test_Auth_Endpoints(unittest.TestCase):

    "Tests auth, signup, login, add entry and delete"

    def setUp(self):
        app = create_app('test')
        self.client= app.test_client(self)
        self.singup_url ='/mydiary-api/v1/auth/signup'
        self.login_url ='/mydiary-api/v1/auth/login'
        self.addEntry_url ='/mydiary-api/v1/auth/edit'
        self.deleteEntry_url ='/mydiary-api/v1/auth/delete'
        self.client_signup_auth = {'fname': 'lname' ,
                'email':'mydiaryemail@api.com',
                'password': 'cpassword'}
        self.client(login_auth) = {'username': 'test',
                'email':'mydiaryemail@api.com',
                'password': 'test'}
        
    def test_singup_auth(self):
        results = self.client.post('self.signup_url', data=self.client, content_type=application/json)
        self.assertEquals(response.status_code == 200)
        assert "Account Created Successfully" in str(response.data)

    def test_login_auth(self):
        results = self.client.post('self.login_url', data=self.client, content_type=application/json)
        self.assertEquals(response.status_code == 200)
        assert "Login Successfull" in str(response.data)   

    def test_edit_auth(self):
        results = self.client.post('self.edit_url', data=self.client, content_type=application/json)
        self.assertEquals(response.status_code == 200)
        assert b"Entry Created Successfully" in str(response.data)

    def test_delete_auth(self):
        results = self.client.post('/', data=self.client, content_type=application/json)
        self.assertEquals(response.status_code == 200)
        assert b"Entry deleted Successfully" in str(response.data)         

        
   