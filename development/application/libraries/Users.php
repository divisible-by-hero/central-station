<?php

/**
 * @name User Library
 *
 * @author Derek Stegelman
 * @package CI Defect Tracker
 * @subpackage Libraries
 *
 * Last Modified Oct 16 2010
 *
 */

class Users {

    /*
     * CI Super Object
     *
     *
     */


    private $ci;


    /*
     *  Define Users Table
     *
     */

    private $userTable;


    // User Properties

    var $userEmail;
    var $userUserID;
    var $userName;
    var $userPassword;
    var $userGroupID;
    var $userLastName;
    var $userFirstName;
    var $userDateCreated;
    var $userTable;

    function Users(){
        $ci =& get_instance();
        $this->userTable = $this->ci->config->item('userTable');

    }

    /*
     * Login
     * @params, User Object
     * @returns useriD - -1 if authentication fails.
     *
     * @todo - Salt/hash.
     */

    

    

    function login(){

           // Check the Username and Password against the Database

        // Encrypt the given Password so it can be
        // compared to the one in the database.

        // Grab User info for this Username
        //The Code block below is replacing validation for the moment.


        if (isset($this->userEmail)){

        } else {
            log_message('debug', 'User_mdl: No useremail supplied.');
            return -1;
        }
        if (isset($this->userPassword)){

        } else {
            log_message('debug', 'User_mdl: No password supplied.');
            return -1;
        }


         // Set the Users Table.

        // Build The select query.

        $UserQuery = "SELECT email, pass, userID FROM
        $this->userTable WHERE email = '$this->userEmail' LIMIT 1";

        // Exectute Query

        $query = $this->db->query($UserQuery);

        if ($query->num_rows() == 0){
            log_message('debug', 'User_mdl: $query->num_rows() returned a null or 0 value.');
            return -1; // This indicates that the query returned no records.  ERROR.
        } else {}
        $getUsersInfo = $this->db->query($UserQuery);
        log_message('debug', 'User_mdl: Executing query to find password. ' . $UserQuery);

        // Get The Info

        foreach ($getUsersInfo->result() as $row){
            $dbPassword = $row->pass; // Fetched Password
            $dbUserID = $row->userID; // Fetched User ID
            $dbEmail = $row->email;

        }

        // Decode password.

        $unencryptPass = $this->encrypt->decode($dbPassword);


        // Check the password against the password provided.

        if ($unencryptPass == $this->userPassword){

            // User Is Authenticated
            log_message('debug', 'User_mdl: User ' . $this->userEmail . ' has logged in successfully.');
            $newdata = array(
                   'isLoggedIn'  => '1',
                   'email'=> $dbEmail,
                   'userid'=> $dbUserID,

               );

        $this->session->set_userdata($newdata);

            return $dbUserID;

        }
        else
        {
            log_message('debug', 'User_mdl: User ' . $this->userEmail . ' could no be authenticated.');
            return -1;
        }

    }

    // Logout Method

    function logout(){

        // Destroy Session Data

        $this->session->sess_destroy();

    }

    function isLoggedIn(){
        log_message('debug', 'isLoggedIn method hit');
        if ($this->session->userdata("isLoggedIn") == 1){
            return TRUE;
        } else {
            return FALSE;
        }
    }

    function register(){


        date_default_timezone_set('UTC');
        $this->userDateCreated = date("m/d/y");


            //Start Registration.

            $encryptPassword = $this->encrypt->encode($this->userPassword);
            $userData = array('email'=>$this->userEmail, 'pass'=>$encryptPassword,
                'firstName'=>$this->userFirstName, 'lastName'=>$this->userLastName,
                'dateCreated'=>$this->userDateCreated);

            $userInsert = $this->db->insert_string($this->userTable, $userData);
            $this->db->query($userInsert);
    }

    function getUsers(){
        $select = "SELECT * FROM $this->userTable";
        log_message('info', 'User_mdl::getUsers() is executing a query ' . $select);
        $dump = $this->db->query($select);
        return $dump;
    }

