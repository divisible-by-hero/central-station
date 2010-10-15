<?php
/**
 * @name Controls Library
 * @package CI Defect Tracker
 * @subpackage Libraries
 * @author Derek Stegelman
 *
 *
 * Last Modified October 8 2010
 *
 */

class Controls {

    // CI Object
    
    private $ci;

    private $projectTable;

    private function  __construct() {
        $this->ci =& get_instance();
        
        $this->ci->config->item('projectTable');
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
