<?php
/**
 *
 * @name Posts Controller
 * @author Derek Stegelman
 * @package CI Defect Tracker
 * @subpackage Forums Module
 *
 * Last Updated October 16 2010
 *
 *
 */


class Posts extends MY_Controller {

    function Posts()
    {
        parent::MY_Controller();
        $this->load->model('Post_mdl');
        $this->data['forumName'] = getSetting('forumName');

    }

    /*
     *
     * View post
     *
     *
     *
     */

    public function view($postID)
    {
        if (!is_numeric($postID) || $postID == null)
        {
            show_404();
        }

        // Grab the post and replies

        $this->data['postData'] = $this->Post_mdl->getPostAndReplies($postID);

        // Load the Views

        $this->load->view('viewPost', $this->data);
    }


    /*
     * Add post
     *  @todo - Everything
     * @params Void.
     * @returns Void.
     *
     */

    public function addPost()
    {
        
    }


}
?>