    function getUserInfo($userID){
        $select = "SELECT * FROM $this->userTable WHERE userID = $userID LIMIT 1";
        log_message('info', 'User_mdl::getUserInfo() is executing a query ' . $select);
        $dump = $this->db->query($select);
        return $dump;
    }

    function getUserPassword($userID){
        $select = "SELECT * FROM $this->userTable WHERE userID = $userID LIMIT 1";
        log_message('info', 'User_mdl::getUserPassword() is executing a query ' . $select);
        $dump = $this->db->query($select);
        foreach($dump->result() as $row){
            $encryptPass = $row->pass;
        }

        $decode = $this->encrypt->decode($encryptPass);
        return $decode;
    }


    function getCurrentUser(){
        $this->userUserID = $this->session->userdata('UserID');

        $userQuery = "SELECT email FROM $this->userTable WHERE userID = $this->userUserID LIMIT 1";

        $executeQuery = $this->db->query($userQuery);
        foreach ($executeQuery->result() as $row){
            $this->userEmail = $row->Email;
        }
        return $this->userEmail;
    }

    function saveUser(){

        $encryptPass = $this->encrypt->encode($this->userPassword);

        $data = array('email'=>$this->userEmail, 'pass'=>$encryptPass, 'firstName'=>$this->userFirstName, 'lastName'=>$this->userLastName);
        $where = "userID = $this->userUserID";
        $updateString = $this->db->update_string($this->userTable, $data, $where);
        log_message('info', 'User_mdl::saveUser() is trying to execute a query ' . $updateString);
        $this->db->query($updateString);
    }

    function deleteUser(){
        $delete = "DELETE FROM $this->userTable WHERE userID = $this->userUserID";
        log_message('info', 'User_mdl::deleteUser() is trying to execute a query ' . $delete);
        $this->db->query($delete);
    }

    function changePassword($oldPassword, $newPassword, $userEmail){

        $this->userEmail = $userEmail;

        $getOldPassword = "SELECT * FROM $this->userTable WHERE email = $this->userEmail";
        $getPass = $this->db->query($getOldPassword);
        foreach ($getPass->result() as $row){
            $dbOldPassword = $row->Pass;
        }
        if ($oldPassword == $dbOldPassword){
            // Continue changing the password
            $setData = array('Pass'=>$newPassword);
            $setQuery = $this->db->update_string($setData, $userTable);
            $this->db->query($setQuery);
        } else {
            return -1;
        }
    }

    function resetPassword($password){

        $pass_encrypt = $this->encrypt->encode($password);
        $data = array('pass'=>$pass_encrypt);
        $where = "email = '$this->userEmail'";
        $setQuery = $this->db->update_string($this->userTable, $data, $where);
        $this->db->query($setQuery);
        $this->load->helper('email');
        if(valid_email($this->userEmail)){
            $this->load->library('email');

            $this->email->from('support@fotochest.com', 'FotoChest Support');
            $this->email->to($this->userEmail);


            $this->email->subject('Your Password has been reset.');
            $this->email->message('Your password has been set to ' . $password);

            $this->email->send();
            $message = $this->email->print_debugger();

            return $message;
        }

    }



    public function getUserName(){
        $userName = $this->session->userdata('username');
        return $userName;
    }
    public function getUserID(){
        $userID = $this->session->userdata('userid');
        return $userID;
    }

    public function getUserIDUsername($userName){
        $select = "SELECT userID FROM $this->userTable WHERE email = '$userName'";
        log_message('info', 'User_mdl::getUserIDUsername() is executing a query ' . $select);
        $dump = $this->db->query($select);
        foreach($dump->result() as $row){
            $userID = $row->userID;
            log_message('debug', 'User_mdl::getUserIDUsername() has fetched the userid ' . $userID);
        }
        return $userID;
    }

    function getFirstName(){
        $this->userUserID = $this->session->userdata('userid');

        $getName = "SELECT FirstName
        FROM $this->userTable
        WHERE UserID = $this->userUserID LIMIT 1";


        $excQuery = $this->db->query($getName);
        foreach ($excQuery->result() as $row){
            $firstName = $row->FirstName;

        }
        return $firstName;
    }



}
?>