trame="$GPGGA,085508.375,4804.364,N,00508.820,E,1,12,3.2,M,200.2,M,,*65"

lst_champs = trame.split(",")

heure = lst_champs[1]
latitude_DMS = lst_champs[2]
latitude_S = lst_champs[2].split(".")


print(int(latitude_S[1])*60)
print(latitude_S[1])


longitude = lst_champs[4]
type_position = lst_champs[6]
sat = lst_champs[7]
Precision_horizontal = lst_champs[8]
altitude = lst_champs[10]

print(heure, latitude_DMS, longitude, type_position, sat, Precision_horizontal, altitude)

print ("heure émission = ",heure[0:2])

def nmea_to_decimal(latitude_DMS, longitude):
    degrees_lat = float(latitude_DMS[2:])
    minutes_lat= float(latitude_DMS[2:])
    degrees_lon = int(longitude[:3])
    minutes_lon = float(longitude[3:])
    
    decimal_lat = degrees_lat + (minutes_lat)/60
    decimal_lon = degrees_lon + (minutes_lon)/60
        
    return decimal_lat, decimal_lon

print(nmea_to_decimal(latitude_DMS, longitude), "oui")

