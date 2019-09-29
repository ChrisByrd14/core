"""TODO: document
"""

from cleo import Application as Cleo

from masonite.app import App

class Scheduler:
    command = None
    time = {'hour': '00', 'minutes': '00'}

    def __init__(self):
        app = App()
        self.app = App()
        self.cleo = Cleo(name='Masonite Scheduler')

        # load application commands into the Cleo application for validation.
        self.commands = [
            key
            for key, _ in self.app.providers.items()
            if isinstance(key, str) and key.endswith('Command')
        ]

        for command in self.commands:
            self.cleo.application.add(self.app.make(f'{command}'))

    def call(self, command: str) -> object:
        """Set the craft command to be scheduled.

        Arguments:
            command {str} -- Craft console command.

        Returns:
            self
        """
        try:
            if self.cleo.find(command):
                self.command = command

                return self
        except Exception as e:
            pass

        raise ValueError(f'"{command}" is not defined in the application.')

    def at(self, time: str) -> object:
        """Set the time to run self.command at.

        Arguments:
            time {string} -- Time to run the command (24-hour format)

        Returns:
            self
        """
        hour, minutes = time.split(':')

        if '00' <= hour <= '23' and '00' <= minutes <= '59':
            self.time = {'hour': hour, 'minutes': minutes}

            return self

        raise ValueError(f'"{time}" is not a valid time string.')
