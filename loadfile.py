import json

def load():
    with open('data.json') as f:
        data = json.load(f)
    print('\n\nGet data         [success]')
    return(data)
