<html>
<body>

<?php


$all_ip=array();#initialised an array to store IP values
$file = file("data.txt");
//print_r($file[0]);
foreach ($file as $line) { //loops through the line
  $values = explode(" ", $line);//stores value in a new array
  $all_ip[]=($values); // multi dimensional array.
}

print_r("<h2> No of Connections made: ".count($all_ip)) //prints total connection


//print_r($all_ip)
//print($all_ip[3][2]);
//print_r($all_ip[5][0])
//echo $all_ip[0][0]

//print_r("<select name='ip_value' onchange='myFunction()'>");
?>
<br>
<select name='ip_value' onchange='myFunction(this)'>

<?php
foreach($all_ip as $ip)
{
   echo "<option value='".$ip[0]."'>".$ip[0]."</option>";
}


?>
</select>

<!-- placeholder to show values -->
<h2 id='times'></h2> 
<h2 id ='first'></h2>
<h2 id ='last'></h2>
<script>
  function myFunction(select) {
    var x = select.value;
    <?php
      foreach ($all_ip as $ip) {
        echo "if (x == '".$ip[0]."') { document.getElementById('times').innerHTML = 'This IP has connected <i>".$ip[1]."</i> times'; 
          document.getElementById('first').innerHTML = 'First time connected on ".$ip[2],$ip[3]."'; 
          document.getElementById('last').innerHTML = 'Last time connection was on ".$ip[4],$ip[3]."'; 
        }"; //do not print $ip[5]
      }
    ?>
  }
</script>

</body>
</html>
