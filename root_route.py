from flask import request
import requests
from local_temp import get_details

def root_routes(app): 

    @app.route("/api/hello")
    def hello():
        #client_stats
        client_name = request.args.get("visitor_name")
        client_ip = request.remote_addr

        #location and temperature
        location = get_details(client_ip)
        temp = f'https://api.tomorrow.io/v4/weather/forecast?location={client_ip},-71.0466&apikey=77vBDEuy1eYsBWbfX89bghk1FJcPDbWX'

        return {
            "client_ip" : "Unknown", 
            "location" : "Unknown", 
            "greeting" : "Unknown"
        }
    
    @app.route("/api/test")
    def test():
        client_ip = request.headers.get('X-Forwarded-For', request.remote_addr) 
        IP_INFO_API_ENDPOINT = f'http://ip-api.com/json/{client_ip}'
        response = requests.get(IP_INFO_API_ENDPOINT)
        print(response.json())
        response = response.json()
        city = response.get('city', 'Unknown')
        region = response.get('regionName', 'Unknown')
        country = response.get('country', 'Unknown')
        latitude = response.get('lat', 'Unknown')
        longitude = response.get('lon', 'Unknown')


        return {
            "ip" : request.remote_addr, 
            "city": city, 
            "region" :  region, 
            "country" : country, 
            "latitude" : latitude, 
            "longitude" : longitude,
            }