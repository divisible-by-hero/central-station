<?php
/* 
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

function getReplies($thread_id)
{
    return 23;
    $CI =& get_instance();
    $replies = $CI->Reply_mdl->getWhere('post_id', $thread_id);
    return $replies->num_rows();
}

function getViews($thread_id)
{
    // getCountWhere(key, value)
    $CI =& get_instance();
    $CI->load->model('View_mdl');
    $view_object = $CI->View_mdl->getWhere('post_id', $thread_id);
    foreach($view_object->result() as $view)
    {
        $views = $view->views;
    }
    return $views;
}

function getForumDrop()
{
    
}

function getTopicCount($board_id)
{
    $CI =& get_instance();
    $posts = $CI->Post_mdl->getWhere('board_id', $board_id);
    return $posts->num_rows();
}

function getBoardReplies($board_id)
{
    //$CI =& get_instance();
    //$replies = $CI->Reply_mdl->getWhere('board_id', $board_id);
    //return $replies->num_rows();
}

function getBoardObject($forum_id)
{
    $CI =& get_instance();
    $boards = $CI->Board_mdl->getBoards($forum_id);
    log_message('info', $CI->db->last_query());
    return $boards;
}

function getLatestPostObject($board_id)
{
    $CI =& get_instance();
    return $CI->Post_mdl->get_latest_post($board_id);

}

function get_latest_reply_object($thread_id)
{
    $CI =& get_instance();
    $CI->load->model('Reply_mdl');
    return $CI->Reply_mdl->getWhere('post_id', $thread_id);
}

?>
