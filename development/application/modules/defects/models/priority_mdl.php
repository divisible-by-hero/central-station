<?php
/**
 * Description of priority_mdl
 *
 * @author derek
 */
class Priority_mdl extends CI_Model {

    var $priorityID;
    var $priorityName;
    var $priorityTable;

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
