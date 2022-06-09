from django.db import models
from django.http import HttpResponse
from django.db import models
import requests
import json
import sys
import geopy



# Create your models here.

class geolocation_test(models.Model):
    
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

# Datenbank MOdelle erstellt über python manage.py inspectdb


# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.  
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)        
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CarData(models.Model):
    id_auto = models.BigAutoField(db_column='ID_AUTO', primary_key=True)  # Field name made lowercase.
    allgemein_marke = models.CharField(db_column='Allgemein_Marke', max_length=120)  # Field name made lowercase.
    allgemein_modell = models.CharField(db_column='Allgemein_Modell', max_length=120)  # Field name made lowercase.
    allgemein_baureihe = models.CharField(db_column='Allgemein_Baureihe', max_length=120)  # Field name made lowercase.
    allgemein_hsn_schlüsselnummer = models.CharField(db_column='Allgemein_HSN_Schlüsselnummer', max_length=120, blank=True, null=True)  # Field name made lowercase.    
    allgemein_tsn_schlüsselnummer = models.CharField(db_column='Allgemein_TSN_Schlüsselnummer', max_length=10, blank=True, null=True)  # Field name made lowercase.     
    allgemein_tsn_schlüsselnummer_2 = models.CharField(db_column='Allgemein_TSN_Schlüsselnummer_2', max_length=10, blank=True, null=True)  # Field name made lowercase. 
    messwerte_hersteller_tankgröße = models.CharField(db_column='Messwerte_Hersteller_Tankgröße', max_length=120, blank=True, null=True)  # Field name made lowercase.  
    allgemein_co2_effizienzklasse_field = models.CharField(db_column='Allgemein_CO2_Effizienzklasse_', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    allgemein_grundpreis = models.CharField(db_column='Allgemein_Grundpreis', max_length=120)  # Field name made lowercase.
    allgemein_kfz_steuer = models.CharField(db_column='Allgemein_KFZ_Steuer', max_length=120, blank=True, null=True)  # Field name made lowercase.
    karosserie_und_fahrwerk_fahrzeugklasse = models.CharField(db_column='Karosserie_und_Fahrwerk_Fahrzeugklasse', max_length=120)  # Field name made lowercase.
    karosserie_und_fahrwerk_karosserie = models.CharField(db_column='Karosserie_und_Fahrwerk_Karosserie', max_length=20)  # Field name made lowercase.
    karosserie_und_fahrwerk_reifengröße = models.CharField(db_column='Karosserie_und_Fahrwerk_Reifengröße', max_length=30, blank=True, null=True)  # Field name made lowercase.
    maße_und_gewichte_zul_gesamtgewicht = models.CharField(db_column='Maße_und_Gewichte_Zul__Gesamtgewicht', max_length=10)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    maße_und_gewichte_zuladung = models.CharField(db_column='Maße_und_Gewichte_Zuladung', max_length=10)  # Field name made lowercase.
    messwerte_hersteller_batteriekapazität_brutto_in_kwh = models.CharField(db_column='Messwerte_Hersteller_Batteriekapazität__Brutto__in_kWh', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    messwerte_hersteller_batteriekapazität_netto_in_kwh = models.CharField(db_column='Messwerte_Hersteller_Batteriekapazität__Netto__in_kWh', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    messwerte_hersteller_beschleunigung_0_100km_h = models.CharField(db_column='Messwerte_Hersteller_Beschleunigung_0_100km_h', max_length=120, blank=True, null=True)  # Field name made lowercase.
    messwerte_hersteller_co2_wert_nefz_field = models.CharField(db_column='Messwerte_Hersteller_CO2_Wert__NEFZ_', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    messwerte_hersteller_fahrgeräusch = models.CharField(db_column='Messwerte_Hersteller_Fahrgeräusch', max_length=120, blank=True, null=True)  # Field name made lowercase.
    messwerte_hersteller_füllmenge_adblue_behälter = models.CharField(db_column='Messwerte_Hersteller_Füllmenge_AdBlue_Behälter', max_length=120, blank=True, null=True)  # Field name made lowercase.
    messwerte_hersteller_füllmenge_adblue_behälter_optional_field = models.CharField(db_column='Messwerte_Hersteller_Füllmenge_AdBlue_Behälter__optional_', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.        
    messwerte_hersteller_höchstgeschwindigkeit = models.CharField(db_column='Messwerte_Hersteller_Höchstgeschwindigkeit', max_length=120, blank=True, null=True)  # Field name made lowercase.
    messwerte_hersteller_reichweite_nefz_elektrisch_field = models.CharField(db_column='Messwerte_Hersteller_Reichweite_NEFZ__elektrisch_', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    messwerte_hersteller_reichweite_wltp_elektrisch_field = models.CharField(db_column='Messwerte_Hersteller_Reichweite_WLTP__elektrisch_', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    messwerte_hersteller_reichweite_wltp_city_elektrisch_field = models.CharField(db_column='Messwerte_Hersteller_Reichweite_WLTP_City__elektrisch_', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    messwerte_hersteller_batterietyp = models.CharField(db_column='Messwerte_Hersteller_Batterietyp', max_length=120, blank=True, null=True)  # Field name made lowercase.
    messwerte_hersteller_verbrauch_90_km_h_drittelmix_field = models.CharField(db_column='Messwerte_Hersteller_Verbrauch_90_km_h__Drittelmix_', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    messwerte_hersteller_verbrauch_120_km_h_drittelmix_field = models.CharField(db_column='Messwerte_Hersteller_Verbrauch_120_km_h__Drittelmix_', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    messwerte_hersteller_verbrauch_autobahn_wltp_field = models.CharField(db_column='Messwerte_Hersteller_Verbrauch_Autobahn__WLTP_', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    messwerte_hersteller_verbrauch_autobahn_wltp_2_antrieb = models.CharField(db_column='Messwerte_Hersteller_Verbrauch_Autobahn__WLTP____2__Antrieb', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    messwerte_hersteller_verbrauch_außerorts_2_antrieb_nefz_field = models.CharField(db_column='Messwerte_Hersteller_Verbrauch_Außerorts__2_Antrieb___NEFZ_', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.      
    messwerte_hersteller_verbrauch_außerorts_nefz_field = models.CharField(db_column='Messwerte_Hersteller_Verbrauch_Außerorts__NEFZ__', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    messwerte_hersteller_verbrauch_gesamt_2_antrieb_nefz_field = models.CharField(db_column='Messwerte_Hersteller_Verbrauch_Gesamt__2_Antrieb___NEFZ_', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    messwerte_hersteller_verbrauch_gesamt_drittelmix_field = models.CharField(db_column='Messwerte_Hersteller_Verbrauch_gesamt__Drittelmix_', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    messwerte_hersteller_verbrauch_gesamt_nefz_field = models.CharField(db_column='Messwerte_Hersteller_Verbrauch_Gesamt__NEFZ_', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    messwerte_hersteller_verbrauch_innerorts_2_antrieb_nefz_field = models.CharField(db_column='Messwerte_Hersteller_Verbrauch_Innerorts__2_Antrieb___NEFZ_', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.      
    messwerte_hersteller_verbrauch_innerorts_nefz_field = models.CharField(db_column='Messwerte_Hersteller_Verbrauch_Innerorts__NEFZ__', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    messwerte_hersteller_verbrauch_kombiniert_wltp_field = models.CharField(db_column='Messwerte_Hersteller_Verbrauch_kombiniert__WLTP_', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    messwerte_hersteller_verbrauch_kombiniert_wltp_2_antrieb = models.CharField(db_column='Messwerte_Hersteller_Verbrauch_kombiniert__WLTP____2__Antrieb', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    messwerte_hersteller_verbrauch_kurzstrecke_wltp_field = models.CharField(db_column='Messwerte_Hersteller_Verbrauch_Kurzstrecke__WLTP_', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    messwerte_hersteller_verbrauch_kurzstrecke_wltp_2_antrieb = models.CharField(db_column='Messwerte_Hersteller_Verbrauch_Kurzstrecke__WLTP____2__Antrieb', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    messwerte_hersteller_verbrauch_landstraße_wltp_field = models.CharField(db_column='Messwerte_Hersteller_Verbrauch_Landstraße__WLTP_', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    messwerte_hersteller_verbrauch_landstraße_wltp_2_antrieb = models.CharField(db_column='Messwerte_Hersteller_Verbrauch_Landstraße__WLTP____2__Antrieb', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    messwerte_hersteller_verbrauch_stadt_drittelmix_field = models.CharField(db_column='Messwerte_Hersteller_Verbrauch_Stadt__Drittelmix_', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    messwerte_hersteller_verbrauch_stadtrand_wltp_field = models.CharField(db_column='Messwerte_Hersteller_Verbrauch_Stadtrand__WLTP_', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    messwerte_hersteller_verbrauch_stadtrand_wltp_2_antrieb = models.CharField(db_column='Messwerte_Hersteller_Verbrauch_Stadtrand__WLTP____2__Antrieb', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    motor_und_antrieb_abgasreinigung_verbrennungsmotor_field = models.CharField(db_column='Motor_und_Antrieb_Abgasreinigung__Verbrennungsmotor_', max_length=120)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    motor_und_antrieb_antriebsart = models.CharField(db_column='Motor_und_Antrieb_Antriebsart', max_length=120)  # Field name made lowercase.
    motor_und_antrieb_anzahl_gänge = models.CharField(db_column='Motor_und_Antrieb_Anzahl_Gänge', max_length=120, blank=True, null=True)  # Field name made lowercase.  
    motor_und_antrieb_anzahl_zylinder_verbrennungsmotor_field = models.CharField(db_column='Motor_und_Antrieb_Anzahl_Zylinder__Verbrennungsmotor_', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    motor_und_antrieb_aufladung_verbrennungsmotor_field = models.CharField(db_column='Motor_und_Antrieb_Aufladung__Verbrennungsmotor_', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    motor_und_antrieb_drehmoment_systemleistung_field = models.CharField(db_column='Motor_und_Antrieb_Drehmoment__Systemleistung_', max_length=120)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    motor_und_antrieb_drehmoment_maximal_bei_u_min = models.CharField(db_column='Motor_und_Antrieb_Drehmoment_maximal_bei_U_min', max_length=120, blank=True, null=True)  # Field name made lowercase.
    motor_und_antrieb_einbauposition = models.CharField(db_column='Motor_und_Antrieb_Einbauposition', max_length=120, blank=True, null=True)  # Field name made lowercase.
    motor_und_antrieb_getriebeart = models.CharField(db_column='Motor_und_Antrieb_Getriebeart', max_length=120)  # Field name made lowercase.
    motor_und_antrieb_hubraum_verbrennungsmotor_field = models.CharField(db_column='Motor_und_Antrieb_Hubraum__Verbrennungsmotor_', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    motor_und_antrieb_kraftstoffart = models.CharField(db_column='Motor_und_Antrieb_Kraftstoffart', max_length=120)  # Field name made lowercase.
    motor_und_antrieb_leistung_drehmoment = models.CharField(db_column='Motor_und_Antrieb_Leistung_Drehmoment', max_length=120, blank=True, null=True)  # Field name made lowercase.
    motor_und_antrieb_leistung_maximal_bei_u_min = models.CharField(db_column='Motor_und_Antrieb_Leistung_maximal_bei_U_min', max_length=120, blank=True, null=True)  # Field name made lowercase.
    motor_und_antrieb_leistung_systemleistung = models.CharField(db_column='Motor_und_Antrieb_Leistung_Systemleistung', max_length=120)  # Field name made lowercase.   
    motor_und_antrieb_leistung_maximal_in_ps_systemleistung_field = models.CharField(db_column='Motor_und_Antrieb_Leistung_maximal_in_PS__Systemleistung_', max_length=120)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    motor_und_antrieb_motorart = models.CharField(db_column='Motor_und_Antrieb_Motorart', max_length=120)  # Field name made lowercase.
    motor_und_antrieb_motorcode = models.CharField(db_column='Motor_und_Antrieb_Motorcode', max_length=120, blank=True, null=True)  # Field name made lowercase.        
    motor_und_antrieb_schadstoffklasse = models.CharField(db_column='Motor_und_Antrieb_Schadstoffklasse', max_length=120)  # Field name made lowercase.
    preise_und_ausstattung_grundpreis = models.CharField(db_column='Preise_und_Ausstattung_Grundpreis', max_length=120)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'car_data'

    def __str__(self):
        return self.allgemein_modell
    
    


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Mycar(models.Model):
    id_auto = models.BigAutoField(db_column='ID_AUTO', primary_key=True)  # Field name made lowercase.
    allgemein_marke = models.CharField(db_column='Allgemein_Marke', max_length=120) # Field name made lowercase.
    allgemein_modell = models.CharField(db_column='Allgemein_Modell', max_length=120)  # Field name made lowercase.
    allgemein_baureihe = models.CharField(db_column='Allgemein_Baureihe', max_length=120)  # Field name made lowercase.
    allgemein_hsn_schlüsselnummer = models.CharField(db_column='Allgemein_HSN_Schlüsselnummer', max_length=120, blank=True, null=True)  # Field name made lowercase.    
    allgemein_tsn_schlüsselnummer = models.CharField(db_column='Allgemein_TSN_Schlüsselnummer', max_length=10, blank=True, null=True)  # Field name made lowercase.     
    allgemein_tsn_schlüsselnummer_2 = models.CharField(db_column='Allgemein_TSN_Schlüsselnummer_2', max_length=10, blank=True, null=True)  # Field name made lowercase. 
    messwerte_hersteller_tankgröße = models.CharField(db_column='Messwerte_Hersteller_Tankgröße', max_length=120, blank=True, null=True)  # Field name made lowercase.  
    allgemein_co2_effizienzklasse_field = models.CharField(db_column='Allgemein_CO2_Effizienzklasse_', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    allgemein_grundpreis = models.CharField(db_column='Allgemein_Grundpreis', max_length=120)  # Field name made lowercase.
    allgemein_kfz_steuer = models.CharField(db_column='Allgemein_KFZ_Steuer', max_length=120, blank=True, null=True)  # Field name made lowercase.
    karosserie_und_fahrwerk_fahrzeugklasse = models.CharField(db_column='Karosserie_und_Fahrwerk_Fahrzeugklasse', max_length=120)  # Field name made lowercase.
    karosserie_und_fahrwerk_karosserie = models.CharField(db_column='Karosserie_und_Fahrwerk_Karosserie', max_length=20)  # Field name made lowercase.
    karosserie_und_fahrwerk_reifengröße = models.CharField(db_column='Karosserie_und_Fahrwerk_Reifengröße', max_length=30, blank=True, null=True)  # Field name made lowercase.
    maße_und_gewichte_zul_gesamtgewicht = models.CharField(db_column='Maße_und_Gewichte_Zul__Gesamtgewicht', max_length=10)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    maße_und_gewichte_zuladung = models.CharField(db_column='Maße_und_Gewichte_Zuladung', max_length=10)  # Field name made lowercase.
    messwerte_hersteller_batteriekapazität_brutto_in_kwh = models.CharField(db_column='Messwerte_Hersteller_Batteriekapazität__Brutto__in_kWh', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    messwerte_hersteller_batteriekapazität_netto_in_kwh = models.CharField(db_column='Messwerte_Hersteller_Batteriekapazität__Netto__in_kWh', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    messwerte_hersteller_beschleunigung_0_100km_h = models.CharField(db_column='Messwerte_Hersteller_Beschleunigung_0_100km_h', max_length=120, blank=True, null=True)  # Field name made lowercase.
    messwerte_hersteller_co2_wert_nefz_field = models.CharField(db_column='Messwerte_Hersteller_CO2_Wert__NEFZ_', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    messwerte_hersteller_fahrgeräusch = models.CharField(db_column='Messwerte_Hersteller_Fahrgeräusch', max_length=120, blank=True, null=True)  # Field name made lowercase.
    messwerte_hersteller_füllmenge_adblue_behälter = models.CharField(db_column='Messwerte_Hersteller_Füllmenge_AdBlue_Behälter', max_length=120, blank=True, null=True)  # Field name made lowercase.
    messwerte_hersteller_füllmenge_adblue_behälter_optional_field = models.CharField(db_column='Messwerte_Hersteller_Füllmenge_AdBlue_Behälter__optional_', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.        
    messwerte_hersteller_höchstgeschwindigkeit = models.CharField(db_column='Messwerte_Hersteller_Höchstgeschwindigkeit', max_length=120, blank=True, null=True)  # Field name made lowercase.
    messwerte_hersteller_reichweite_nefz_elektrisch_field = models.CharField(db_column='Messwerte_Hersteller_Reichweite_NEFZ__elektrisch_', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    messwerte_hersteller_reichweite_wltp_elektrisch_field = models.CharField(db_column='Messwerte_Hersteller_Reichweite_WLTP__elektrisch_', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    messwerte_hersteller_reichweite_wltp_city_elektrisch_field = models.CharField(db_column='Messwerte_Hersteller_Reichweite_WLTP_City__elektrisch_', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    messwerte_hersteller_batterietyp = models.CharField(db_column='Messwerte_Hersteller_Batterietyp', max_length=120, blank=True, null=True)  # Field name made lowercase.
    messwerte_hersteller_verbrauch_90_km_h_drittelmix_field = models.CharField(db_column='Messwerte_Hersteller_Verbrauch_90_km_h__Drittelmix_', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    messwerte_hersteller_verbrauch_120_km_h_drittelmix_field = models.CharField(db_column='Messwerte_Hersteller_Verbrauch_120_km_h__Drittelmix_', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    messwerte_hersteller_verbrauch_autobahn_wltp_field = models.CharField(db_column='Messwerte_Hersteller_Verbrauch_Autobahn__WLTP_', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    messwerte_hersteller_verbrauch_autobahn_wltp_2_antrieb = models.CharField(db_column='Messwerte_Hersteller_Verbrauch_Autobahn__WLTP____2__Antrieb', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    messwerte_hersteller_verbrauch_außerorts_2_antrieb_nefz_field = models.CharField(db_column='Messwerte_Hersteller_Verbrauch_Außerorts__2_Antrieb___NEFZ_', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.      
    messwerte_hersteller_verbrauch_außerorts_nefz_field = models.CharField(db_column='Messwerte_Hersteller_Verbrauch_Außerorts__NEFZ__', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    messwerte_hersteller_verbrauch_gesamt_2_antrieb_nefz_field = models.CharField(db_column='Messwerte_Hersteller_Verbrauch_Gesamt__2_Antrieb___NEFZ_', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    messwerte_hersteller_verbrauch_gesamt_drittelmix_field = models.CharField(db_column='Messwerte_Hersteller_Verbrauch_gesamt__Drittelmix_', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    messwerte_hersteller_verbrauch_gesamt_nefz_field = models.CharField(db_column='Messwerte_Hersteller_Verbrauch_Gesamt__NEFZ_', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    messwerte_hersteller_verbrauch_innerorts_2_antrieb_nefz_field = models.CharField(db_column='Messwerte_Hersteller_Verbrauch_Innerorts__2_Antrieb___NEFZ_', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.      
    messwerte_hersteller_verbrauch_innerorts_nefz_field = models.CharField(db_column='Messwerte_Hersteller_Verbrauch_Innerorts__NEFZ__', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    messwerte_hersteller_verbrauch_kombiniert_wltp_field = models.CharField(db_column='Messwerte_Hersteller_Verbrauch_kombiniert__WLTP_', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    messwerte_hersteller_verbrauch_kombiniert_wltp_2_antrieb = models.CharField(db_column='Messwerte_Hersteller_Verbrauch_kombiniert__WLTP____2__Antrieb', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    messwerte_hersteller_verbrauch_kurzstrecke_wltp_field = models.CharField(db_column='Messwerte_Hersteller_Verbrauch_Kurzstrecke__WLTP_', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    messwerte_hersteller_verbrauch_kurzstrecke_wltp_2_antrieb = models.CharField(db_column='Messwerte_Hersteller_Verbrauch_Kurzstrecke__WLTP____2__Antrieb', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    messwerte_hersteller_verbrauch_landstraße_wltp_field = models.CharField(db_column='Messwerte_Hersteller_Verbrauch_Landstraße__WLTP_', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    messwerte_hersteller_verbrauch_landstraße_wltp_2_antrieb = models.CharField(db_column='Messwerte_Hersteller_Verbrauch_Landstraße__WLTP____2__Antrieb', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    messwerte_hersteller_verbrauch_stadt_drittelmix_field = models.CharField(db_column='Messwerte_Hersteller_Verbrauch_Stadt__Drittelmix_', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    messwerte_hersteller_verbrauch_stadtrand_wltp_field = models.CharField(db_column='Messwerte_Hersteller_Verbrauch_Stadtrand__WLTP_', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    messwerte_hersteller_verbrauch_stadtrand_wltp_2_antrieb = models.CharField(db_column='Messwerte_Hersteller_Verbrauch_Stadtrand__WLTP____2__Antrieb', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    motor_und_antrieb_abgasreinigung_verbrennungsmotor_field = models.CharField(db_column='Motor_und_Antrieb_Abgasreinigung__Verbrennungsmotor_', max_length=120)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    motor_und_antrieb_antriebsart = models.CharField(db_column='Motor_und_Antrieb_Antriebsart', max_length=120)  # Field name made lowercase.
    motor_und_antrieb_anzahl_gänge = models.CharField(db_column='Motor_und_Antrieb_Anzahl_Gänge', max_length=120, blank=True, null=True)  # Field name made lowercase.  
    motor_und_antrieb_anzahl_zylinder_verbrennungsmotor_field = models.CharField(db_column='Motor_und_Antrieb_Anzahl_Zylinder__Verbrennungsmotor_', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    motor_und_antrieb_aufladung_verbrennungsmotor_field = models.CharField(db_column='Motor_und_Antrieb_Aufladung__Verbrennungsmotor_', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    motor_und_antrieb_drehmoment_systemleistung_field = models.CharField(db_column='Motor_und_Antrieb_Drehmoment__Systemleistung_', max_length=120)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    motor_und_antrieb_drehmoment_maximal_bei_u_min = models.CharField(db_column='Motor_und_Antrieb_Drehmoment_maximal_bei_U_min', max_length=120, blank=True, null=True)  # Field name made lowercase.
    motor_und_antrieb_einbauposition = models.CharField(db_column='Motor_und_Antrieb_Einbauposition', max_length=120, blank=True, null=True)  # Field name made lowercase.
    motor_und_antrieb_getriebeart = models.CharField(db_column='Motor_und_Antrieb_Getriebeart', max_length=120)  # Field name made lowercase.
    motor_und_antrieb_hubraum_verbrennungsmotor_field = models.CharField(db_column='Motor_und_Antrieb_Hubraum__Verbrennungsmotor_', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    motor_und_antrieb_kraftstoffart = models.CharField(db_column='Motor_und_Antrieb_Kraftstoffart', max_length=120)  # Field name made lowercase.
    motor_und_antrieb_leistung_drehmoment = models.CharField(db_column='Motor_und_Antrieb_Leistung_Drehmoment', max_length=120, blank=True, null=True)  # Field name made lowercase.
    motor_und_antrieb_leistung_maximal_bei_u_min = models.CharField(db_column='Motor_und_Antrieb_Leistung_maximal_bei_U_min', max_length=120, blank=True, null=True)  # Field name made lowercase.
    motor_und_antrieb_leistung_systemleistung = models.CharField(db_column='Motor_und_Antrieb_Leistung_Systemleistung', max_length=120)  # Field name made lowercase.   
    motor_und_antrieb_leistung_maximal_in_ps_systemleistung_field = models.CharField(db_column='Motor_und_Antrieb_Leistung_maximal_in_PS__Systemleistung_', max_length=120)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    motor_und_antrieb_motorart = models.CharField(db_column='Motor_und_Antrieb_Motorart', max_length=120)  # Field name made lowercase.
    motor_und_antrieb_motorcode = models.CharField(db_column='Motor_und_Antrieb_Motorcode', max_length=120, blank=True, null=True)  # Field name made lowercase.        
    motor_und_antrieb_schadstoffklasse = models.CharField(db_column='Motor_und_Antrieb_Schadstoffklasse', max_length=120)  # Field name made lowercase.
    preise_und_ausstattung_grundpreis = models.CharField(db_column='Preise_und_Ausstattung_Grundpreis', max_length=120)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mycar'

    def __str__(self):
        return self.allgemein_modell

        # wird glaube ich nicht benötigt? Passwort wird in Django User DB gespeicehrt 

class User(models.Model):
    id_user = models.BigAutoField(db_column='ID_USER', primary_key=True)  # Field name made lowercase.
    username = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=40, blank=True, null=True) 
    fk_auto = models.BigIntegerField(db_column='FK_AUTO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'

    def __str__(self):
        return self.username