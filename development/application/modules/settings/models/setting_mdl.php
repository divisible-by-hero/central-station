<?php
/**
 * Description of setting_mdl
 *
 * @author derek
 */
class Setting_mdl extends CI_Model {

    var $settingID;
    var $settingName;
    var $settingValue;
    var $settingTable;

    function  __construct() {
        parent::CI_Model();
        $this->settingTable = $this->config->item('settingTable');
    }

    public function getSetting($settingName){

        $selectQuery = "SELECT * FROM $this->settingTable WHERE settingName = $settingName";
        $setting = $this->db->query($selectQuery);
        foreach($setting->result() as $row){
            $value = $row->settingValue;
        }
        return $value;

    }

    public function setSetting($settingName, $settingValue){

        $updateData = array('settingValue' => $settingValue);
        $where = "settingName = $settingName";
        $updateString = $this->db->update_string($this->settingTable, $updateData, $where);
        log_message('info', 'Setting_mdl::setSetting() is executing a query ' . $updateString);
        $this->db->query($updateString);

    }

}
?>
