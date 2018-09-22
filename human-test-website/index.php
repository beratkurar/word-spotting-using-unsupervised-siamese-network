
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
   "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

<html xmlns = "http://www.w3.org/1999/xhtml">

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
<form action="action.php" method="post">
<b>What is your name?</b><br>
<input type="text" name="name"><br>
<br>
<br>

<fieldset style="width:400px">
<legend><b>Are these images in correct order?</b></legend>
<table>

<?php

$folders=array("pairs/0-1", "pairs/1-0","pairs/2-1","pairs/3-0","pairs/4-0","pairs/5-1","pairs/6-0","pairs/7-0",
"pairs/8-0","pairs/9-0","pairs/11-0","pairs/12-1","pairs/14-0","pairs/15-0","pairs/16-1",
"pairs/17-0","pairs/18-1","pairs/19-1","pairs/22-0","pairs/26-0");
$c=1;
foreach($folders as $folder)
{
?>
<tr>

<td><b><?php echo $c; ?></b></td>
<td width="110px" height="80px">
<img src=<?php echo $folder."/l.png"; ?> />
</td>

<td width="110px" height="80px">
<img src=<?php echo $folder."/r.png"; ?> />
</td>

<td width="100px">
<input type="radio" name=<?php echo $folder; ?> value="yes" checked>Yes<br>
<input type="radio" name=<?php echo $folder; ?>  value="no">No<br>
</td>

</tr>
<?php $c=$c+1;} ?>

<tr>
<td><input type="submit" value="Submit">
</td></tr>
</table>
</fieldset>
</form>

</div>
</body>
</html>