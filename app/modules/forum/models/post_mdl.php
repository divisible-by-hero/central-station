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

class Post_mdl extends CoreModel {
    //put your code here

    public function __construct()
    {
        parent::__construct();
        $this->_table = 'defect_forum_post';
    }

    public function get_posts($board_id)
    {
        return $this->db->select('*, COUNT(defect_forum_post_reply.id) as replies, defect_forum_post_reply.id as replyID, defect_forum_post_views.id as viewID, defect_authentication.id as authorID')
                        ->from($this->_table)
                        ->join('defect_forum_post_reply', 'defect_forum_post_reply.post_id = defect_forum_post.id')
                        ->join('defect_forum_post_views', 'defect_forum_post_views.post_id = defect_forum_post.id')
                        ->join('defect_authentication', 'defect_authentication.id = defect_forum_post.author_id')
                        ->where('board_id', $board_id)
                        ->get();
    }

    public function get_post_detail($post_id)
    {
        return $this->db->select('*, COUNT(defect_forum_post_reply.id) as replies, defect_forum_post_reply.title as replyTitle, defect_forum_post_reply.id as replyID, defect_forum_post_views.id as viewID, defect_authentication.id as authorID')
                        ->from($this->_table)
                        ->join('defect_forum_post_reply', 'defect_forum_post_reply.post_id = defect_forum_post.id')
                        ->join('defect_forum_post_views', 'defect_forum_post_views.post_id = defect_forum_post.id')
                        ->join('defect_authentication', 'defect_authentication.id = defect_forum_post.author_id')
                        ->where('defect_forum_post.id', $post_id)
                        ->get();
    }

}
?>