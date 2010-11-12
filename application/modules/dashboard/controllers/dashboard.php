<?php
/**
 * 
 * @name Dashboard Controller
 * @author Derek Stegelman
 * @package CI Defect Tracker
 * @subpackage Dashboard Module
 * @category Dashboard Module Controllers
 *
 * Last Updated October 8 2010
 * 
 */


class Dashboard extends MY_Controller {
    

    function index(){
        $this->load->view('dashboard');
    }
}
?>
