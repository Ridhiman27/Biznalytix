import pandas as pd

def coordinates_data(file_name):
    coordinates = []
    csv_path = "./static/"+file_name
    df = pd.read_csv(csv_path)

    for row in df.iterrows():

        latitude = float(row['DeliveryLocation(Latitude)'])
        longitude = float(row['DeliveryLocation(Longitude)'])
        print(latitude)
        print(longitude)
        coordinates.append({"latitude": latitude, "longitude": longitude})

    return coordinates
