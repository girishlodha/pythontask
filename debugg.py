import json
from multiprocessing.sharedctypes import Value
filepaths = 'data.json'


def read_data(filepaths):
    with open(filepaths) as json_file:
        data = json.load(json_file)
    # Read data from filepaths

    return data


data = read_data(filepaths)
# print(data)


def get_oldest(data):
    age_dict = {}
    oldest_info = []

    for i in data["AVENGERS"]:
        age_dict[i] = data["AVENGERS"][i]['age']

    for i in data["DC"]:
        age_dict[i] = data["DC"][i]['age']

    oldest = [key for key in age_dict if all(age_dict[temp] <= age_dict[key] for temp in age_dict)]

    # Return all info of the oldest superheroes
    # Return all info of the oldest superheroes
    # return oldest
    for i in oldest:
        if i in data["AVENGERS"]:
            oldest_info.append(data["AVENGERS"][i])
        
        if i in data["DC"]:
            oldest_info.append(data["DC"][i])
    
    return oldest_info

# returns info: Thor and Wonder Woman
# print(get_oldest(data))

def get_oldest_avenger(data):
    max = 0
    for i in data["AVENGERS"]:
        if (data["AVENGERS"][i]['age'] > max):
            max = data["AVENGERS"][i]['age']
            oldest_avenger = data["AVENGERS"][i]
    # Return all info of the oldest avenger
    return oldest_avenger

# returns info: Thor
# print(get_oldest_avenger(data))

def get_total_points(data):
    total_points = {}
    for i in data["AVENGERS"]:
        key = data["AVENGERS"][i]["name"]
        total_points[key] = 0
        for j in data["AVENGERS"][i]['points']:
            total_points[key] += data["AVENGERS"][i]['points'][j]
    for i in data["DC"]:
        key = data["DC"][i]["name"]
        total_points[key] = 0
        for j in data["DC"][i]['points']:
            total_points[key] += data["DC"][i]['points'][j]
    # Return a dictionary
    # Key: superhero name
    # Value: total points
    return total_points

# returns info: Dict of superhero name and total points
# print(get_total_points(data))

def get_more_than_average(data):
    more_than_average = []
    avg_mcu = 0
    avg_dc = 0

    for i in data["AVENGERS"]:
        avg_mcu += data["AVENGERS"][i]['points']['stealth']
    avg_mcu = avg_mcu/len(data["AVENGERS"])
    for i in data["AVENGERS"]:
        if(data["AVENGERS"][i]['points']['stealth'] > avg_mcu):
            more_than_average.append(data["AVENGERS"][i])

    for i in data["DC"]:
        avg_dc += data["DC"][i]['points']['strength']
    avg_dc = avg_dc/len(data["DC"])
    for i in data["DC"]:
        if(data["DC"][i]['points']['strength'] > avg_dc):
            more_than_average.append(data["DC"][i])
    '''
    Return list of superheroes with stealth more than average in MCU 
    and list of superheroes with strength more than average in DCEU
    '''
    return more_than_average

  # returns info: Steve Rogers and Superman
# print(get_more_than_average(data))

def get_names(data):
    names = []
    for i in data["AVENGERS"]:
        names.append(data["AVENGERS"][i]['name'])
    for j in data["DC"]:
        names.append(data["DC"][j]['name'])
    # Return a list of superhero names
    return names

# returns a list
# print(get_names(data))