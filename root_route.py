from flask import request
import requests

def root_routes(app): 

    @app.route("/api/hello", methods = ['GET'])
    def hello():
        client_ip = request.headers.get('X-Forwarded-For', request.remote_addr) 
        visitor_name = request.args.get('visitor_name')
        
        IP_INFO_API_ENDPOINT = f'http://ip-api.com/json/{client_ip}'
        response = requests.get(IP_INFO_API_ENDPOINT)
        response = response.json()
        country = response.get('country', 'Unknown')
        latitude = response.get('lat', 'Unknown')
        longitude = response.get('lon', 'Unknown')
        key_weather = "77vBDEuy1eYsBWbfX89bghk1FJcPDbWX"
        WEATHER_API_ENDPOINT = f'https://api.tomorrow.io/v4/weather/forecast?location={latitude},{longitude}&apikey={key_weather}'
        response = requests.get(WEATHER_API_ENDPOINT)
        
        response = response.json()
        temp = response.get('timelines').get('minutely')[0].get('values').get('temperature')

        # {
        #     "client_ip": "127.0.0.1", // The IP address of the requester
        #     "location": "New York" // The city of the requester
        #     "greeting": "Hello, Mark!, the temperature is 11 degrees Celcius in New York"
        # }


        return {
            "client_ip" : request.remote_addr,  
            "location" : country, 
            "greeting" : f"Hello, {visitor_name}!, The temperature is {temp} degrees Celcius"
            }