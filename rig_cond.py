import urllib.request
import json
import os






                                       
def find(key, dictionary):
    for k, v in dictionary.items():
        if k == key:
            yield v
        elif isinstance(v, dict):
            for result in find(key, v):
                yield result
        elif isinstance(v, list):
            for d in v:
              if isinstance(d, dict):
                  for result in find(key, d):
                     yield result


js = urllib.request.urlopen(address)
content = js.read()
data = json.loads(content.decode("utf8"))


final1 = list(find(value, data))


if string in final1:
    check = 'No Problem'
else:
    os.system('echo "The monitoring system reported a problem with the condition of the rig, check your rig portal"  | mail -v -s "ETHOS Worker 5f8cab Update" andre8525@hotmail.com')
    check = 'Yes.. PROBLEM'
    



print('Ethos address: ', address)
print('Current Condition: ', final1)
print('Notification is for: ', string)
print('Is there a problem? ', check)

