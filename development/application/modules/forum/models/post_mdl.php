<?php
/**
 *
 * @name Forum Post Model
 * @author Derek Stegelman
 * @package CI Defect Tracker
 * @subpackage Forums Module
 *
 * Last Updated October 16 2010
 *
 *
 */

class Post_mdl extends CI_Model {

    // Vars

    public $postID;
    public $postCreatedDate;
    public $postTitle;
    public $postContent;

    // Private vars

    private $postTable;


    //Constructor...

    function Post_mdl(){
        parent::CI_Model();
        $this->load->config('forum');
        $this->postTable = $this->config->item('postTable');
    }

    // CRUD

    public function create(){

        $data = array('postID'=>$this->postID,
                      'postCreatedDate'=>date('m/y/d'),
                      'postTitle'=>$this->postTitle,
                      'postContent'=>$this->postContent);

        $this->db->insert($this->postTable, $data);
    }

    public function read(){

        $posts = $this->db->get($this->postTable);
        return $posts;

    }

    public function update(){
        $data = array('postTitle'=>$this->postTitle,
                      'postContent'=>$this->postContent);
        
        $this->db->where('postID', $this->postID);

        $this->db->update($this->postTable, $data);
    }

    public function delete(){

        $this->db->where("postID", $this->postID);
        $this->db->delete($this->postTable);
    }

    // End CRUD

    public function getPostAndReplies($postID)
    {
        
    }


}
?>
