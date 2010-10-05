<?php
/**
 * Description of defects
 *
 * @author derek
 */
class Defects extends Controller {


    private function __construct(){
        parent::Controller();
    }

    public function index(){
        $this->load->view('defectListing');
    }

    public function view($defectID){

        $this->load->model('defect_mdl');
        $defectData = $this->Defect_mdl->getDefect($defectID);
        
    }
}
?>
