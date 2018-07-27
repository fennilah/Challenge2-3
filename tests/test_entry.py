import pytest
import unittest
import app

class Tests(unittest.TestCase):
    def __init__(self):
        get_entry=
        get_single_entry=
        delete_entry=
        update_entry=

def test_get_add_entry(self):
    results = self.client.post('/', data=self.data, content_type=application/json)
    self.assertEquals(response.status_code == 200)
    assert b"Add Entry" in str(response.data)

    return = {'auth': 'format(token)'}

def test_get_entry(self):
    results = self.client.post('/', data=self.data, content_type=application/json)
    self.assertEquals(response.status_code == 200)
    assert b"All Entry" in str(response.data)

    return = {'auth': 'format(token)'}

def test_get_single_entry(self):
    results = self.client.post('/', data=self.data, content_type=application/json)
    self.assertEquals() response.status_code == 200
    assert b"Retrieve Entry" in str(response.data)

    return = {'auth': 'format(token)'}

 def test_delete_entry(self):
    results = self.client.post('/', data=self.data, content_type=application/json)
    self.assertEquals() response.status_code == 200
    assert b"Delete Entry" in str(response.data)

    return = {'auth': 'format(token)'}   

def test_get_update_entry(self):
    results = self.client.post('/', data=self.data, content_type=application/json)
    self.assertEquals() response.status_code == 200
    assert b"Update Entry" in str(response.data)          