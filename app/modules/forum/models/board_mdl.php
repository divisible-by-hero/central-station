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

class Board_mdl extends CoreModel {
    

    public function __construct()
    {
        parent::__construct();
        $this->_table = 'defect_forum_board';
    }

    public function getBoards($forum_id)
    {
        // board title, description, topic count, reply count, latest_post, latest post author, latest post time
        return $this->db->select('*')
                        ->where('forum_id', $forum_id)
                        ->get($this->_table);

    }
}
?>
