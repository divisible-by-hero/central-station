<?php
/* 
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 * Description of wiki
 *
 * @author derek
 */
class Wiki extends Controller {

    public function index(){
        $this->load->view('wikiPage');
    }


}
?>
