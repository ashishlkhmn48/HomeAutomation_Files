<?php


//database connection
$db_name = "id4109358_fcm_info";
$mysql_username = "id4109358_fcm_info";
$mysql_password = "ashish123";
$server_name = "localhost";
$conn = mysqli_connect($server_name, $mysql_username, $mysql_password, $db_name);

$temperature = $_POST["temperature"];
$humidity = $_POST["humidity"];
$date_time = $_POST["date_time"];


$path_to_fcm = "https://fcm.googleapis.com/fcm/send";
$server_key = 
"AAAApjK4aj0:APA91bHbJPVvlK5LjrmIipJFq3YpHpSSyXlPz4QGgBk7a5VHuo2XgMn9bxKIsq8lT6iAEuWyIzXCXjsj8vb-AovPAJGQ1fQX7xAQsH2qFj2RffH0-ypjHYFe6PnkNGCRO7_Bg68kbe5j";

$headers = array(
			"Authorization:key=" .$server_key,
			"Content-Type:application/json"
			);

$curl_session = curl_init();
	curl_setopt($curl_session, CURLOPT_URL, $path_to_fcm);
	curl_setopt($curl_session, CURLOPT_POST, true);
	curl_setopt($curl_session, CURLOPT_HTTPHEADER, $headers);
	curl_setopt($curl_session, CURLOPT_RETURNTRANSFER, true);
	curl_setopt($curl_session, CURLOPT_SSL_VERIFYPEER, false);    //Check its usage

$query = "select * from fcm_info_home_automation;";
$result = mysqli_query($conn,$query);
while($row = mysqli_fetch_array($result)){
	
	$fields = array(
		"to"=>$row["fcm_token"],
		"data"=>array("temperature"=>$temperature,"humidity"=>$humidity,"date_time"=>$date_time)
	);
	
	$details = json_encode($fields);
	curl_setopt($curl_session, CURLOPT_POSTFIELDS, $details);
	$result_curl = curl_exec($curl_session);

}
curl_close($curl_session);
mysqli_close($conn);
echo "success";
?>
