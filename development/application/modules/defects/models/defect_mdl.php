<?php
/**
 * Description of defect_mdl
 *
 * @author derek
 */
class Defect_mdl extends CI_Model {

    // Vars

    var $defectID;
    var $defectTitle;
    var $defectCreatedDate;
    var $defectModifiedDate;
    var $defectDescription;
    var $defectProjectID;
    var $defectUserID;
    var $defectStatusID;
    var $defectPriorityID;
    var $defectTable;

    public function createDefect(){

        $defectData = array('defectTitle'=>$this->defectTitle);
        $insertString = $this->db->insert_string($this->defectTable, $defectData);
        log_message('info', 'Defect_mdl::createDefect executes query ' . $insertString);
        $this->db->query($insertString);

    }

    public function getDefect($defectID){
        $getDefectSQL = "SELECT * FROM $this->defectTable WHERE defectID = $defectID";
        $executeDefect = $this->db->query($getDefectSQL);
        return $executeDefect;
    }

}
?>
