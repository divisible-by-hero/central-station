<?php
/**
 * 
 * @name Defect Model
 * @author Derek Stegelman
 * @package CI Defect Tracker
 * @subpackage Defect Module
 * @version 1.0
 *
 * Last Updated October 25, 2010
 * @todo Document
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

    // Object Table
    
    private $defectTable;

    // Contruct

    public function __construct()
    {
        parent::CI_Model();
        $this->defectTable = $this->config->item('defectTable');
    }
    /**
     *
     * @name create()
     * @param void
     *
     *
     *
     */
    public function create(){
        $defectData = array('defectTitle'=>$this->defectTitle);
        $this->db->insert($this->defectTable, $defectData);
        
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
