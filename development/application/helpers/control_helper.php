<?php
/**
 * 
 *
 * @author Derek Stegelman
 * @package CI Defect Tracker
 * @subpackage Control Helper
 * 
 *
 *
 */


/**
 * projectDropdownList()
 *
 * @param void.
 * @return A drop down list of current/active projects
 *
 */

function projectDropdownList(){
    $CI2 =& get_instance();
    $CI2->load->library('controls');
//    //$projects = $CI->controls->getProject(0);
//    $dropData = array();
//    foreach($projects->result() as $row){
//        $dropData[$row->projectID] = $row->projectTitle;
//    }
//    $CI->load->helper('form');
//
//    return form_dropdown('projects', $dropData);
}



?>
