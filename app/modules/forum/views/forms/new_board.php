<div class="form">
    <?php echo form_open(); ?>
    <div class="formItem">
        <label>Board Name:</label>
        <div>
            <input type="text" name="title" id="title">
        </div>
    </div>
    <div class="formItem">
        <label>Forum:</label>
        <div>
            <?php echo getForumDrop(); ?>
        </div>
    </div>
    <div class="formItem">
        <div>
            <a class="button" href="#"><span>Add</span></a>
        </div>
    </div>

    <?php echo form_close(); ?>

</div>
