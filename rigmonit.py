import urllib.request
import json
from crontab import CronTab


# Ethos rig URL
address = input('Enter Ethos Rig API URL: ')
email = input('Enter your emails addess: ')
print('\n')
print('Retrieving......', address)
print('****** Restults ******')

# Check and parse the URL
try:
  js = urllib.request.urlopen(address)
  content = js.read()
  data = json.loads(content.decode("utf8"))
except:
  print('There is a problem with the URL you provided')

#Print JSON output
print(data)
print('\n')

#Define search for KEY in Dictionary
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


#Enter KEY for search                        
print (60 * '-')
print ("   WHICH SETTING WOULD YOU LIKE TO MONITOR?")
print (60 * '-')
print ("1. Condition. The current condition is....")
final1 = list(find("condition", data))
value1 = "condition"
str1 = ''.join(final1)
print(final1)
print ("2. Total Hash. The current total hash is....")
final2 = list(find("total_hash", data))
value2 = "total_hash"
flt2 = repr(final2)
print(final2)
print ("3. Alive GPUs. The current alive GPUs are....")
final3 = list(find("alive_gpus", data))
value3 = "alive_gpus"
flt3 = repr(final3)
print(final3)
print ("4. Total GPUs. The current total GPUs are....")
final4 = list(find("total_gpus", data))
value4 = "total_gpus"
flt4 = repr(final4)
print(final4)
print ("5. Alive Rigs. The current alive rigs are....")
final5 = list(find("alive_rigs", data))
value5 = "alive_rigs"
flt5 = repr(final5)
print(final5)
print ("6. Total Rigs. The current total rigs are....")
final6 = list(find("total_rigs", data))
value6 = "total_rigs"
flt6 = repr(final6)
print(final6)
print ("7. Average GPU Temp. The current average GPU temp is....")
final7 = list(find("avg_temp", data))
value7 = "avg_temp"
flt7 = repr(final7)
print(final7)
print ("8. Hash Per GPU. The current hash per GPU is....")
final8 = list(find("per_hash-gpu", data))
value8 = "per_hash-gpu"
str8 = ''.join(final8)
print(final8)
print (60 * '-')

#Validate the selection number
def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("Not an integer! Try again.")
       continue
    else:
       return userInput 
       break 

choice = inputNumber("Enter your choice [1-8], or press [0] for exit: ")

