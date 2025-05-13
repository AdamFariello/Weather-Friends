import requests
mainUrl = "https://geocoding-api.open-meteo.com/v1/"
#search?name=Berlin&count=10&language=en&format=json"

def getPage():
    res = requests.get(mainUrl).json()
    print(res)


def main():
    getPage()

if __name__ == '__main__': main()
