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
class Authentication_mdl extends CoreModel {
    //put your code here
    
    public function __construct() {
        parent::__construct();
        $this->load->config('auth');
        $this->_table = $this->config->item('user_table');
    }
    
}

?>
