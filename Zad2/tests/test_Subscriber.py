from src.Subscriber import Subscriber
from unittest.mock import Mock
import unittest


class TestSubscriber(unittest.TestCase):
    def setUp(self):
        self.temp = Subscriber()

    def test_addClient(self):
        self.temp.add_client = Mock()
        self.temp.add_client.return_value = {'firstname': 'Jan', 'lastname': 'Kowalski'}
        self.assertEqual({'firstname': 'Jan', 'lastname': 'Kowalski'}, self.temp.add_client('Jan', 'Kowalski'))

    def test_addClient_typeerror_firstname(self):
        self.temp.add_client = Mock()
        self.temp.add_client.side_effect = TypeError
        self.assertRaises(TypeError, self.temp.add_client, None, 'Kowalski')

    def test_addClient_typeerror_lastname(self):
        self.temp.add_client = Mock()
        self.temp.add_client.side_effect = TypeError
        self.assertRaises(TypeError, self.temp.add_client, 'Jan', None)

    def test_addClient_typeerror(self):
        self.temp.add_client = Mock()
        self.temp.add_client.side_effect = TypeError
        self.assertRaises(TypeError, self.temp.add_client, None, None)

    def test_deleteClient(self):
        self.temp.delete_client = Mock()
        self.temp.delete_client.return_value = 2
        self.assertEqual(2, self.temp.delete_client(2))

    def test_deleteClient_typeerror(self):
        self.temp.delete_client = Mock()
        self.temp.delete_client.side_effect = TypeError
        self.assertRaises(TypeError, self.temp.delete_client, None)

    def test_deleteClient_valueerror(self):
        self.temp.delete_client = Mock()
        self.temp.delete_client.side_effect = ValueError
        self.assertRaises(ValueError, self.temp.delete_client, 0)

    def test_sendMessage(self):
        self.temp.send_message = Mock()
        self.temp.send_message.return_value = "Wysłano wiadomość do Jan Kowalski"
        self.assertEqual("Wysłano wiadomość do Jan Kowalski", self.temp.send_message('Text', 1))

    def test_sendMessage_typeerror_text(self):
        self.temp.send_message = Mock()
        self.temp.send_message.side_effect = TypeError
        self.assertRaises(TypeError, self.temp.send_message, None, 1)

    def test_sendMessage_typeerror_client_id(self):
        self.temp.send_message = Mock()
        self.temp.send_message.side_effect = TypeError
        self.assertRaises(TypeError, self.temp.send_message, 'Text', None)

    def est_sendMessage_valueerror_client_id(self):
        self.temp.send_message = Mock()
        self.temp.send_message.side_effect = ValueError
        self.assertRaises(ValueError, self.temp.send_message, 'Text', -2)

    def tearDown(self):
        self.temp = None
