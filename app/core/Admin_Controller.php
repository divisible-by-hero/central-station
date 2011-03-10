<?php


class Admin_Controller extends CoreController {

    public function  __construct() {
        parent::__construct();
        if(isLoggedIn() == TRUE){
            
            $this->template->set_template('admin');
        } else {
            redirect('login');
        }
    }
}
?>
