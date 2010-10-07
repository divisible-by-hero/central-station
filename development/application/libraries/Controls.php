<?php
/**
 * Description of Controls
 *
 * @author Derek Stegelman
 */
class Controls {
    //put your code here


    private $ci;

    private $projectTable;

    public function  __construct() {
        $this->ci =& get_instance();
        $this->ci->load->database();
    }

    public function setTable($name){
        if(isset($name)){
            $this->projectTable = $name;
        }
    }


    public function getProject($projectID){
      
        if ($projectID == 0){

        $projectData = $this->ci->db->get($this->projectTable);
        } else {
            $projectData = $this->ci->db->get_where($this->projectTable, array('projectID'=>$projectID));
        }
        return $projectData;
    }
}
?>
