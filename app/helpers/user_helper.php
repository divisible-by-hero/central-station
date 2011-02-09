<?php

function isLoggedIn()
{
    $ci =& get_instance();
    $ci->load->library('users');

    // Call isLoggedIn Method

    $isLoggedIn = $ci->users->isLoggedIn();
    return $isLoggedIn;
}

function getUserName(){
    $userName = $this->session->userdata('username');
    return $userName;
}
function getUserID(){
    $userID = $this->session->userdata('userid');
    return $userID;
}

?>
