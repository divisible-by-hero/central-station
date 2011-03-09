<?php

/**
* iRoam
*
* iRoam is a simple web travel application.  Meant to help you share your trips with family and friends.
*
* @package		iRoam
* @version		1.0
* @author		Derek Stegelman <stegelman.com>
* @license		Apache License v2.0
* @copyright	2010 - 2011 iRoam
*/

// ----------------------------------------------------------------

/**
* Static Pages Controller
*
* @package		iRoam
* @category		Controllers
* @author		Derek Stegelman
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

function is_logged_in()
{
	$CI =& get_instance();
	$CI->load->library('session');
	if (! $CI->session->userdata('user_id'))
	{
		return FALSE;
	}
	return TRUE;
}

/** Optional Methods **/

function user_object($user_id)
{
	$CI =& get_instance();
	$CI->load->model('Authentication_mdl');
	return $CI->Authentication_mdl->get($user_id);
}


?>
