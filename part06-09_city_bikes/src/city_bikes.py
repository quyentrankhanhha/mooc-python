def get_station_data(filename: str):
    result = {}
    with open(f"{filename}") as data_file:
        for line in data_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            print(parts)
            # if parts[0] == "Longitude":
            #     continue
            # result[parts[3]] = (int(parts[0]), int(parts[1]))
    return result

def distance(stations: dict, station1: str, station2: str):
    return

if __name__ == "__main__":
    stations = get_station_data('stations1.csv')
    print(stations)