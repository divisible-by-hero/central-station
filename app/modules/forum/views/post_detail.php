<div id="forums">
    <div class="forum">
        <?php foreach($threads->result() as $thread) { ?>
        <h2><?php echo $thread->title; ?></h2>
        
        <div class="forumDetails">
            <a href="#"><?php echo $thread->username; ?></a>
            <span>Posted: <?php echo $thread->date_created; ?></span>
        </div>
        <div class="thread">
            <div class="author">
                <span></span>
                <span>Total Posts: <?php echo get_authors_post_count($thread->author_id) ?></span>
                <span>Joined: <?php echo get_author_date_joined($thread->author_id) ?></span>
            </div>
            <div class="threadContent">
                <?php echo $thread->content; ?>
            </div>
        </div>
        <?php } ?>
        <div class="replies">
            <?php foreach($replies->result() as $reply) { ?>
                <div class="thread">
                    <div class="author">
                        <span></span>
                        <span>Total Posts: <?php echo get_authors_post_count($reply->author_id); ?></span>
                        <span>Joined: <?php echo get_author_date_joined($reply->author_id); ?></span>
                    </div>
                    <div class="threadContent">
                        <?php echo $reply->reply; ?>
                    </div>
                </div>
            <?php } ?>
        </div>
    </div>
</div>
