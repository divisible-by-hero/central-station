<?php

function getSetting($settingName){
    $CI =& get_instance();
    $CI->load->model('Setting_mdl');
    $settingValue = $CI->Setting_mdl->getSetting($settingName);
    return $settingValue;
}




?>
