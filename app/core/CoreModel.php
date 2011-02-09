<?php

/**
* Core Model
*
* Open Cook Book is a simple CodeIgniter based cooking application that stores recipes.
*
* @package		CodeIgniter
* @subpackage           Core Classes
* @version		1.0
* @author		Derek Stegelman <http://derek.stegelman.com>
* @license		Apache License v2.0
* @copyright		2010 OpenCookBook
*/

// ----------------------------------------------------------------

class CoreModel extends CI_Model {

    public $_table;
    public $primaryKey = 'id';
    


    public function __construct()
    {
        parent::__construct();
        log_message('info', 'Load Core Model');
    }

    // Variable setting

    public function  __setVar($name, $value) {
        $this->$name = $value;
    }

    public function __getVar($key)
    {
        return $this->$key;
    }


    public function get($keyValue = null)
    {
        if($keyValue == null)
        {
            return $this->db->get($this->_table);
        }
        else
        {
            return $this->db->where($this->primaryKey, $keyValue)
                            ->get($this->_table);

        }
    }
    
    /*
     * getCount
     * 
     * @author Derek Stegelman
     * @access Public
     * @param null
     */

    public function getCount()
    {
        log_message('info', 'Get count!');
        return $this->db->count_all($this->_table);
    }
    
    /*
     * getCountWhere
     * 
     * @author Derek Stegelman
     * @access Public
     * @param key, Value Strings
     * 
     */
    
    public function getCountWhere($key, $value)
    {
//    	return $this->db->where($key, $value)
//                        ->count_all($this->_table);
        $counts = $this->db->where($key, $value)->get($this->_table);
        return $counts->num_rows();
    }

    /*
     * getWhere
     *
     * @author Derek Stegelman
     * @access public
     * @param var $key, var $value
     */

    public function getWhere($key, $value)
    {
        log_message('info', 'Performing get where..' . ' where ' . $key . ' equals ' . $value);
        return $this->db->where($key, $value)
                        ->get($this->_table);
    }

    /*
     * getLimtWhere
     *
     * @author Derek Stegelman
     * @access public
     * @param var $key, var $value, int $limit
     * @return array Dataset
     */

    public function getLimitWhere($key, $value, $limit)
    {
        return $this->db->limit($limit)
                        ->where($key, $value)
                        ->get($this->_table);
    }

    /*
     * getLimit
     *
     * @author Derek Stegelman
     * @access public
     * @param int $limit
     * @return array of data with the a limit.
     */

    public function getLimit($limit)
    {
        return $this->db->get($this->_table, $limit);
    }


    /*
     * Get a dataset in desc order.
     *
     * @author Derek Stegelman
     * @access public
     * @param var $key
     * @return array Dataset
     */

    public function getDesc($key)
    {
        return $this->db->order_by($key, 'desc')
                        ->get($this->_table);
    }

    /*
     * Get a dataset in ascending order.
     *
     * @author Derek Stegelman
     * @access public
     * @param var $key
     * @return array dataset
     *
     */

    public function getAsc($key)
    {
        return $this->db->order_by($key, 'asc')
                        ->get($this->_table);
    }

    /*
     * Create
     * @author Derek Stegelman
     * @access public
     * @param array $data
     * @return null
     */

    public function create($data)
    {
        $this->db->insert($this->_table, $data);
    }

    /*
     * Update
     * @author Derek Stegelman
     * @access public
     * @param array $data, int $key
     * @return null - executes query
     */

    public function update($data, $key)
    {
        return $this->db->where('id', $key)
        				->update($data);
    }
    
    /*
     * updateWhere
     * 
     * @author Derek Stegelman
     */
    
    public function updateWhere($data, $key, $value)
    {
    	return $this->db->where($key, $value)
    					->update($data);
    }

    /*
     * Exist - Check to see if a record exsists for a given value
     * @author Derek Stegelman
     * @access public
     * @param string $col, string $value
     * @return bool
     */

    public function exist($col, $value)
    {
        $tableData = $this->db->where($col, $value)
                              ->get($this->_table);
        if($tableData->num_rows == 0)
        {
            return FALSE;
        }
        else
        {
            return TRUE;
        }
    }

    public function delete($id)
    {
        return $this->db->where($this->primary_key, $id)
			->delete($this->_table);
    }
    
    public function deleteWhere($key, $value)
    {
    	return $this->db->where($key, $value)
    					->delete($this->_table);
    }

    public function __destruct()
    {
        log_message('info', $this->db->last_query());
    }
}
?>