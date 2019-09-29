import unittest

import pytest

from masonite.app import App
from masonite.commands.RoutesCommand import RoutesCommand
from masonite.commands.Scheduler import Scheduler


class TestScheduler(unittest.TestCase):

    def setUp(self):
        self.scheduler = Scheduler()
        self.app = App()

        # define command, and bind to Masonite/Cleo application
        self.app.bind('MasoniteRoutesCommand', RoutesCommand())
        self.scheduler.cleo.add(self.app.make('MasoniteRoutesCommand'))

    def test_invalid_command_raises_exception(self):
        with pytest.raises(ValueError, match='.* is not defined in the application.'):
            self.scheduler.call('some:command')

        self.assertFalse(self.scheduler.command)

    def test_valid_commands_are_set_and_retrieved(self):
        self.scheduler.call('show:routes')
        self.assertEqual(self.scheduler.command, 'show:routes')
        self.assertIsInstance(self.scheduler.cleo.find('show:routes'), RoutesCommand)

    def test_set_specific_time(self):
        """Tests that .at() accepts a valid 24-hour format time string.
        """
        with pytest.raises(ValueError, match='.* is not a valid time string.'):
            self.scheduler.at('24:00')
            self.scheduler.at('01:60')

        self.scheduler.at('13:01')
        self.assertEqual(self.scheduler.time, {'hour': '13', 'minutes': '01'})

    def test_(self):
        pass
