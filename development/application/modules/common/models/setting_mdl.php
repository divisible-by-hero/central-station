<?php
/**
 * Gets and Sets settings for the app.
 *
 * @author Derek Stegelman
 */
class Setting_mdl extends CI_Model {

    public $settingTable;
    public $settingID;
    public $settingName;
    public $settingValue;

    /**
     *  Set Variables
     *
     * @author Derek Stegelman
     * @updated Oct 5 2010
     *
     */

    public function setSetting($settingName, $settingValue){

        $settingData = array('settingValue'=>$settingValue);
        $settingWhere = "settingName = '$settingName'";
        $settingUpdate = $this->db->update_string($this->settingTable, $settingData, $settingWhere);
        $this->db->query($settingUpdate);

        
    }

    public function getSetting($settingName){

        $settingSQL = "SELECT settingValue WHERE settingName = '$settingName'";
        $settingData = $this->db->query($settingSQL);
        if ($settingData->num_rows == 0){
            show_error("Setting " . $settingName . " cannot be found");
        } else {
            foreach($settingData->result() as $row){
                $settingValue = $row->settingValue;

            }
            return $settingValue;
        }
    }

}
?>
