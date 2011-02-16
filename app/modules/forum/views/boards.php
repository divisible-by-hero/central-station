<div id="forums">
    <?php foreach($forums->result() as $forum) { ?>
    <div class="forum">
        <h2><?php echo $forum->title; ?></h2>
        <table>
            <tr>
                <th>Forum Name</th>
                <th>Topics</th>
                <th>Replies</th>
                <th>Latest Post Info</th>
            </tr>
            <?php $boards = getBoardObject($forum->id); ?>
            <?php foreach($boards->result() as $board) { ?>
            <tr>
                <td>
                    <h3><a href="#"><?php echo $board->title; ?></a></h3>
                    <p><?php echo $board->description; ?></p>
                </td>
                <td>
                    <?php echo getTopicCount($board->id); ?>
                </td>
                <td>
                    <?php echo getBoardReplies($board->id); ?>
                </td>
                <td>
                    <?php $posts = getLatestPostObject($board->id) ?>
                    <?php foreach($posts->result() as $post) { ?>
                    <a href="#"><?php echo $post->post ?></a>
                    <span>Posted: <?php echo $post->publish_date; ?> ago</span>
                    <span>Author: <a href="#"><?php echo $post->author; ?></a></span>
                    <?php } ?>
                </td>
            </tr>
           
            <?php } ?>
        </table>
    </div>
    <?php } ?>
</div>
