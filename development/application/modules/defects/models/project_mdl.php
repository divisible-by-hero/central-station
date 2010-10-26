<?php
/**
 * @name Project_mdl
 * @author Derek Stegelman
 * @package CI Defect Tracker
 *
 * Last Updated October 25, 2010
 *
 * 
 */
class Project_mdl extends CI_Model {

    var $projectID;
    var $projectTitle;
    var $projectDescription;

    // Object Table

    private $projectTable;

    public function  __construct() {
        parent::CI_Model();
        $this->projectTable = $this->config->item('projectTable');
    }

    // @todo CRUD

    public function getProject($projectID){

        if ($projectID == 0){

       
        $projectData = $this->db->get($this->projectTable);

        } else {

            
            $projectData = $this->db->get_where($this->projectTable, array('projectID'=>$projectID));
        }

        
        return $projectData;

    }

    public function createProject(){

        $projectData = array('projectTitle'=>$this->projectTitle, 'projectDescription'=>$this->projectDescription);
        $insert_query = $this->db->insert_string($this->projectTable, $projectData);

        log_message('info', 'Project_mdl::createProject() is executing a query ' . $insert_query);

        $this->db->query($insert_query);

    }


    

}
?>
