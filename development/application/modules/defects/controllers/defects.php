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
class Defects extends Controller {


   function Defects(){

       // Why can't I set this to a private __construct() ???
       parent::Controller();
       $this->load->model('Defect_mdl');
       $this->Defect_mdl->defectTable = $this->Settings_mdl->getSetting('defectTable');
   }

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
