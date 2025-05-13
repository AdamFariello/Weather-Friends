import requests
import pprint
mainUrl = "https://geocoding-api.open-meteo.com/v1/"
paramater = "search?"
#search?name=Berlin&count=10&language=en&format=json"

# Args:
# 1) name	
# 2) count
# 3) format	
# 4) language	 -- Default
# 5) apikey	
# 6) countryCode

def getPage(city):
    apiCall = mainUrl
    def addCity(city):
        return apiCall + paramater + "name=" + city + "&" 

    apiCall = addCity(city)
    res = requests.get(apiCall).json()
    pprint.pprint(res)


def main():
    getPage("Berlin")

if __name__ == '__main__': main()
