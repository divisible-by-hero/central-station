<?php
/**
 * Defect Controller
 *
 * @author Derek Stegelman
 * @package CI Defect Tracker
 * @subpackage Defects
 * @category Defect Controllers
 *
 * Last Modified Oct 16 2010
 *
 */
class Defects extends MY_Controller {


    /*
     * Contructor - Load dependencies/models and such.
     *
     */

    function Defects()
    {
        parent::MY_Controller();
        $this->load->library('defect_lib');
        $this->data['defectName'] = getSetting('defectName');

    }
    
    public function index(){

        $this->data['defectData'] = $this->defect_lib->getDefect();
        $this->load->view('defectListing', $this->data);
    }

    
    public function view($defectID){

        
        $this->data['defectData'] = $this->defect_lib->getDefect($defectID);
        $this->load->view('singleDefect', $this->data);
        
    }

    public function create()
    {
        // Instantiate form validation library

//        $this->load->library('form_validation');
//
//        // Set form validation rules
//
//        //$this->form_validation->set_rules('defectTitle', 'Defect Title', 'required|xss_clean');
//
//
//
//        // Run
//
//        if(!$this->form_validation->run())
//        {
//            $this->load->view('modals/addDefectModal');
//        }
//        else
//        {
//            // Instantiate the object
//
//            $this->defect_lib->defectTitle = $this->input->post('defectTitle');
//
//            // Create the defect
//
//            $this->defect_lib->create();


        //}
        $this->load->view('defects/modals/addDefectModal');
    }

 
}
?>
