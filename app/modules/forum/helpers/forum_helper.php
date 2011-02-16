<?php
/* 
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

function getReplies($thread_id)
{
    return 23;
}

function getViews($thread_id)
{
    return 23;
}

function getForumDrop()
{
    
}

function getTopicCount($board_id)
{
    
}

function getBoardReplies($board_id)
{
    
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
    
}

?>
