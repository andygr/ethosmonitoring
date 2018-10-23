# ethosmonitoring
Monitoring for Ethos rings by using Python and Email notifications

To use the scripts in your web server and monitor your rig, you will need to do the following:
1) Change the metrics in each of the scripts 
e.g.
address = use your ethos API 
email = use your email here
string = use the value that represents your setup. For example the alive GPUs is how many GPUs you have
value = this must be exactly as it is in the JSON API
minvalue = minimum value for notifications

example:
address = 'http://v1s10n.ethosdistro.com/?json=yes'
email = 'andre8525@hotmail.com'
string = '[6]'
value = 'alive_gpus'
minvalue = '4'


2) Put the script files and log files in an folder at home directory
e.g 
Script files = /home/python/
log files = /home/python/logs


2) Create a cron job to export the results to log files
*/30 * * * * /usr/bin/python3 /home/python/rig_algpu.py > /home/python/logs/rig_algpu.log
*/30 * * * * /usr/bin/python3 /home/python/rig_alrigs.py > /home/python/logs/rig_alrigs.log
*/30 * * * * /usr/bin/python3 /home/python/rig_avgtemp.py > /home/python/logs/rig_avgtemp.log
*/30 * * * * /usr/bin/python3 /home/python/rig_cond.py > /home/python/logs/rig_cond.log
*/30 * * * * /usr/bin/python3 /home/python/rig_hagpu.py > /home/python/logs/rig_hagpu.log
*/30 * * * * /usr/bin/python3 /home/python/rig_thash.py > /home/python/logs/rig_thash.log
*/30 * * * * /usr/bin/python3 /home/python/rig_togpu.py > /home/python/logs/rig_togpu.log
*/30 * * * * /usr/bin/python3 /home/python/rig_torigs.py > /home/python/logs/rig_torigs.log



3) Install a web server
Apache is ok for this task


4) Install mail and mailutils
apt-get install mailutils


5) Rsync the scripts to the web server folder (add it in the cronjob)
* * * * * /usr/bin/rsync -a /home/python/logs/rig_* /var/www/html/stats/


6) Create an HTML page (index.html)
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




p.s 
Also i uploaded the rigmonit python script that will generate all the python scripts that you want to use for your monitoring. You only need to provide the following and the script will do the rest for you:
address = input('Enter Ethos Rig API URL: ')
email = input('Enter your emails addess: ')

Also have a selection menu where you choose which metric you want to use and minimum values


Finally if you are happy with the scripts, please donate some ethereum so i can drink a beer :) 
0xd5c065aDD7468832C52997972E768db4928134af



That's ALL !!!!
