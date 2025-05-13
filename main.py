import requests, geocoder
from pprint import pprint

# TODO: Figure if should include search? at the end
searchUrl = "http://geocoding-api.open-meteo.com/v1/search?"
forecastUrl = "http://api.open-meteo.com/v1/forecast?"

# Args:
# 1) name	
# 2) count
# 3) format	
# 4) language	 -- Default
# 5) apikey	
# 6) countryCode

#print(vars(g))
#print(dir(g))
#pprint(g.__dict__)
#print(g())

def getUserLocation():
    return geocoder.ip('me').latlng

def searchLocations():
    apiCall = searchUrl 

    # TODO: Figure if adding "&" at the end is needed
    def getParamCity(city):
        return "name=%s&" % str(city)

    res = requests.get(apiCall).json()
    pprint(res)

def getForecast():
    apiCall = forecastUrl 

    # TODO: Figure if adding "&" at the end is needed
    def getParamLatlng(latlng):
        return "latitude=%f&longitude=%f" % (latlng[0], latlng[1])

    apiCall += getParamLatlng(getUserLocation())
    print(apiCall)

    res = requests.get(apiCall).json()
    pprint(res)


def main():
    #searchLocations()
    getForecast()

if __name__ == '__main__': main()
