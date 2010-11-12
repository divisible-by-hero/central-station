<?php

/**
 *
 * @name Asset Helper - Loads css, javascript, and common markup controls to a page with ease.
 *
 * @author Derek Stegelman
 * @package CI Defect Tracker
 * @subpackage Global Helpers
 *
 *
 * Last Modified Oct 8 2010
 *
 *
 *
 *
 */


function commonButton($controller, $text){

    $url = base_url() . $controller;
    $buttonMarkup = "<a href='$controller' class='button'><span>$text</span></a>";
    return $buttonMarkup;
}

function getJquery(){
    $jquery = "<script type='text/javascript' src='http://code.jquery.com/jquery-1.4.2.min.js'></script>";
    return $jquery;
}

function getJqueryUI(){
    $jqueryUI = "<script type='text/javascript' src='http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.5/jquery-ui.min.js'></script>";
    return $jqueryUI;
}

function js($url){
    $builtURL = base_url() . "assets/javascript/" . $url . ".js";
    $javascript = "<script type='text/javascript' src='$builtURL'></script>";
    return $javascript;
}

function css($fileName){
    $builtURL = base_url() . "assets/css/" . $fileName . ".css";
    $outputCSS = "<link href='$builtURL' type='text/css' rel='stylesheet'>";
    return $outputCSS;
}

function loadColorScheme($color){
    $colorStylesheet = base_url() . "assets/css/colorscheme/" . $color . ".css";
    $css = "<link href='$colorStylesheet' type='text/css' rel='stylesheet'>";
    return $css;
}

/* End of Asset_helper.php */

?>
