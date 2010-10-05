<?php
/**
 * Description of status_mdl
 *
 * @author derek
 */
class Status_mdl extends CI_Model {

    var $statusID;
    var $statusName;
    var $statusTable;

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
