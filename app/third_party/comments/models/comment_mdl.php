<?php

/**
* iRoam
*
* iRoam is a simple web travel application.  Meant to help you share your trips with family and friends.
*
* @package		iRoam
* @version		1.0
* @author		Derek Stegelman <stegelman.com>
* @license		Apache License v2.0
* @copyright	2010 - 2011 iRoam
*/

// ----------------------------------------------------------------

/**
* Static Pages Controller
*
* @package		iRoam
* @category		Controllers
* @author		Derek Stegelman
*/


class Comment_mdl extends CoreModel {


	public function __construct()
	{
            parent::__construct();
            $this->load->config('comment');
            $this->_table = $this->config->item('comment_table');
	}
	
//	public function get_comments($module_id, $item_id)
//	{
//		$joe = $this->db->select(*)
//                                ->from($this->_table)
//				->where('module_id', $module_id)
//				->where('item_id', $item_id)
//				->get();
//	}

	public function get_comments($module_id, $item_id)
	{
		$where_data = array('module_id'=>$module_id, 'item_id'=>$item_id);
		$this->db->where($where_data);
		
	} 



}
?>