import summoner_by_name as summoner
import requests
import json
import pprint
import API_key

my_key = API_key.GetKey()

use_additional_data = False
def InitGlobal():
    global use_additional_data
    use_additional_data = False

def SetUseAdditionalData():
    global use_additional_data
    use_additional_data = True

def InitItemData():
    region = summoner.InputRegion()
    additional_data = input("Include all data?(yes or no) ")
    if (additional_data == "yes"):
        SetUseAdditionalData()
        call = "https://global.api.pvp.net/api/lol/static-data/" + region +  \
        "/v1.2/item?itemListData=all&" + my_key

    else:
        call = "https://global.api.pvp.net/api/lol/static-data/" + region + "/v1.2/item?" + my_key

    try:
        my_request = requests.get(call)

    except requests.exception.ConnectionError as error:
        print("Invalid region")
        exit()

    my_data = json.loads(my_request.text)
    return my_data

def GetData(item_data):
    """ Returns Map[string, ItemDto] """
    return item_data['data']

# This all seems tedious and rigid to use
def GetItemNames(my_data):
    names = {}
    for i in my_data.keys():
        names[i] = [my_data[i]['name']]
    return names

def AddItemDescription(name_data, my_data):
    new_dict = name_data
    for i in my_data.keys():
        new_dict[i].append(my_data[i]['description'])
    return new_dict

def GetGoldDto(my_data):
    if (not use_additional_data):
        print("Error, must use additional data")
        exit()
    gold = {}
    for i in my_data.keys():
        gold[i] = my_data[i]['name'], my_data[i]['gold']
    return gold

def GetImageDto(my_data):
    if (not use_additional_data):
        print("Error, must use additional data")
        exit()
    image = {}
    for i in my_data.keys():
        image[i] = my_data[i]['name'],my_data[i]['image']
    return image

def GetDescription(my_data):
    my_dict = {}
    for i in my_data.keys():
        my_dict[i] = my_data[i]['name'], my_data[i]['description']
    return my_dict

# Instead of making a bunch of functions, why not just make one that fits all?
# More flexible and less work!
def GetCustomData(key, my_data):
    dict = {}
    for i in my_data.keys():
        dict[i] = [my_data[i][key]]
    return dict

def AddCustomData(key, custom_data, my_data):
    dict = custom_data
    for i in my_data.keys():
        dict[i].append(my_data[i][key])
    return dict

def main():
    item_data = InitItemData()
    my_data = GetData(item_data)
    my_dict = GetCustomData('image', my_data)
    my_dict = AddCustomData('description', my_dict, my_data)
    pprint.pprint(my_dict)

if __name__ == '__main__':
    main()
