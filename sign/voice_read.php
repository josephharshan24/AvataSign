<?php
extract($_REQUEST);
require_once('voicerss_tts.php');
?>
<html>
<head>
<title>Untitled Document</title>
</head>

<body>
<?php
$name=$mess;
$lg="en-us";

if($lang=="en")
{
$lg="en-us";
}
else if($lang=="fr")
{
$lg="fr-ch";
}
else
{
$lg=$lang."-in";
}

if($name!="")
{
$message=$name;
//en-us
$tts = new VoiceRSS;
$voice = $tts->speech(array(
    'key' => '84690531ea3147658ee11c95c69ed82f',
    'hl' => $lg,
    'src' => "$message",
    'r' => '0',
    'c' => 'mp3',
    'f' => '44khz_16bit_stereo',
    'ssml' => 'false',
    'b64' => 'true'
));

//echo '<audio src="' . $voice['response'] . '" autoplay="autoplay"></audio>';
?>
<embed src="<?php echo $voice['response']; ?>" autostart="true" width="60" height="40"></embed>

<?php
}
?>
<script>
						setTimeout(function () {
						   //Redirect with JavaScript
						 // window.location.href="voice_read.php?mess=<?php //echo $mess; ?>";
						//}, 10000);
						</script>
</body>
</html>
