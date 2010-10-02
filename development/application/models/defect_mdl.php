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

    }

    public function getDefect($defectID){
        $getDefectSQL = "SELECT * FROM $this->defectTable WHERE defectID = $defectID";
        $executeDefect = $this->db->query($getDefectSQL);
        return $executeDefect;
    }

}
?>
