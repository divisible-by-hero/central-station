<?php
/**
 *
 * @name Gravatar Helper - Wrap Gravatar.com function calls for easy integration.
 * @author Derek Stegelman
 * @package CI Defect Tracker
 * @subpackage Global Helpers
 *
 * Last Modified October 8 2010
 *
 *
 */


/**
 * Get either a Gravatar URL or complete image tag for a specified email address.
 *
 * @param string $email The email address
 * @param string $s Size in pixels, defaults to 80px [ 1 - 512 ]
 * @param array $atts Optional, additional key/value attributes to include in the IMG tag
 * @return String containing either just a URL or a complete image tag
 * @source http://gravatar.com/site/implement/images/php/
 */

function getGravatar($email, $s = 80) {

    $d = "mm";
    $r = "x";
    $img = false;
    $url = 'http://www.gravatar.com/avatar/';
    $url .= md5( strtolower( trim( $email ) ) );
    $url .= "?s=$s&d=$d&r=$r";
    if ( $img ) {
        $url = '<img src="' . $url . '"';
        foreach ( $atts as $key => $val )
            $url .= ' ' . $key . '="' . $val . '"';
        $url .= ' />';
    }
    //return $url;
    $buildTag = "<img src='$url' class='gravatar'>";
    return $buildTag;
}

/* End of gravatar_helper.php */

?>
