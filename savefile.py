import json

def save(x):
    with open('data.json', 'w') as writeing:
        json.dump(x, writeing, indent=4)
    print('Save data        [success]')