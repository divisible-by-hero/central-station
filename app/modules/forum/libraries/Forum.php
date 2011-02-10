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

class Forum extends CoreLibrary {
    //put your code here

    public $post_title;
    public $post_content;
    public $board_id;
    public $author_id;


    public function __construct()
    {
        parent::__construct();
        // Load dependent models
        $this->load->model('Post_mdl');
    }

    public function process_new_post()
    {
        // Must create the entry in the post table, as well as create an entry in the view table.
        // Add record in the view table

        $post_data = array('title'=>$this->post_title, 'content'=>$this->post_content,
                'board_id'=>$this->board_id, 'author_id'=>$this->author_id);

        $this->Post_mdl->create($post_data);
        $post_id = //Unkonwn;

        $view_data = array('views'=>0, 'post_id'=>$post_id);
        $this->db->insert('defect_forum_post_views', $view_data);

    }

    public function record_view($post_id)
    {
        $current_view = $this->db->where('post_id', $post_id)
                                 ->get('defect_forum_post_views');
        foreach($current_view->result() as $view)
        {
            $current_views = $view->views;
        }

        // increment by 1

        $new_views = $current_views + 1;

        // Update the record.

        $view_data = array('views'=>$new_views);
        $this->db->where('post_id', $post_id)
                 ->update('defect_forum_post_views', $view_data);

    }
}
?>
