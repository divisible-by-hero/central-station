<table>
    <tr>
        <th>Topic Title</th>
        <th>Replies</th>
        <th>Views</th>
        <th>Latest Info</th>
    </tr>
    <?php foreach($posts->result() as $post) { ?>
    <tr>
        <td>Folder</td>
        <td><a href="<?php echo site_url('forum/viewthread/' . $post->id); ?>"><?php echo $post->title; ?></a></td>
        <td><?php echo $post->replies; ?></td>
        <td><?php echo $post->views; ?></td>
        <td>Posted 27  Minutes ago::author <?php echo $post->username; ?></td>
    </tr>
    <?php } ?>
</table>