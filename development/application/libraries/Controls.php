<?php
/**
 * Description of Controls
 *
 * @author Derek Stegelman
 */
class Controls {
    //put your code here


    private $ci;  

    public function  __construct() {
        $this->ci =& get_instance();
        $this->ci->load->database();
    }


    public function getProject($projectID){
      

        if ($projectID == 0){


        $projectData = $this->ci->db->get('projectTable');

        } else {


            $projectData = $this->ci->db->get_where('projectTable', array('projectID'=>$projectID));
        }


        return $projectData;

    }
}
?>
