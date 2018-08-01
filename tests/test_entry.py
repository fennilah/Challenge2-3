import unittest
from app import *


class Tests(unittest.TestCase):
    def __init__(self):
        get_entry='/api/v1/auth/entries'
        get_single_entry='/api/v1/auth/entry'
        delete_entry='/api/v1/auth/delete'
        update_entry='/api/v1/auth/update'


    def test_get_entry(self):
        results = .client().get('get_entry', data=self.data, content_type='application/json')
        self.assertEqual(results.status_code, 200)
        assert "Add Entry" in str(results.data)

    
        return self.client().post('/api/v1/auth/entry/', data=user_data)

    def test_get_single_entry(self):
        results = .client().get('get_single_entry', data=self.data, content_type='application/json')
        self.assertEqual(results.status_code, 200)
        assert "All Entry" in str(results.data)

    
        return self.client().post('/api/v1/auth/single/entry/', data=user_data)

    def test_delete_entry(self):
        results = .client().delete('delete_entry', data=self.data, content_type='application/json')
        self.assertEqual(results.status_code, 200)
        assert "Delete Entry" in str(results.data)

     
        return self.client().post('/api/v1/auth/delete/entry', data=user_data)

    def test_get_update_entry(self):
        results = .client.post('update_entry', data=self.data, content_type='application/json')
        self.assertEquals(results.status_code, 200)
        assert "Update Entry" in str(results.data)


        return self.client().post('/api/v1/auth/update/entry/', data=user_data)
             