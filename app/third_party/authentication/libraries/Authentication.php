<?php
/**
 * Auth Package
 * 
 * @package Authentication
 * @version 1.0
 * @author Derek Stegelman
 * @copyright 2011 Derek Stegelman
 * @link http://stegelman.com
 */

namespace Authentication;

// ------------------------------------------------------------------------

/**
 * Authencation
 * 
 * @package Authentication
 * @author Derek Stegelman
 * 
 * Dependencies
 *  - CI 2.0 with package support
 *  - Derek Stegelman's Core Model
 * 
 */



class Authentication {
    
    /**
     *
     * @var object   CI Super object
     */
    private $_ci;
    
    /**
     * 
     * Constructor - Grab and load dependencies.
     * 
     */
    
    public function __construct() {
        $this->_ci =& get_instance();
        $this->_ci->load->model('Authentication_mdl');
        $this->_ci->load->config('auth');
        $this->_ci->load->library('session');
    }
    
    private function generate_salt()
    {
        $this->ci->load->helper('string');
        return sha1(random_string('alnum', 32));
    }
    
    /*
     * log_in()
     * @var $identity_field  and $password
     * @author Derek Stegelman
     * @returns user_id or -1 if failed int
     */
    
    public function log_in($identity, $password)
    {
        // Check for user for username first
	$user_object = $this->ci->Authentication_mdl->getWhere('username', $identity);
        
        if ($user_object->num_rows() !==1)
        {
            // Check for the email now.
            $user_object = $this->ci->Authentication_mdl->getWhere('email', $identity);
            if ($user_object->num_rows() !==1)
            {
                // Okay now we really couldn't find the user.  Bastard.
                log_message('info', 'User ' . $identity . ' was not found.');
                return -1;
            }
            
        }

	if (sha1($password.$user_object->row('salt')) == $user_object->row('password'))
	{
		$data = array(
			'user_id'   => $user_object->row('user_id'),
			'username'  => $user_object->row('username'),
			'email'     => $user_object->row('email'),
			'salt'      => $user_object->row('salt'),
		);
		
		$this->ci->session->set_userdata($data);
		
		return $user_object->row('user_id');
	}
        log_message('info', 'User ' . $identity . ' could not be authenticated.');
	return -1;
    }
    
    /**
     * Register
     * 
     * @author Derek Stegelman
     * 
     * @param string $username
     * @param string $email
     * @param string $password
     * @param string $first_name
     * @param string $last_name 
     */
    
    public function register($username, $email, $password, $first_name, $last_name)
    {
        if ($this->_ci->Authentication_mdl->exist('username', $username) OR $this->_ci->Authentication_mdl->exist('email', $email))
        {
            return FALSE;
        }
        
        $user_salt = $this->generate_salt();
        
        
        $user_data = array('username'=>$username, 'email'=>$email, 'salt'=>$user_salt, 'password'=>sha1($password.$user_salt),
                           'first_name'=>$first_name, 'last_name'=>$last_name);
        
        // Create user 
        return $this->_ci->Authentication_mdl->create($user_data);
        
    }
    
    public function log_out()
    {
        $this->ci->session->sess_destroy();
    }
    
    public function is_logged_in()
    {
        if(! $this->ci->session->userdata('user_id'))
        {
            return FALSE;
        }
        
        return TRUE;
    }
}