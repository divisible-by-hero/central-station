<?php
/**
* Open Cook Book
*
* Open Cook Book is a simple CodeIgniter based cooking application that stores recipes.
*
* @package		OpenCookBook
* @version		1.0
* @author		Derek Stegelman <fotochest.com|stegelman.com>
* @license		Apache License v2.0
* @copyright		2010 OpenCookBook
*/

// ----------------------------------------------------------------

/**
* Recipes Controller
*
* @package		OpenCookBook
* @category		Controllers
* @author		Derek Stegelman
*/

class CoreLibrary {

    public $ci;

    public function __construct()
    {
        $this->ci =& get_instance();
        log_message('info', 'TRYING TO LOAD ' . get_class($this)."_mdl");
        $this->ci->load->model(get_class($this)."_mdl");
        log_message('info', get_class($this)."_mdl"." has been loaded");
    }

    public function __setpublic($name, $value)
    {
        $this->$name = $value;
    }

    public function __getpublic($key)
    {
        return $this->$key;
    }
}
?>
