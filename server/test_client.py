import requests
import json

# turtle command to be sent
commands = {
        'linear': {
            'x': 0,
            'y': 0,
            'z': 0
        },
        'angular': {
            'x': 0,
            'y': 0,
            'z': 0
        }
}
#our server url and turtle id
url = 'http://localhost:3000'
tid = 1

# register the turtle with the server
r = requests.post(url, json = {'id': tid})
# print the response
print r.text

i = 0
while True:
    # alternate commands to draw a shape
    i += 1
    if i % 2 == 1:
        commands['linear']['x'] = 2
        commands['angular']['z'] = 0
    else:
        commands['linear']['x'] = 0
        commands['angular']['z'] = 2

    # send the command to the server
    r = requests.post(url + '/command', json = {'id': tid, 'commands': commands})
    # parse and print the json response
    data = json.loads(r.text)
    print data
