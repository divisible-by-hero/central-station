0<?php  if ( ! defined('BASEPATH')) exit('No direct script access allowed');

/**
* CI Base Core
*
* 
*
* @package		CodeIgniter Base
* @version		1.0
* @author		Derek Stegelman <stegelman.com>
* @license		Apache License v2.0
* @copyright		2010 Derek Stegelman
*/

// ----------------------------------------------------------------

/**
* Authentication Library
*
* @package		CodeIgniter Base
* @category		Libraries
* @author		Derek Stegelman
*/

class Authentication extends CoreLibrary {

    private $authTable;

    public function  __construct() {

        parent::__construct();
        log_message('info', 'auth   ' . $this->authTable);
    }

    public function login($email, $password)
    {

        // Must be refactored
        $qry = $this->ci->Authentication_mdl->getLogin($email);

	// No results, we're done.
        
	if ($qry->num_rows() !== 1)
	{
            log_message('info', 'user not found');
            return FALSE;

	}

	if (sha1($password.$qry->row('salt')) == $qry->row('password'))
	{
		$data = array(
			'user_id'		=> $qry->row('user_id'),
			'email'			=> $qry->row('email'),
			'salt'			=> $qry->row('salt'),
			'username'		=> $qry->row('username'),
			'isAdmin' 		=> $qry->row('isAdmin'),
		);

		$this->ci->session->set_userdata($data);
                log_message('info', 'authenticated.' . $qry->row('user_id'));
		return $qry->row('user_id');
	}
        log_message('info', 'auth failed');
	return FALSE;
    }

    public function logout()
    {
        $this->ci->session->sess_destroy();
    }

    public function is_loggedin()
    {

        if($this->ci->session->userdata('user_id') != 0)
        {
            return TRUE;
        }
        else
        {
            return FALSE;
        }

    }

    public function createUser($email, $password, $username, $firstname, $lastname)
    {

        //Refactor
         $qry = $this->ci->Authentication_mdl->checkUser($email);

        if ($qry->num_rows() !== 0)
        {
            return FALSE;
        }

        $salt = $this->_buildSalt();

        $data = array(
            'password'      => sha1($password.$salt),
            'email'         => $email,
            'username'      => $username,
            'firstName'     => $firstName,
            'lastName'      => $lastName,
            'salt'          => $salt,
            'status'        => 1,
        );

        // Call the create method.

        $id = $this->ci->Authentication_mdl->createUser($data);
        return $id;
        
    }

    public function forgotPassword()
    {

    }

    public function changePassword()
    {

    }

    private function _buildSalt()
    {
        $this->ci->load->helper('string');
        return sha1(random_string('alnum', 32));
    }
    

    

}
?>
