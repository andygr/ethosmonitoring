# Ethos monitoring Python Scripts



# Steps

## 1) In an server with Python 3 installed copy the following script in a folder:
rigmonit.py

Also create these files in the same folder (touch <file name>):
rig_cond.py
rig_thash.py
rig_algpu.py
rig_togpu.py
rig_alrigs.py
rig_torigs.py
rig_avgtemp.py
rig_hagpu.py


2) Run the script:
python rigmonit.py


3) The script will ask for the following ifo:
Enter Ethos Rig API URL: <you can get this by clicking the API in your ethos distro portal>
Enter your emails addess: <use your email>


4) Script will return some data from the API:
Retrieving...... <API URL>
****** Restults ******
.
.
.
.


5) Script will ask which metrics to monitor:
------------------------------------------------------------
   WHICH SETTING WOULD YOU LIKE TO MONITOR?
------------------------------------------------------------
1. Condition. The current condition is....
['mining']
2. Total Hash. The current total hash is....
[171.64]
3. Alive GPUs. The current alive GPUs are....
[6]
4. Total GPUs. The current total GPUs are....
[6]
5. Alive Rigs. The current alive rigs are....
[1]
6. Total Rigs. The current total rigs are....
[1]
7. Average GPU Temp. The current average GPU temp is....
[55.67]
8. Hash Per GPU. The current hash per GPU is....
['28.6']
------------------------------------------------------------
Enter your choice [1-8], or press [0] for exit: 


6) Input your selection and the script will ask the minimum or maximum value. 
If the current value change then you will get an email notification




7) Rigmonit script will append the following data (based on your input) to the individual monitoring scripts

example for how many alive GPUs are:
address = <ethos API address>
email = <your email>
string = '[6]'
value = 'alive_gpus'
minvalue = '4'



8) Create the log folder and the log files. Check step 9 



9) Create a cron job to export the results to log files

*/30 * * * * /usr/bin/python3 /home/python/rig_algpu.py > /home/python/logs/rig_algpu.log

*/30 * * * * /usr/bin/python3 /home/python/rig_alrigs.py > /home/python/logs/rig_alrigs.log

*/30 * * * * /usr/bin/python3 /home/python/rig_avgtemp.py > /home/python/logs/rig_avgtemp.log

*/30 * * * * /usr/bin/python3 /home/python/rig_cond.py > /home/python/logs/rig_cond.log

*/30 * * * * /usr/bin/python3 /home/python/rig_hagpu.py > /home/python/logs/rig_hagpu.log

*/30 * * * * /usr/bin/python3 /home/python/rig_thash.py > /home/python/logs/rig_thash.log

*/30 * * * * /usr/bin/python3 /home/python/rig_togpu.py > /home/python/logs/rig_togpu.log

*/30 * * * * /usr/bin/python3 /home/python/rig_torigs.py > /home/python/logs/rig_torigs.log




10) Install a web server

Apache is ok for this task



11) Install mail and mailutils

apt-get install mailutils



12) Rsync the scripts to the web server folder (add it in the cronjob)

* * * * * /usr/bin/rsync -a /home/python/logs/rig_* /var/www/html/stats/



13) Create an HTML page in the same folder with the log files (index.html). Use the raw page to see the source code

<!DOCTYPE html>
<html>
<head>
<style>
</style>
</head>
<body>
<center>

<h2> Ethos Monitoring Log Files</h2>
<br>
<a href="rig_algpu.log" target="_self">Available GPUs</a> 
</p>
<br>
<p>
<a href="rig_alrigs.log" target="_self">Available Rigs</a>
</p>
<br>
<p>
<a href="rig_avgtemp.log" target="_self">Average Tempreture</a>
</p>
<br>
<p>
<a href="rig_cond.log" target="_self">Condition of the Rig</a>
</p>
<br>
<p>
<a href="rig_hagpu.log" target="_self">Hash per GPU</a>
</p>
<br>
<p>
<a href="rig_thash.log" target="_self">Total Hash</a>
</p>
<br>
<p>
<a href="rig_togpu.log" target="_self">Total available GPUs</a>
</p>
<br>
<p>
<a href="rig_torigs.log" target="_self">Total available RIGs</a>
</p>
</center>
</body>
</html>




Finally if you are happy with the scripts, please donate something. Thank you in advance !!!!!!! :) 
0xd5c065aDD7468832C52997972E768db4928134af

Also check my other videos: https://www.youtube.com/channel/UCQY7kB87mg_A_vd85iTB0Dg


That's ALL folks!!!!
