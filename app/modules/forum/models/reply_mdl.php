<?php
/* 
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

/**
* Open Cook Book
*
* Open Cook Book is a simple CodeIgniter based cooking application that stores recipes.
*
* @package		OpenCookBook
* @version		1.0
* @author		Derek Stegelman <fotochest.com|stegelman.com>
* @license		Apache License v2.0
* @copyright		2010 OpenCookBook
*/

// ----------------------------------------------------------------

/**
* Recipes Controller
*
* @package		OpenCookBook
* @category		Controllers
* @author		Derek Stegelman
*/

class Reply_mdl extends CoreModel {
    //put your code here

    public function __construct()
    {
        parent::__construct();
        $this->_table = 'defect_forum_post_reply';
    }

    public function get_replies($post_id)
    {
        return $this->db->select('*, defect_authentication.id as userID')
                        ->from('defect_forum_post_reply')
                        ->join('defect_authentication', 'defect_authentication.id = defect_forum_post_reply.author_id')
                        ->where('post_id', $post_id)
                        ->get();
    }
}
?>
