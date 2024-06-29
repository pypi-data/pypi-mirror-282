import requests


class Weather:
    """ Creates a Weather object getting an apikey as input
        and either a city name or lat and lon coordinates.

        Package user example:

        # Create a weather object using a city name:
        # The api key below is not guaranteed to work.
        # Get your own apikey from https://openweathermap.org
        # And wait a couple of hours for the apileu to be activated

        >>> weather1 = Weather(apikey="6a14e4a05a5dc9206860b6dd5cbdd07d", city="Honolulu")

        # Using latitude and longitude coordinates
        >>> weather3 = Weather(apikey="6a14e4a05a5dc9206860b6dd5cbdd07d", lat="40.1", lon="3.4")

        # Get complete weather data for the next 12 hours:
        >>> weather1.next_12h()

        # Simplified data for the next 12 hours:
        >>> weather1.next_12h_simplified()
    """

    def __init__(self, apikey, city=None, lat=None, lon=None):
        if city:
            url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={apikey}&units=imperial"
            r = requests.get(url)
            self.data = r.json()
        elif lat and lon:
            url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={apikey}&units=imperial"
            r = requests.get(url)
            self.data = r.json()
        else:
            raise TypeError("Provide either a city or lat and lon arguments")

        if self.data["cod"] != "200":
            raise ValueError(self.data["message"])

    def next_12h(self):
        """ Returns 3-hour data for the next 12 hours as a dict
        """
        # [:4] get up to (and including the 4th item)
        return self.data['list'][:4]

    def next_12h_simplified(self):
        """ Returns data, temperature, and sky condition every 3 hours
            for the next 12 hours as a list of dicts
        """
        simple_data = []
        for dicty in self.data['list'][:4]:
            simple_data.append({
                "date": dicty['dt_txt'],
                "temp": dicty['main']['temp'],
                "weather": dicty['weather'][0]['description']})
        return simple_data
