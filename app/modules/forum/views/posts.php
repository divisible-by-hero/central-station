<div id="forums">
    <div class="forum">
        <h2><?php echo $title; ?></h2>
        <table>
            <tr>
                <th>Topic</th>
                <th>Replies</th>
                <th>Views</th>
                <th>Latest Post Info</th>
            </tr>
            <?php foreach($threads->result() as $thread) { ?>
            <tr>
                <td>
                    <h3><a href="#"><?php echo $thread->title; ?></a></h3>
                    <p>Author: <a href="#"><?php echo $thread->author; ?></a></p>
                </td>
                <td>
                    <?php echo $thread->reply_count; ?>
                </td>
                <td>
                    <?php echo $thread->view_count; ?>
                </td>
                <td>

                    <span>Posted: <?php echo $thread->latest_post_time; ?> ago</span>
                    <span>Author: <a href="#"><?php echo $thread->latest_post_author; ?></a></span>
                </td>
            </tr>

            <?php } ?>
        </table>
    </div>
</div>
