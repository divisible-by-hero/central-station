<?php

function isLoggedIn()
{
    $ci =& get_instance();
    $ci->load->library('users');
    $loggedIn = $ci->users->isLoggedIn();
    return $loggedIn;
}


?>
