<?php
/* 
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 * Description of Settings
 *
 * @author derek
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
