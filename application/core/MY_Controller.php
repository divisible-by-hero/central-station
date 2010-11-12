<?php defined('BASEPATH') OR exit('No direct script access allowed');
/**
 *
 * @name MY_Controller
 * @author Derek Stegelman
 * @package CI Defect Tracker
 * @subpackage Class Extensions
 *
 * Last Updated October 8, 2010
 *
 */


class MY_Controller extends CI_Controller {


    function  MY_Controller() {
        parent::CI_Controller();
//        if (!isLoggedIn())
//        {
//            redirect('users/login');
//        }
        // Commented out until lib is done.
    }
}
?>
