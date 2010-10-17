<?php
/**
 *
 * @name Users Controller
 * @author Derek Stegelman
 * @package CI Defect Tracker
 * @subpackage Users Module
 *
 * Last Updated October 16 2010
 *
 *
 */


class Users extends Controller {

    /*
     * Constructor - Load dependencies and other stuff.
     *
     *
     */

    function Users()
    {
        parent::Controller();
    }

    /*
     *
     * General Purpose Login for all modules
     *
     *
     * @params - Accepts Email/Pass, and passes them to the model/Lib.
     * @returns @void
     *
     * @todo EVERYTHING
     */


    public function login()
    {
        $this->load->library('form_validation');

        $this->form_validation->set_rules('userEmail', 'Email Address', 'required|valid_email|xss_clean');
        $this->form_validation->set_rules('userPassword', 'Password', 'required');

        if(!$this->form_validation->run())
        {
            $this->load->view('login');
        }
        else
        {
            // Call Login function
            $this->load->library('users_lib');
            $this->users_lib->userEmail = $this->input->post('userEmail');
            $this->users_lib->userPassword = $this->input->post('userPassword');
            
            $this->users_lib->login();
        }



        
    }


}
?>
