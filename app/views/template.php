<!--
To change this template, choose Tools | Templates
and open the template in the editor.
-->
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>hi this is using the template</title>
        <?php echo link_tag('assets/css/style.css'); ?>
    </head>
    <body>
        <div class="header">
            <h1>Issue Tracker</h1>
        </div>
        <div class="content">
            <?php
            echo $content;
            ?>
        </div>
        <div class="sidebar">
            <a class="button"><span>Add Issue</span></a>
            

        </div>
    </body>
</html>
