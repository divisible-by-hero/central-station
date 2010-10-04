<?php
/* 
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 * Description of defects
 *
 * @author derek
 */
class Defects extends Controller {
    //put your code here

    public function index(){
        $this->load->view('defectListing');
    }

    public function test(){
        $this->load->view('defectListing');
    }
}
?>
