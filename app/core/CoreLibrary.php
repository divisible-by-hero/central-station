<?php
/**
* iRoam
*
* iRoam is a simple web travel application.  Meant to help you share your trips with family and friends.
*
* @package		iRoam
* @version		1.0
* @author		Derek Stegelman <stegelman.com>
* @license		Apache License v2.0
* @copyright	2010 - 2011 iRoam
*/

// ----------------------------------------------------------------

/**
* Static Pages Controller
*
* @package		iRoam
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

    protected function __setVar($name, $value)
    {
        $this->$name = $value;
    }

    protected function __getVar($key)
    {
        return $this->$key;
    }
}
?>
