<?php
/**
 * Controls Helper
 *
 * @author Derek Stegelman
 * @package CI Defect Tracker
 * @subpackage Control Helper
 * 
 * Last Modified Oct 7 2010
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
    $CI =& get_instance();
    $CI->load->library('controls');
    $CI->load->helper('form');
    $CI->controls->setTable(getSetting('projectTable'));
    $projects = $CI->controls->getProject(0);
    $dropData = array();
    foreach($projects->result() as $row){
        $dropData[$row->projectID] = $row->projectTitle;
    }

    return form_dropdown('projects', $dropData);

}

/**
 * priorityDropdownList()
 *
 * @param void
 * @return a Drop down list of priorities available via the database
 *
 */

function priorityDropdownList(){

    $CI =& get_instance();
    $CI->load->library('controls');
    
}

/**
 *
 * statusDropdownList()
 *
 * @param void
 * @return a drop down list of available statuses.
 *
 *
 */

function statusDropdownList (){
    
}

?>
