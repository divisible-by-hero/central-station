<?php
/**
 *
 * @name Forum Controller
 * @author Derek Stegelman
 * @package CI Defect Tracker
 * @subpackage Forums Module
 *
 * Last Updated October 16 2010
 *
 *
 */

class Forum extends CI_Controller {

    function __construct(){
        parent::__construct();
    }

    function index()
    {
        $this->template->write_view('content', 'forums');
        $this->template->render();
    }




}
?>
