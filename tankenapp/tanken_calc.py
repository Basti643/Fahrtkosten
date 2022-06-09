# -*- coding: utf-8 -*-


import requests
import json
import sys
import geopy
from django.conf import settings
print('\nWillkommen bei Kek25\n')

def geoloc():

    from geopy.geocoders import Nominatim 
    loc = Nominatim(user_agent="GetLoc") 
    # Geopy Adressen in Koordinaten umwandeln

    while True:
        try:
            address_input = input("Bitte Adresse eingeben:\n\n") 
            getLoc = loc.geocode(address_input) 
            print(getLoc.address,"\n")       

            lat = getLoc.latitude
            long = getLoc.longitude
            return lat,long
            break   
            
        except AttributeError:
            print('\nKeine passende Adresse gefunden. Bitte erneut versuchen.\n')
        except:
            print('Fehler. Bitte erneut versuchen.\n')



def tanken_calc():
    api_key = "fc02e15f-5ca9-4851-965e-a351c8336370"
    
    #tim_lat = 51.152446           # fixer lat eigener Wohnort zum testen # brauchen Umwandlung von Google oder so von Adresse in Long Lat
    #tim_long = 6.886285           # fixer long eigener Wohnort zum testen
    #fuel_type = 'e5'              # e5, e10, diesel oder all
    #radius = 3                    # Radius in km für Anzeige der Tankstellen
    sort_index = 1                 # Sortierung der Preise in der Regel aufsteigend. 1 = günstigster Preis sort_index = i+1 heißt zweit bester Preis
   
    
    
    tanken_loc = geoloc()                                  
    lat = tanken_loc[0]        
    long = tanken_loc[1]  

    # Benzin Auswahl
        
    def fuel_type_calc():
        while True:    
            fuel_type = input('Welches Benzin möchtest du tanken?\n\nWähle zwischen E5, E10 oder Diesel aus:\n\n')

            if (fuel_type == "E5" or fuel_type == "Super 95" or fuel_type == "Super"or fuel_type == "e5"):         
                return 'e5'
                break
            elif (fuel_type == "E10" or fuel_type == "Super E10" or fuel_type == "e10"):         
                return 'e10'
                break
            elif (fuel_type == "Diesel"):         
                return 'diesel'   
                break
            else:      
                print('Ungültige Eingabe! Waehle zwischen E5, E10 oder Diesel\n')
                
    fuel_type = fuel_type_calc()           
    
    # Radius Abfrage
    def radius_calc():
        while True:

                try:
                    radius = float(input('\nBitte gibt den Radius zur Suche des günstigsten Preises in km an:\n\n'))
                    
                    if radius == 0 or radius > 25: 
                        print("Fehler! Bitte gibt einen gültigen Wert ein\n")
                    else:
                        break
                except ValueError:
                    print('Bitte gib eine Zahl ein\n')
        return radius

    radius = radius_calc()    
        
    #URL in Browser eigeben zum testen der ergebnisse der abfrage (hardcoded)            
    # https://creativecommons.tankerkoenig.de/json/list.php?lat=51.152446&lng=6.886285&rad=3&sort=price&type=e5&apikey=fc02e15f-5ca9-4851-965e-a351c8336370'
    url = f'https://creativecommons.tankerkoenig.de/json/list.php?lat={lat}&lng={long}&sort=price&type={fuel_type}&rad={radius}&apikey={api_key}'
         
    #Gesamtrückgabe in JSON Format
    data = requests.get(url).json()                                  # Durchführen der Abfrage mit Parameter oben
    
    if data['status'] == 'ok':

        try:
            station_name = data['stations'][sort_index]['name']              # sort_index für günstigsten Preis (1 Element, bei mehreren Treffern im Radius)
            station_price = data['stations'][sort_index]['price']
            station_distance = data['stations'][sort_index]['dist']   
            station_street = data['stations'][sort_index]['street']  
            station_house_nr = data['stations'][sort_index]['houseNumber'] 
            
        except IndexError:
            print(f'\nIn deinem gewählten Umkreis befinden sich keine Tankstellen\n')
            radius()
        except TypeError:
            print('Bitte gib eine Zahl oder Komma-Zahl ein:\n')
            radius()  
        except UnboundLocalError as unbound_e:
            print(unbound_e)
            print('Bitte gib eine Zahl oder Komma-Zahl ein:\n')
            radius() 

        # Ausgabe des günstigsten Ergebnisses
        print(f'\nDie günstigste Tankstelle in deiner Nähe ist die {station_name} auf der {station_street} {station_house_nr}.\n')
        print(f'Hier kostet {fuel_type.capitalize()} Benzin aktuell {station_price} €\n')
        print(f'Von deinem jetzigen Standort ist die Tankstelle ca. {station_distance} km entfernt.\n')

    elif data['status'] == 'error':
        print({data['message']})
        print('Fehler')
    
