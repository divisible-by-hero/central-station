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

class Forums extends CoreController {
    

    public function __construct()
    {
        parent::__construct();
        $this->load->model('Forum_mdl');
        $this->load->model('Post_mdl');
        $this->load->model('Reply_mdl');
        $this->load->helper('forum');
    }

    public function index()
    {
        $this->template->write_view('content', 'boards');
        $this->template->render();
    }

    public function view_board($board_id)
    {
        $data['posts'] = $this->Post_mdl->get_posts($board_id);
        log_message('info', $this->db->last_query());
        $this->template->write_view('content', 'posts', $data);
        $this->template->render();
    }

    public function view_thread($thread_id)
    {
        // Get Related replies
        $data['replies'] = $this->Reply_mdl->get_replies($thread_id);

        // Get original post info
        $data['post'] = $this->Post_mdl->get_post_detail($thread_id);
        log_message('info', $this->db->last_query());
        // Build and render the template
        $this->template->write_view('content', 'post_detail', $data);
        $this->template->render();

    }

    public function new_reply($thread_id)
    {
        
    }

    public function new_post($board_id)
    {
        
    }
}
?>
