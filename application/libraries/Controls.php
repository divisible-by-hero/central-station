<?php
/**
 * @name Controls Library
 * @package CI Defect Tracker
 * @subpackage Libraries
 * @author Derek Stegelman
 * @version 1.0
 *
 * Last Modified October 25 2010
 *
 */

class Controls {

    // CI Object
    
    private $ci;

    // Project table

    private $projectTable;

    public function  __construct() {
        $this->ci =& get_instance();
        
        $this->projectTable = $this->ci->config->item('projectTable');
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
