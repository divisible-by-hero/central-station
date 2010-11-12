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


class MY_Controller extends Controller {


    function  MY_Controller() {
        parent::Controller();
//        if (!isLoggedIn())
//        {
//            redirect('users/login');
//        }
        // Commented out until lib is done.
    }
}
?>
