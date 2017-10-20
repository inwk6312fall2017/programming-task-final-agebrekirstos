from weather import Weather

weather = Weather()

def get_dates_high():
    """displays the date with the highest temperature from weather forecast for next five days"""
    location = weather.lookup_by_location('halifax')
    condition = location.condition()


    # Get weather forecasts for the upcoming days.

    my_list =[]
    high = 0
    date = ""

    forecasts = location.forecast()

    for i in range(5):
        my_list.append(forecasts[i])

    for index in my_list:
        if index['high'] > str(high):
            high = index['high']
            date = index['date']
    return date

def get_dates_low():
    """returns the date with the lowest temperature from weather forecast for next five days"""
    location = weather.lookup_by_location('halifax')
    forecasts = location.forecast()
    low_list = []

    low_date = ""

    forecasts = location.forecast()

    for i in range(5):
        low_list.append(forecasts[i])

    #print(low_list)
    low = low_list[0]['low']
    #print(low)
    for days in low_list:
        if days['low'] < str(low):
            low= days['low']
            low_date = days['date']
    return low_date

def will_it_rain():
    """determines if it is going to rain within the next five days"""
    location = weather.lookup_by_location('halifax')
    forecasts = location.forecast()
    rain_list = []
    rain_date = ""
    forecasts = location.forecast()
    for i in range(5):
        rain_list.append(forecasts[i])
    #print(rain_list)
    for index in rain_list:
        if index['text'] =='Rain':
            rain_date = index['date']

    return rain_date


print(get_dates_high())
print(get_dates_low())
print(will_it_rain())