<div id="forums">
    <div class="forum">
        <h2>Title of Board</h2>
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
                    <h3><a href="<?php echo site_url('forum/viewthread/' . $thread->id); ?>"><?php echo $thread->title; ?></a></h3>
                    <p>Author: <a href="<?php echo site_url('users/profile/' . $thread->username); ?>"><?php echo $thread->username; ?></a></p>
                </td>
                <td>
                    <?php echo $thread->replies; ?>
                </td>
                <td>
                    <?php echo getViews($thread->id) ?>
                </td>
                <td>
                    <span>Posted: <?php echo $thread->latest_post_time; ?> ago</span>
                    <span>Author: <a href="<?php echo site_url('users/profile/' . $thread->username); ?>"><?php echo $thread->username; ?></a></span>
                </td>
            </tr>
            <?php } ?>
        </table>
    </div>
</div>
