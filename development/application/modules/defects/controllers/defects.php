<?php
/**
 * Description of defects
 *
 * @author derek
 */
class Defects extends Controller {


    

    public function index(){
        $this->load->view('defectListing');
    }

    public function view($defectID){

        $this->load->model('defect_mdl');
        $this->data['defectData'] = $this->Defect_mdl->getDefect($defectID);
        $this->load->view('singleDefect', $this->data);
        
    }

    public function viewDefect($filterID){

        
    }
}
?>
