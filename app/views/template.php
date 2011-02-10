<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Issue Tracking?</title>
        <!-- Begin CSS Delcarations -->
        <?php echo link_tag('assets/css/style.css'); ?>

        <!-- Begin JS Declarations -->
    </head>
    <body>
        <div class="header">
            <h2>Company Name?</h2>
            <h1>Issue Tracker</h1>
        </div>
        <div class="content">
            <?php
            echo $content;
            ?>
        </div>
        <div class="sidebar">
            <a class="button"><span>Add Issue</span></a>
            <!-- Will Probably need a sidebar content region -->
        </div>
    </body>
</html>
