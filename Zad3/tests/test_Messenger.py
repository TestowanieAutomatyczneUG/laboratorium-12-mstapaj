import unittest
from src.Messenger import Messenger
from unittest.mock import Mock


class TestMessenger(unittest.TestCase):

    def setUp(self):
        self.temp = Messenger()

    def test_sendMessage(self):
        self.temp.send_message = Mock()
        self.temp.send_message.return_value = 'Wysłano wiadomość do example@example.com'
        self.assertEqual('Wysłano wiadomość do example@example.com',
                         self.temp.send_message('example@example.com', 'Text'))

    def test_sendMessage_typeerror_email(self):
        self.temp.send_message = Mock()
        self.temp.send_message.side_effect = TypeError
        self.assertRaises(TypeError, self.temp.send_message, None, 'Text')

    def test_sendMessage_typeerror_text(self):
        self.temp.send_message = Mock()
        self.temp.send_message.side_effect = TypeError
        self.assertRaises(TypeError, self.temp.send_message, 'example@example.com', None)

    def test_sendMessage_typeerror(self):
        self.temp.send_message = Mock()
        self.temp.send_message.side_effect = TypeError
        self.assertRaises(TypeError, self.temp.send_message, None, None)

    def test_getMessage(self):
        self.temp.get_message = Mock()
        self.temp.get_message.return_value = ['First message', 'Second message']
        self.assertEqual(['First message', 'Second message'], self.temp.get_message('example@example.com'))

    def test_getMessage_empty(self):
        self.temp.get_message = Mock()
        self.temp.get_message.return_value = []
        self.assertEqual([], self.temp.get_message('example@example.com'))

    def test_getMessage_typeerror(self):
        self.temp.get_message = Mock()
        self.temp.get_message.side_effect = TypeError
        self.assertRaises(TypeError, self.temp.get_message, None)

    def tearDown(self):
        self.temp = None
