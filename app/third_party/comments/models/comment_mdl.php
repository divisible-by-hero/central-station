<?php

class Comment_mdl extends CoreModel {


	public function __construct()
	{
		parent::__construct();
		$this->load->config('comment');
		$this->_table = $this->config->item('comment_table');
	}
	
	public function get_comments($module_id, $item_id)
	{
		return $this->db->select(*)
						->from($this->_table)
						->where('module_id', $module_id)
						->where('item_id', $item_id);
	}

}
?>