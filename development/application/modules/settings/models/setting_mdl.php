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


    private function  __construct() {
        parent::CI_Model();
        $this->load->config('settings');
        $this->settingTable = $this->config->item('settingTable');
    }


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

    /*
     * getSetting($settingName)
     *
     * Retrieves a setting
     */

    public function getSetting($settingName){

        
        $settingData = $this->db->get_where($this->settingTable, array('settingName' => $settingName));
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
