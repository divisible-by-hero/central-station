<?php
/**
 * Description of defects
 *
 * @author derek
 */
class Defects extends Controller {


    private function  __construct() {
        parent::Controller();
        $this->load->model('Defect_mdl');
        
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
