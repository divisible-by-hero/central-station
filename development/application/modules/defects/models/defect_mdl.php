<?php
/**
 * Description of defect_mdl
 *
 * @author Derek Stegelman
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

    function setTable($name){
        $this->defectTable = $name;
    }

    public function createDefect(){

        $this->defectCreatedDate = date("m/d/y");

        $defectData = array('defectTitle'=>$this->defectTitle);
        $insertString = $this->db->insert_string($this->defectTable, $defectData);
        log_message('info', 'Defect_mdl::createDefect executes query ' . $insertString);
        $this->db->query($insertString);

    }

    public function getDefect($defectID){

        if($defectID == 0){

            //Select All Defects

            $getDefectSQL = "SELECT * FROM $this->defectTable";

            // @todo rewrite with active record
        } else {

        $getDefectSQL = "SELECT * FROM $this->defectTable WHERE defectID = $defectID";

        }
        
        $executeDefect = $this->db->query($getDefectSQL);
        return $executeDefect;
    }

   

    

}
?>
