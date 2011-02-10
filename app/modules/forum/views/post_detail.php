<div class="post">
    <?php foreach($post->result() as $post_detail) { ?>
    <?php $postID = $post_detail->id; ?>
    <h2><?php echo $post_detail->title; ?></h2>
    <div class="photo">
        <?php echo getGravatar($post_detail->email); ?>
        <a href="#" class="username"><?php echo $post_detail->username; ?></a>
    </div>
    <p class="content">
        <?php echo $post_detail->content; ?>
    </p>
    <?php } ?>
</div>
<div class="replies">
    <?php foreach($replies->result() as $reply) { ?>
    <div class="reply">
        <h3><?php echo $reply->title; ?></h3>
        <div class="photo">
            <?php echo getGravatar($reply->email); ?>
            <a href="#" class="username"><?php echo $post_detail->username; ?></a>
        </div>
        <p class="content">
            <?php echo $reply->reply; ?>
        </p>
        
    </div>
    <?php } ?>
</div>
<a class="button" href="<?php echo site_url('forum/reply/' . $postID); ?>"><span>Reply</span></a>