choice_notinrange = 0
while choice_notinrange != choice:
    if (choice<=8):
       print("Initializing monitoring .......")
       if choice == 1:
           print ("You selected to Monitor: Condition")
           print ("Monitoring have started and will use the email ", email ,"for notifications.....")
           with open( 'rig_cond.py', 'r+' ) as f:
                file_data = f.read()
                f.seek(45, 0)
                f.write("address = " + "'" + address + "'" + '\n' )
                f.write("email = " + "'" + email + "'" + '\n' )
                f.write("string = " + "'" + str1 + "'" + '\n' )  
                f.write("value = " + "'" + value1 + "'" + '\n' )
                f.close()
           #cron = CronTab(user='andrew')
           #job = cron.new(command='/usr/bin/python /home/environments/example_cron.py')
           #job.minute.every(1)
           #cron.write()
       elif choice == 2:
           print ("You selected to Monitor: Total Hash")
           minvalue1 = int(input("Please provide the minimum value:"))
           minval1 = repr(minvalue1)
           print ("Monitoring have started and will use the email ", email ,"for notifications.....")
           with open( 'rig_thash.py', 'r+' ) as f:
                file_data = f.read()
                f.seek(45, 0)
                f.write("address = " + "'" + address + "'" + '\n' )
                f.write("email = " + "'" + email + "'" + '\n' )
                f.write("string = " + "'" + flt2 + "'" + '\n' )
                f.write("value = " + "'" + value2 + "'" + '\n' )
                f.write("minvalue = " + "'" + minval1 + "'" + '\n' )
                f.close()
       elif choice == 3:
           print ("You selected to Monitor: Alive GPUs")
           minvalue2 = int(input("Please provide the minimum value:"))
           minval2 = repr(minvalue2)
           print ("Monitoring have started and will use the email ", email ,"for notifications.....")
           with open( 'rig_algpu.py', 'r+' ) as f:
                file_data = f.read()
                f.seek(45, 0)
                f.write("address = " + "'" + address + "'" + '\n' )
                f.write("email = " + "'" + email + "'" + '\n' )
                f.write("string = " + "'" + flt3 + "'" + '\n' )
                f.write("value = " + "'" + value3 + "'" + '\n' )
                f.write("minvalue = " + "'" + minval2 + "'" + '\n' )
                f.close()
       elif choice == 4:
           print ("You selected to Monitor: Total GPUs")
           minvalue3 = int(input("Please provide the minimum value:"))
           minval3 = repr(minvalue3)
           print ("Monitoring have started and will use the email ", email ,"for notifications.....")
           with open( 'rig_togpu.py', 'r+' ) as f:
                file_data = f.read()
                f.seek(45, 0)
                f.write("address = " + "'" + address + "'" + '\n' )
                f.write("email = " + "'" + email + "'" + '\n' )
                f.write("string = " + "'" + flt4 + "'" + '\n' )
                f.write("value = " + "'" + value4 + "'" + '\n' )
                f.write("minvalue = " + "'" + minval3 + "'" + '\n' )
                f.close()
       elif choice == 5:
           print ("You selected to Monitor: Alive Rig")
           minvalue4 = int(input("Please provide the minimum value:"))
           minval4 = repr(minvalue4)
           print ("Monitoring have started and will use the email ", email ,"for notifications.....")
           with open( 'rig_alrigs.py', 'r+' ) as f:
                file_data = f.read()
                f.seek(45, 0)
                f.write("address = " + "'" + address + "'" + '\n' )
                f.write("email = " + "'" + email + "'" + '\n' )
                f.write("string = " + "'" + flt5 + "'" + '\n' )
                f.write("value = " + "'" + value5 + "'" + '\n' )
                f.write("minvalue = " + "'" + minval4 + "'" + '\n' )
                f.close()
       elif choice == 6:
           print ("You selected to Monitor: Total Rigs")
           minvalue5 = int(input("Please provide the minimum value:"))
           minval5 = repr(minvalue5)
           print ("Monitoring have started and will use the email ", email ,"for notifications.....")
           with open( 'rig_torigs.py', 'r+' ) as f:
                file_data = f.read()
                f.seek(45, 0)
                f.write("address = " + "'" + address + "'" + '\n' )
                f.write("email = " + "'" + email + "'" + '\n' )
                f.write("string = " + "'" + flt6 + "'" + '\n' )
                f.write("value = " + "'" + value6 + "'" + '\n' )
                f.write("minvalue = " + "'" + minval5 + "'" + '\n' )
                f.close()
       elif choice == 7:
           print ("You selected to Monitor: Average GPU Temp")
           maxvalue6 = int(input("Please provide the maximum value:"))
           maxval6 = repr(maxvalue6)
           print ("Monitoring have started and will use the email ", email ,"for notifications.....")
           with open( 'rig_avgtemp.py', 'r+' ) as f:
                file_data = f.read()
                f.seek(45, 0)
                f.write("address = " + "'" + address + "'" + '\n' )
                f.write("email = " + "'" + email + "'" + '\n' )
                f.write("string = " + "'" + flt7 + "'" + '\n' )
                f.write("value = " + "'" + value7 + "'" + '\n' )
                f.write("maxvalue = " + "'" + maxval6 + "'" + '\n' )
                f.close()
       elif choice == 8:
           print ("You selected to Monitor: Hash Per GPU")
           minvalue7 = int(input("Please provide the minimum value:"))
           minval7 = repr(minvalue7) 
           print ("Monitoring have started and will use the email ", email ,"for notifications.....")
           with open( 'rig_hagpu.py', 'r+' ) as f:
                file_data = f.read()
                f.seek(45, 0)
                f.write("address = " + "'" + address + "'" + '\n' )
                f.write("email = " + "'" + email + "'" + '\n' )
                f.write("string = " + "'" + str8 + "'" + '\n' )
                f.write("value = " + "'" + value8 + "'" + '\n' )
                f.write("minvalue = " + "'" + minval7 + "'" + '\n' )
                f.close()
       break
    else:
       print("Your choice is out of range, please try again.....")
       choice = inputNumber("Enter your choice [1-8]: ")


      








