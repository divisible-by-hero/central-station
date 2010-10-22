<?php
/**
 *
 * @name Defect_lib
 * @package CI Defect Tracker
 * @author Derek Stegelman
 *
 * Last Modified October 22 2010
 *
 */

class Defect_lib {

    // CI Super object

    private $ci;

    // Defect Properties

    var $defectID;
    var $defectTitle;
    var $defectCreatedDate;
    var $defectModifiedDate;
    var $defectDescription;
    var $defectProjectID;
    var $defectUserID;
    var $defectStatusID;
    var $defectPriorityID;

    public function Defect_lib()
    {
        // Contructor..
        $this->ci =& get_instance();  
    }

    /*
     * create()
     * @returns void
     * @params All properites of the defect library object
     *
     * Creates a defect, uses model methods to interact with the database.
     *
     */

    public function create()
    {
        // Instantiate the object

        $this->ci->load->model('Defect_mdl');

        // Load the Variables

        $this->ci->Defect_mdl->defectTitle = $this->defectTitle;
        $this->ci->Defect_mdl->defectCreatedDate = date("m/d/y");
        $this->ci->Defect_mdl->defectDescription = $this->defectDescription;
        $this->ci->Defect_mdl->defectProjectID = $this->defectProjectID;
        $this->ci->Defect_mdl->defectUserID = $this->defectUserID;
        $this->ci->Defect_mdl->defectStatusID = $this->defectStatusID;
        $this->ci->Defect_mdl->defectPriorityID = $this->defectPriorityID;

        // Execute Create

        $this->ci->Defect_mdl->create();
    }

    public function getDefect($defectID = null)
    {

        // Instantiate object

        $this->ci->load->model('Defect_mdl');

        // Grab the data

        $defectInfo = $this->ci->Defect_mdl->read($defectID);
        return $defectInfo;
    }

    public function delete()
    {
        // Instantiate object

        $this->ci->load->model('Defect_mdl');

        // Load the object

        $this->ci->Defect_mdl->defectID = $this->defectID;

        // Fire the method

        $this->ci->Defect_mdl->delete();
    }


}
?>
