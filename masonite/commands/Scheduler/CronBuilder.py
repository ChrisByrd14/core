"""TODO: document
"""

class CronBuilder:
    def __init__(self):
        self.minute = '*'
        self.hour = '*'
        self.day_of_month = '*'
        self.month = '*'
        self.day_of_week = '*'

    def every_minute(self):
        self.minute = '*'

    def every_five_minutes(self):
        self.minute = '*/5'

    def every_ten_minutes(self):
        self.minute = '*/10'

    def every_fifteen_minutes(self):
        self.minute = '*/15'

    def on_minute_interval(self, minutes):
        if minutes < 0 or minutes > 59:
            raise ValueError('Minute intervales must be greater >= 0 or <= 59.')

        self.minute = f'*/{minutes}'

    def every_thirty_minutes(self):
        self.minute = '*/30'

    def hourly(self):
        self.minute = '0'
