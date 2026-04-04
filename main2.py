import folium


def dms_to_decimal_lat(lat_str: str, direction: str) -> float:
    deg = int(lat_str[:2])
    minutes = float(lat_str[2:])
    decimal = deg + minutes / 60
    return -decimal if direction == "S" else decimal


def dms_to_decimal_lon(lon_str: str, direction: str) -> float:
    deg = int(lon_str[:3])
    minutes = float(lon_str[3:])
    decimal = deg + minutes / 60
    return -decimal if direction == "W" else decimal


def parser_gga(trame: str) -> dict:
    champs = trame.split(",")

    return {
        "latitude": dms_to_decimal_lat(champs[2], champs[3]),
        "longitude": dms_to_decimal_lon(champs[4], champs[5]),
        "precision": float(champs[8]),
    }


def creer_carte(data: dict, output_file: str = "carte.html") -> None:
    lat = data["latitude"]
    lon = data["longitude"]
    precision = data["precision"]

    carte = folium.Map(location=[lat, lon], zoom_start=15)

    folium.Marker(
        [lat, lon],
        tooltip="Position GPS"
    ).add_to(carte)

    folium.Circle(
        radius=precision,  # en mètres
        location=[lat, lon],
        color="blue",
        fill=True,
        fill_opacity=0.2
    ).add_to(carte)

    carte.save(output_file)
    print(f"Carte générée : {output_file}")

trame = "$GPGGA,085508.375,4804.364,N,00508.820,E,1,12,3.2,M,200.2,M,,*65"

data = parser_gga(trame)
creer_carte(data)