<div class="modal">

    <h1>Add Defect</h1>
    <div class="form">
        <div class="formItem">
            <label for="defectTitle"><?php echo getSetting('defectName'); ?> Title</label>
            <input type="text" name="defectTitle" id="defectTitle">
        </div>
        <div class="formItem">
            <label for="defectProject">Project</label>
            <?php echo projectDropdownList(); ?>
        </div>
        <div class="formItem">
            <label for="defectDescription">Description</label>
            <textarea cols="44" rows="12"></textarea>
        </div>
        <a class="button">
            <span>Create <?php echo getSetting('defectName'); ?></span>
        </a>
    </div>
    
</div>
