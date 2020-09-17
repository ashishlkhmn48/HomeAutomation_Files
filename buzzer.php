<?php
$state = $_POST["state"];
echo shell_exec("sudo python /var/www/html/buzzer.py '$state'");
if ($state=="on")
        echo "on";
else 
        echo "off";
?>


