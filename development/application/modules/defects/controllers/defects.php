<?php
/**
 * Defect Controller
 *
 * @author Derek Stegelman
 * @package CI Defect Tracker
 * @subpackage Defects
 * @category Defect Controllers
 *
 * Last Modified Oct 7 2010
 *
 */
class Defects extends MY_Controller {


  

    public function index(){

        $this->data['defectData'] = $this->Defect_mdl->getDefect(0);
        $this->load->view('defectListing', $this->data);
    }

    
    public function view($defectID){

        $this->load->model('defect_mdl');
        $this->data['defectData'] = $this->Defect_mdl->getDefect($defectID);
        $this->load->view('singleDefect', $this->data);
        
    }

    public function viewDefect($filterID){

        
    }

    public function createDefect(){

        

    }
}
?>
