<?php


function commonButton($controller, $text){

    $url = base_url() . $controller;
    $buttonMarkup = "<a href='$controller' class='button'><span>$text</span></a>";
    return $buttonMarkup;
}

function getJquery(){
    $jquery = "<script type='text/javascript' src='http://code.jquery.com/jquery-1.4.2.min.js'></script>";
    return $jquery;
}

function js($url){
    $builtURL = base_url() . "assets/javascript/" . $url;
    $javascript = "<script type='text/javascript' src='$builtURL'></script>";
    return $javascript;
}

function css($fileName){
    $builtURL = base_url() . "assets/css/" . $fileName;
    $outputCSS = "<link href='$builtURL' type='text/css' rel='stylesheet'>";
    return $outputCSS;
}


?>
