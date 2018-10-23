import urllib.request
import json
import os

address = 'http://v1s10n.ethosdistro.com/?json=yes'
email = 'andre8525@hotmail.com'
string = '[1]'
value = 'total_rigs'
minvalue = '1'
                          
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
intfinal1 = list(map(int, final1))
strfinal1 = ''.join(str(v) for v in intfinal1)


if minvalue in strfinal1:
    check = 'No Problem'
else:
    os.system('echo "The monitoring system reported a problem with the Total Hash of the rig, check your rig portal"  | mail -v -s "ETHOS Worker 5f8cab Update" andre8525@hotmail.com')
    check = 'Yes... PROBLEM'
    



print('Ethos address: ', address)
print('Current Condition: ', strfinal1)
print('Notification is for: ', minvalue)
print('Is there a problem? ', check)
#print(type(string))
#print(type(final1))
