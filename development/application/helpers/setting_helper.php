<?php

function getSetting($settingName){
    $CI =& get_instance();
    $CI->load->library('settings');
    $settingValue = $CI->settings->getSetting($settingName);
    return $settingValue;
}




?>
