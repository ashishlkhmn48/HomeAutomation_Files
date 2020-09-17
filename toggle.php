<?php
$state = $_POST["state"];
echo shell_exec("sudo python /var/www/html/toggle.py '$state'");
if ($state=="on")
	echo "led on";
else 
	echo "led off";

?>

