<?php

class Comment extends CoreLibrary {
	
	
	public $module_id;
	
		
	public function __construct()
	{
		parent::__construct();
		log_message('info', 'loading model for comment lib');
				
	}
	
	public function get_comments($item_id, $limit = null)
	{
		if ($limit == null)
		{
			log_message('info', 'laskdjf;laskfjasl;dfkjas;lfkjsdl;fkj');
			$data = array('module_id'=>$this->module_id, 'item_id'=>$item_id);
			return $this->ci->Comment_mdl->get_where_many($data);
		}
		else
		{
		
		
		}
	}
	
	/***
		Add Comment
		Derek Stegelman
		@param item_id;
	***/
	
	public function add_comment($item_id, $comment, $email, $first_name, $last_name)
	{
		$comment_data = array('item_id'=>$item_id, 'comment'=>$comment, 'email'=>$email, 'first_name'=>$first_name, 'last_name'=>$last_name);
		$this->ci->Comment_mdl->create($comment_data);
	
	}

}