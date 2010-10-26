<?php
/**
 * @name Priority Table
 * @package CI Defect Tracker
 * @author Derek Stegelman
 *
 * Last updated October 25, 2010
 *
 */
class Priority_mdl extends CI_Model {

    var $priorityID;
    var $priorityName;
    

    // Object Table

    private $priorityTable;

    public function  __construct() {
        parent::CI_Model();
        $this->priorityTable = $this->config->item('priorityTable');

    }
    
    // @todo CRUD

    public function getPriority($priorityID){

        if ($priorityID == 0){

            $prioritySQL = "SELECT * FROM $this->priorityTable";

        } else {

            $prioritySQL = "SELECT * FROM $this->priorityTable WHERE priorityID = $priorityID";

        }

        log_message('info', 'Priority_mdl::getPriority() executing a query ' . $prioritySQL);
        $priorityData = $this->db->query($prioritySQL);

        return $priorityData;

    }


}
?>
