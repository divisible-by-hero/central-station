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

}
?>
