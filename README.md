# Home Automation Files

<b>Note : </b>Use pip module to install required Python Libraries.
  
<h3>Electronics Components Control(ON/OFF) :</h3>
<ul>
<li><b>toggle.py : </b> Python code to toggle the state of the Pin to which the Electronics Component is Connected.</li>
<li><b>toggle.php : </b> Php code to accept the request over the Network to Toggle the Electronics Component.
  <br>
  It sends the toggle state to the Python File to work accordingly.</li>
</ul>

<h3>Fire Control System with Notifications :</h3>
<ul>
<li><b>DHT11.py : </b> Python code to get the Temperature of the Room at Certain intervals and Notify us if the Temperature is Beyond a thresold value.</li>
<li><b>notification_home_automation.php : </b> Php code on a Live Server to Send Notification to the User. (We can avoid use of other Server by using our own Server when it goes Online.)</li>
</ul>


<h3>Automatic Human Detection Outside the Door :</h3>
<ul>
<li><b>buzzer.py : </b> Python code to detect human being using a Ultrasonic Sensor and after 5 sec it automatically rings the bell of the house.</li>
</ul>
