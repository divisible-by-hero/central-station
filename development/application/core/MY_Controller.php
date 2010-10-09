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

        // Set the Defect Table from settings.
        $this->Defect_mdl->defectTable = getSetting('defectTable');
    }
}
?>
