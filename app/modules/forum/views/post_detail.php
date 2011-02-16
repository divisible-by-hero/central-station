<div id="forums">
    <div class="forum">
        <h2><?php echo $title; ?></h2>
        <div class="forumDetails">
            <a href="#"><?php echo $thread_author; ?></a>
            <span>Posted: <?php echo $thread_post_date; ?></span>
        </div>
        <div class="thread">
            <div class="author">
                <span></span>
                <span>Total Posts: <?php echo $author_thread_count; ?></span>
                <span>Joined: <?php echo $author_date_joined; ?></span>
            </div>
            <div class="threadContent">
                <?php echo $thread_content; ?>
            </div>
        </div>
        <div class="replies">
            <?php foreach($replies->result() as $reply) { ?>
                <div class="thread">
                    <div class="author">
                        <span></span>
                        <span>Total Posts: <?php echo $reply->author_thread_count; ?></span>
                        <span>Joined: <?php echo $reply->author_date_joined; ?></span>
                    </div>
                    <div class="threadContent">
                        <?php echo $reply->content; ?>
                    </div>
                </div>
            <?php } ?>
        </div>
    </div>
</div>
