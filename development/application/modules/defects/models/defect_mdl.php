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
    private $defectTable;

    function Defect_mdl()
    {
        $this->defectTable = $this->config->item('defectTable');
    }

    public function create(){
        $defectData = array('defectTitle'=>$this->defectTitle);
        $insertString = $this->db->insert($this->defectTable, $defectData);
        log_message('info', 'Defect_mdl::createDefect executes query ' . $insertString);
        
    }

    public function read($defectID = null){

        if($defectID != null){

            //Select certain defect

           $defects = $this->db->get_where($this->defectTable, array('defectID'=>$defectID));

            // @todo rewrite with active record
        } else {

            $defects = $this->db->get($this->defectTable);

        }
        return $defects;
    }

    public function update()
    {
        $data = array('defectTitle'=>$this->defectTitle,
                      'defectModifiedDate'=>$this->defectModifiedDate,
                      'defectDescription'=>$this->defectDescription,
                      'defectProjectID'=>$this->defectProjectID,
                      'defectUserID'=>$this->defectUserID,
                      'defectStatusID'=>$this->defectStatusID,
                      'defectPriorityID'=>$this->defectPriorityID);
        $this->db->where('defectID', $this->defectID);
        $this->db->update($this->defectTable, $data);
    }

    public function delete()
    {
        $this->db->where('defectID', $this->defectID);
        $this->db->delete($this->defectTable);
    }
}
?>
