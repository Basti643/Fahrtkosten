
import requests
import json
import sys
import geopy


from django.test import TestCase

# Create your tests here.
def geolocation(origin_address_input):

    from geopy.geocoders import Nominatim 
    
    g_loc = Nominatim(user_agent="GetLoc") 

    #Startadresse-Abfrage
       
    getLoc = g_loc.geocode(origin_address_input) 
    
    print("\n",getLoc.address,"\n")                               # umgewandelte Adresse
        
    lat = getLoc.latitude
    long = getLoc.longitude

    return lat, long


def distance_calc():

        GOOGLE_API_KEY= 'AIzaSyBm1wsWiSIHLpSEianmorGkkZRVnNtbMhk' 
        # example multiple destinations  google_url = f'https://maps.googleapis.com/maps/api/distancematrix/json?origins=40.6655101%2C-73.89188969999998&destinations=40.659569%2C-73.933783%7C40.729029%2C-73.851524%7C40.6860072%2C-73.6334271%7C40.598566%2C-73.7527626&key=AIzaSyBm1wsWiSIHLpSEianmorGkkZRVnNtbMhk'  
        
        origin_address_input = input("\n\nBitte Startadresse eingeben\n\n")  
        geolocation(origin_address_input)

    # Zieladress-Abfrage

        destination_address_input = input("Bitte Zieladresse eingeben\n\n")     
        getLoc = g_loc.geocode(destination_address_input) 
        
        print("\n",getLoc.address,"\n")          # umgewandelte Adresse
                
        d_lat = getLoc.latitude
        d_long = getLoc.longitude 


        google_url = f'https://maps.googleapis.com/maps/api/distancematrix/json?origins={geolocation}%2C{geolocation}&destinations={d_lat}%2C{d_long}&departure_time=now&key={GOOGLE_API_KEY}'
        #google_url = f'https://maps.googleapis.com/maps/api/distancematrix/json?origins=51.244044956733546%2C6.7946884559788785&destinations=51.15277686460546%2C6.885700582958439&departure_time=now&key=AIzaSyBm1wsWiSIHLpSEianmorGkkZRVnNtbMhk' 
        
        response = requests.get(google_url).json() 

        # Prüfung, ob Abfrage valide ist

        if response['rows'][0]['elements'][0]["status"]== "OK":
        
            try:
                distance = response['rows'][0]['elements'][0]["distance"]['value']
                duration = response['rows'][0]['elements'][0]['duration']['value']
                duration_in_traffic = response['rows'][0]['elements'][0]['duration_in_traffic']['value']
                
                print(f'\nDie Entfernung der Strecke betraegt {round(float(distance/1000),2)} km.')
                print(f'Die Fahrt dauert etwa {int(duration/60)} Minuten.\n')
                print(f'Die Fahrt dauert bei aktuellem Verkehr etwa {int(duration_in_traffic/60)} Minuten.\n')
        
            except IndexError:
                print(f'\n"Keine Ergebnisse. Bitte Eingabe überprüfen')
                sys.exit()
        
        #Fehlerprüfung bei Fehl- / Falscheingaben

        elif response['rows'][0]['elements'][0]["status"] == "NOT_FOUND":
                print(f'\n"Adresse kann nicht verarbeitet werden. Bitte Eingaben überprüfen')
        elif response['rows'][0]['elements'][0]["status"] == "ZERO_RESULTS":
                print(f'\n"Keine Route gefunden. Bitte Eingaben überprüfen')
        elif response['rows'][0]['elements'][0]["status"] == "MAX_ROUTE_LENGTH_EXCEEDED ":
                print(f'\n"Adresse ist zu lang und kann nicht verarbeitet werden. Bitte Eingaben überprüfen')

    
distance_calc()
