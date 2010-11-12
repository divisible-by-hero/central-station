<?php

function isLoggedIn()
{
    $ci =& get_instance();
    $ci->load->library('users/users_lib');
    $loggedIn = $ci->users->isLoggedIn();
    return $loggedIn;
}


?>
