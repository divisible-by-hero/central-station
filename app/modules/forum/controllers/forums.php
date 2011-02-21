<?php
/**
* DefectTracker
*
* 
*
* @package		DefectTracker
* @version		1.0
* @author		Derek Stegelman <fotochest.com|stegelman.com>
* @license		Apache License v2.0
* @copyright		2010 Nuts and Bolts Web Solutions
*/

// ----------------------------------------------------------------

/**
* Forums Controller
*
* @package		Forums
* @category		Controllers
* @author		Derek Stegelman
*/

class Forums extends CoreController {
    

    public function __construct()
    {
        parent::__construct();
        $this->load->library('forum');
        $this->load->model('Reply_mdl');
        $this->load->helper('forum');
        $this->load->model('Board_mdl');
        $this->template->write_view('sidebar', 'sidebar');
    }

    public function index()
    {
        // Show all forums and boards

        // Get all boards
        $data['forums'] = $this->Forum_mdl->get();

        $this->template->write_view('content', 'boards', $data);
        $this->template->render();
    }
    
    /*
    * View Board
    *
    *
    */

    public function view_board($board_id)
    {
        // View all threads for a board
        $data['threads'] = $this->Post_mdl->get_posts($board_id);
        log_message('info', $this->db->last_query());
        $this->template->write_view('content', 'posts', $data);
        $this->template->render();
    }

    public function view_thread($thread_id)
    {
        // View thread details

        
        // Get Related replies
        $data['replies'] = $this->Reply_mdl->get_replies($thread_id);

        // Get original post info
        $data['threads'] = $this->Post_mdl->get_post_detail($thread_id);
        log_message('info', $this->db->last_query());

        // Record the view
        $this->forum->record_view($thread_id);
        
        // Build and render the template
        $this->template->write_view('content', 'post_detail', $data);
        $this->template->render();
    }

    public function new_reply($thread_id)
    {
        $this->load->library('form_validation');

        // Set validation rules

        $this->form_validation->set_rules('username', 'Username', 'required');

        // Check for form submission

        if(!$this->form_validation->run())
        {
            // Validation failed, show form
            $this->template->write_view('content', 'forms/new_reply');
            $this->template->render();
        }
        else
        {
            // Process form.
            $reply_data = array('post_id'=>$thread_id, 'title'=>$this->input->post('title'),
                'reply'=>$this->input->post('reply_content'));
            $this->Reply_mdl->create($reply_data);
        }
    }

    public function new_post($board_id)
    {

        $this->load->library('form_validation');

        //Set Rules

        $this->form_validation->set_rules('username', 'Username', 'required');

        //Check for Validation

        if(!$this->form_validation->run())
        {
            // Validation failed, show form
            $this->template->write_view('content', 'forms/new_post');
            $this->template->render();
        }
        else
        {
            // Process new post.
            $this->forum->post_title = $this->input->post('post_title');
            $this->forum->post_content = $this->input->post('post_content');
            $this->forum->board_id = $board_id;
            $this->forum->process_new_post();
        }

    }

    public function new_board($forum_id)
    {
        $this->load->library('form_validation');

        $this->form_validation->set_rules('title', 'Board Name', 'required');

        if (!$this->form_validation->run())
        {
            $this->template->write_view('content', 'forms/new_board');
            $this->template->render();
        }
        else
        {
            $board_data = array('title'=>$this->input->post('title'),
                                'forum_id'=>$forum_id);
            $this->Board_mdl->create($board_data);
        }
    }

    public function new_forum()
    {
        $this->load->library('form_validation');

        $this->form_validation->set_rules('title', 'Forum Name', 'required');

        if (!$this->form_validation->run())
        {
            $this->template->write_view('content', 'forms/new_forum');
            $this->template->render();
        }
        else
        {
            $forum_data = array('title'=>$this->input->post('title'));
            $this->Forum_mdl->create($forum_data);
        }

    }
}
?>
