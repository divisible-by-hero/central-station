<?php

class Comment extends CoreLibrary {
	
	
	public $module_id;
	
	public function __construct()
	{
		parent::__construct();
	}
	
	public function get_comments($item_id, $limit = null)
	{
		if (!$limit)
		{
			return $this->Comment_mdl->get_comments($this->module_id, $item_id);
		
		}
		else
		{
		
		
		}
	}
	
	/***
		Add Comment
		Derek Stegelman
	***/
	
	public function add_comment($item_id)
	{
	
	
	}

}