tanken_calc() 


def distance_calc():

    print('-------------------------------------------\n')
    print('Routenberechnung\n')

    GOOGLE_API_KEY= 'AIzaSyBm1wsWiSIHLpSEianmorGkkZRVnNtbMhk' 
    # example multiple destinations  google_url = f'https://maps.googleapis.com/maps/api/distancematrix/json?origins=40.6655101%2C-73.89188969999998&destinations=40.659569%2C-73.933783%7C40.729029%2C-73.851524%7C40.6860072%2C-73.6334271%7C40.598566%2C-73.7527626&key=AIzaSyBm1wsWiSIHLpSEianmorGkkZRVnNtbMhk'  


    #Startadresse-Abfrage
    origin_loc = geoloc()                                  
    o_lat = origin_loc[0]        
    o_long = origin_loc[1]  
 

    # Zieladress-Abfrage
    destination_loc = geoloc()                                  
    d_lat = destination_loc[0]        
    d_long = destination_loc[1]  
    

    google_url = f'https://maps.googleapis.com/maps/api/distancematrix/json?origins={o_lat}%2C{o_long}&destinations={d_lat}%2C{d_long}&departure_time=now&key={GOOGLE_API_KEY}'
    #google_url = f'https://maps.googleapis.com/maps/api/distancematrix/json?origins=51.244044956733546%2C6.7946884559788785&destinations=51.15277686460546%2C6.885700582958439&departure_time=now&key=AIzaSyBm1wsWiSIHLpSEianmorGkkZRVnNtbMhk' 
    
    response = requests.get(google_url).json() 

    # Prüfung, ob Abfrage valide ist

    while True:
        if response['rows'][0]['elements'][0]["status"]== "OK":
        
            try:
                distance = response['rows'][0]['elements'][0]["distance"]['value']
                duration = response['rows'][0]['elements'][0]['duration']['value']
                duration_in_traffic = response['rows'][0]['elements'][0]['duration_in_traffic']['value']
                
                print(f'\nDie Entfernung der Strecke beträgt {round(float(distance/1000),2)} km.\n')
                print(f'Die Fahrt dauert etwa {int(duration/60)} Minuten.\n')
                print(f'Die Fahrt dauert bei aktuellem Verkehr etwa {int(duration_in_traffic/60)} Minuten.\n')
                break
        
            except IndexError:
                print('\n"Keine Ergebnisse. Bitte Eingabe überprüfen\n')
                break
            except KeyError:
                print('\nKeine Strecke gefunden. Bitte Eingabe überprüfen\n')
                break

        #Fehlerprüfung bei Fehl- / Falscheingaben

        elif response['rows'][0]['elements'][0]["status"] == "NOT_FOUND":
                print(f'\n"Adresse kann nicht verarbeitet werden. Bitte Eingaben überprüfen')
        elif response['rows'][0]['elements'][0]["status"] == "ZERO_RESULTS":
                print(f'\n"Keine Route gefunden. Bitte Eingaben überprüfen')
        elif response['rows'][0]['elements'][0]["status"] == "MAX_ROUTE_LENGTH_EXCEEDED ":
                print(f'\n"Adresse ist zu lang und kann nicht verarbeitet werden. Bitte Eingaben überprüfen')

    
distance_calc()


