<?php

/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 * Description of authentication_mdl
 *
 * @author Derek
 */
class Authentication_mdl extends CoreModel {
    //put your code here
    
    public function __construct() {
        parent::__construct();
        $this->load->config('auth');
        $this->_table = $this->config->item('user_table');
    }
    
}

?>
