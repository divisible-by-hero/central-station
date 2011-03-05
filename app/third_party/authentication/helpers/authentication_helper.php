<?php

/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

function get_fully_qualified_name($user_id)
{
    $CI =& get_instance();
    $user_object = $CI->Authentication_mdl->get($user_id);
    foreach($user_object->result() as $user)
    {
        $first_name = $user->first_name;
        $last_name = $user->last_name;
    }
    
    return $first_name.' '.$last_name;
}
?>
