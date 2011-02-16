<div id="forums">
    <?php foreach($forums->result() as $forum) { ?>
    <div class="forum">
        <h2><?php echo $title; ?></h2>
        <table>
            <tr>
                <th>Forum Name</th>
                <th>Topics</th>
                <th>Replies</th>
                <th>Latest Post Info</th>
            </tr>
            <?php foreach($boards->result() as $board) { ?>
            <tr>
                <td>
                    <h3><a href="#"><?php echo $board->title; ?></a></h3>
                    <p><?php echo $board->description; ?></p>
                </td>
                <td>
                    <?php echo $board->topic_count; ?>
                </td>
                <td>
                    <?php echo $board->reply_count; ?>
                </td>
                <td>
                    <a href="#"><?php echo $board->latest_post; ?></a>
                    <span>Posted: <?php echo $board->latest_post_time; ?> ago</span>
                    <span>Author: <a href="#"><?php echo $board->latest_post_author; ?></a></span>
                </td>
            </tr>
           
            <?php } ?>
        </table>
    </div>
    <?php } ?>
</div>
