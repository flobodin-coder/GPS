trame="$GPGGA,085508.375,4804.364,N,00508.820,E,1,12,3.2,M,200.2,M,,*65"

lst_champs = trame.split(",")

heure = lst_champs[1]
latitude = lst_champs[2]
longitude = lst_champs[4]
type_position = lst_champs[6]
sat = lst_champs[7]
Precision_horizontal = lst_champs[8]
altitude = lst_champs[10]

print(heure, latitude, longitude, type_position, sat, Precision_horizontal, altitude)

print ("heure émission = ",heure[0:2])