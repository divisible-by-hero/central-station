<?php
/**
 * @name Status Model
 * @package CI Defect Tracker
 * @subpackage Defect Module
 * @version 1.0
 *
 * @author Derek Stegelman
 *
 * Last udpated October 25, 2010
 * @todo Document and finish CRUD.
 */

class Status_mdl extends CI_Model {

    var $statusID;
    var $statusName;

    // Object table

    private $statusTable;

    // Constructor

    public function  __construct() {
        parent::CI_Model();
        $this->statusTable = $this->config->item('statusTable');
    }

    // @todo CRUD

    public function getStatus($statusID){

        if($statusID == 0){

            $statusSQL = "SELECT * FROM $this->statusTable";


        } else {

            $statusSQL = "SELECT * FROM $this->statusTable WHERE statusID = $statusID";
        }

        log_message('info', 'Status_mdl::getStatus() executing query ' . $statusSQL);
        $statusData = $this->db->query($statusSQL);

        return $statusData;



    }


}
?>
