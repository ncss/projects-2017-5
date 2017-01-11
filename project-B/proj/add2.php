<?php $fn = "score_2.txt"; 
$file = fopen($fn, "a+"); 
$size = filesize($fn); 

$count = (int)fread($file, $size); 
$count = (int)$count + 1;
if($_GET['add']){
    fclose($file); //Close currently open file (that is in read)
    $fh = fopen( 'score_2.txt', 'w+' ); //Open file and overwrite its content
    fclose($fh); //Close that file now that it has been overwritten
    $file = fopen($fn, "w+"); //Go back to the old file again (read)
    fwrite($file, $count); //Add the number of  left to go
}

fclose($file);