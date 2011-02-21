<div id="forums">
    <?php foreach($forums->result() as $forum) { ?>
    <div class="forum">
        <h2><?php echo $forum->title; ?></h2>
        <table>
            <tr>
                <th>Forum Name</th>
                <th>Topics</th>
                <th>Latest Post Info</th>
            </tr>
            <?php $boards = getBoardObject($forum->id); ?>
            <?php foreach($boards->result() as $board) { ?>
            <tr>
                <td class="boardName">
                    <h3><a href="<?php echo site_url('forum/viewboard/' . $board->id); ?>"><?php echo $board->title; ?></a></h3>
                    <p><?php echo $board->description; ?></p>
                </td>
                <td class="topicCount">
                    <?php echo getTopicCount($board->id); ?>
                </td>
                <td class="authorInfo">
                    <?php $posts = getLatestPostObject($board->id) ?>
                    <?php foreach($posts->result() as $post) { ?>
                    <a href="<?php echo site_url('forum/viewthread/' . $post->id); ?>"><?php echo $post->title ?></a>
                    <span>Posted: <?php date('m/y/d'); ?> ago</span>
                    <span>Author: <a href="#">Derek Stegelman</a></span>
                    <?php } ?>
                </td>
            </tr>
           
            <?php } ?>
        </table>
    </div>
    <?php } ?>
</div>
