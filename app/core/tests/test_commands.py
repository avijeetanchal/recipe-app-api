from unittest.mock import patch

from django.core.management import call_command
from django.db.utils import OperationalError
# this will tell whether the connection is on or off

from django.test import TestCase

class CommandTests(TestCase):

    def test_wait_for_db_read(self):
        """TEST WAITING FOR DB WHEN DB IS AVAILABLE"""
        # simulate the behaviour of django to see connection.
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.return_value = True
            # this means whenever this is called it override the function of
            # above method and just do
            # return_value attir to True and also allows us to monitor how many
            # times this was called.
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 1)

    @patch('time.sleep',return_value=True) # to speed up 5 tries
    def test_wait_for_db(self):
        """ wait for db 5 times and run 6th time"""
        # a while loop check that connectionhandler raise the error, if yes
        # then wair for few sec and try again.
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)
