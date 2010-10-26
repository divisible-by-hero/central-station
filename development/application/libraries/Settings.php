<?php
/**
 *
 * @name Settings Library
 * @author Derek Stegelman
 * @package CI Defect Tracker
 * @subpackage Libraries
 * @version 1.0
 * 
 * Last Updated October 25 2010
 *
 *
 */

class Settings {

    // CI Super Object

    private $ci;

    // Settings Table define.

    private $settingTable;

    function Settings() {
        $this->ci =& get_instance();
        
        $this->settingTable = $this->ci->config->item('settingsTable');
    }

    public function getSetting($settingName){

        $settingSQL = "SELECT * FROM $this->settingTable WHERE settingName = '$settingName'";

        $settingData = $this->ci->db->query($settingSQL);
        foreach($settingData->result() as $row){
            $settingValue = $row->settingValue;
        }
        return $settingValue;  
    }

    public function setSetting($settingName, $settingValue){


        return true;
    }
    


}
?>
