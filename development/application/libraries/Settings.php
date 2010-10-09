<?php
/**
 *
 * @name Settings Library
 * @author Derek Stegelman
 * @package CI Defect Tracker
 * @subpackage Libraries
 * 
 * Last Updated October 8 2010
 *
 *
 */

class Settings {

    private $ci;

    private $settingTable;

    public function  __construct() {
        $this->ci =& get_instance();
        $this->ci->load->database();
        $this->settingTable = 'settingTable';
    }

    public function getSetting($settingName){

        $settingSQL = "SELECT * FROM $this->settingTable WHERE settingName = '$settingName'";

        $settingData = $this->ci->db->query($settingSQL);
        foreach($settingData->result() as $row){
            $settingValue = $row->settingValue;
        }
        return $settingValue;
        
    }
    


}
?>
