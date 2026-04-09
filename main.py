import folium

trame = "$GPGGA,085508.375,4804.364,N,00508.820,E,1,12,3.2,M,200.2,M,,*65"

c = trame.split(",")

# conversion en degrés décimaux
lat = int(c[2][:2]) + float(c[2][2:]) / 60
if c[3] == "S":
    lat = -lat

lon = int(c[4][:3]) + float(c[4][3:]) / 60
if c[5] == "W":
    lon = -lon

precision = float(c[8])

# carte
m = folium.Map(location=[lat, lon], zoom_start=15)

# markeur
folium.Marker([lat, lon]).add_to(m)

# cercle de pressision
folium.Circle(
    location=[lat, lon],
    radius=precision,
    fill=True
).add_to(m)

m.save("carte.html")