<?php
/* 
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 * Description of view_mdl
 *
 * @author Derek
 */
class View_mdl extends CoreModel {


    public function  __construct() {
        parent::__construct();
        $this->_table = 'defect_forum_post_views';
    }

}
?>
