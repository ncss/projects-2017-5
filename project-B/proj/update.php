<?php 

if(isset($_GET['new_score'])){
    $score = (string)$_GET['new_score'];
    echo $score;
    $file = fopen("score_1.txt", "w+");
    fwrite($file, $score); //Add the number of left to go
    fclose($file);
}
