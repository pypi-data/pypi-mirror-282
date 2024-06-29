import datetime


class Flight:

    def __init__(self, flight_number: str, flight_type: str, departure_airport_code: str, arrival_airport_code: str,
                 local_departure_date: str, local_arrival_date: str, local_departure_time: str,
                 local_arrival_time: str):
        self.flight_number = flight_number
        self.flight_type = flight_type
        self.departure_airport_code = departure_airport_code
        self.arrival_airport_code = arrival_airport_code

        try:
            self.local_departure_date = datetime.datetime.strptime(local_departure_date.strip(), '%Y-%m-%d')
        except ValueError:
            raise ValueError('Local departure date must be in format YYYY-MM-DD')

        try:
            self.local_arrival_date = datetime.datetime.strptime(local_arrival_date.strip(), '%Y-%m-%d')
        except ValueError:
            raise ValueError('Local arrival date must be in format YYYY-MM-DD')

        self.local_arrival_date = local_arrival_date
        self.local_departure_time = local_departure_time
        self.local_arrival_time = local_arrival_time

    def __str__(self):
        return self.flight_number
