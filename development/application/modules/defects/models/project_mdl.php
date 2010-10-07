<?php
/**
 * Description of project_mdl
 *
 * @author derek
 */
class Project_mdl extends CI_Model {

    var $projectID;
    var $projectTitle;
    var $projectDescription;
    var $projectTable;

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
