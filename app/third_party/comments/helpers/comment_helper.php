<?php


function get_item_comments($module_id, $item_id)
{
	$CI =& get_instance();
	$where_data = array('module_id'=>$module_id, 'item_id'=>$item_id);
	$CI->load->model('Comment_mdl');
	$comments = $CI->Comment_mdl->get_where_many($where_data);
	return $comments->num_rows();
}

?>