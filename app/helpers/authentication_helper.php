<?php
/* 
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
function isLoggedIn()
{
    $CI =& get_instance();
    $CI->load->library('authentication');
    $loggedIn = $CI->authentication->is_loggedin();
    return $loggedIn;
}


?>
