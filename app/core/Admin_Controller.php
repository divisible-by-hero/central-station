<?php


class Admin_Controller extends MY_Controller {

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
