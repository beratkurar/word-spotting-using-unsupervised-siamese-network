<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
   "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

<html xmlns = "http://www.w3.org/1999/xhtml">
<?php
 $path = 'data.txt';
 if (!empty($_POST['name']) ) 
 {
    $answers =array($_POST['pairs/0-1'], $_POST['pairs/1-0'], $_POST['pairs/2-1'],
	 $_POST['pairs/3-0'], $_POST['pairs/4-0'], $_POST['pairs/5-1'], $_POST['pairs/6-0'], $_POST['pairs/7-0'],
	 $_POST['pairs/8-0'], $_POST['pairs/9-0'], $_POST['pairs/11-0'], $_POST['pairs/12-1'], $_POST['pairs/14-0'],
	 $_POST['pairs/15-0'], $_POST['pairs/16-1'], $_POST['pairs/17-0'], $_POST['pairs/18-1'], $_POST['pairs/19-1'],
	 $_POST['pairs/22-0'], $_POST['pairs/26-0']);
	 $corrects=array('yes','no','yes','no','no','yes','no','no','no','no','no','yes','no','no','yes','no','yes','yes','no', 'no' );
	 $n_right=0;
	 for( $i= 0 ; $i < 20 ; $i++ )
	 {
		 if ($answers[$i]==$corrects[$i])
		 {
			 $n_right=$n_right+1;
		 }
	 }
	 $perf=$n_right/20; 
	 
    $fh = fopen($path,"a+");
    $string ="\n".$_POST['name']."-performance-".$perf."\n".$_POST['pairs/0-1']."\n".$_POST['pairs/1-0']."\n".$_POST['pairs/2-1']."\n"
	.$_POST['pairs/3-0']."\n".$_POST['pairs/4-0']."\n".$_POST['pairs/5-1']."\n".$_POST['pairs/6-0']."\n".$_POST['pairs/7-0']."\n"
	.$_POST['pairs/8-0']."\n".$_POST['pairs/9-0']."\n".$_POST['pairs/11-0']."\n".$_POST['pairs/12-1']."\n".$_POST['pairs/14-0']."\n"
	.$_POST['pairs/15-0']."\n".$_POST['pairs/16-1']."\n".$_POST['pairs/17-0']."\n".$_POST['pairs/18-1']."\n".$_POST['pairs/19-1']."\n"
	.$_POST['pairs/22-0']."\n".$_POST['pairs/26-0']."\n";
    fwrite($fh,$string); // Write information to the file
    fclose($fh); // Close the file

	 
?>

<head>
<title>Visual Media Lab</title>
<link rel="stylesheet" type="text/css" href="style.css" />
</head>

<body>

<!--the most top white part -->
<div class="header"><h2 align="center">VISUAL MEDIA LAB <br> HUMAN PERFORMANCE EVALUATION</h2></div>


<div class="main">

<!--the menu part-->
<div class="menu">
<br/>
<a href="index.php">Test yourself</a>
</div>

<br/>

<b>Thank you for participating!</b>
<br/>
<br/>
<b><?php echo "Your performance is " . $perf; ?></b>

</div>
</body>
</html>
 <?php 
 }
 else
 {
?>
<head>
<title>Visual Media Lab</title>
<link rel="stylesheet" type="text/css" href="style.css" />
</head>

<body>

<!--the most top white part -->
<div class="header"><h2 align="center">VISUAL MEDIA LAB <br> HUMAN PERFORMANCE EVALUATION</h2></div>


<div class="main">

<!--the menu part-->
<div class="menu">
<br/>
<a href="index.php">Test yourself</a>
</div>

<br/>

<b>Please fill your name field</b>

</div>
</body>
</html>
<?php
 }
 
?>