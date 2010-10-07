<div class="modal">

    <h1>Add Defect</h1>
    <div class="form">
        <div class="formItem">
            <label for="defectTitle"><?php echo getSetting('defectTitle'); ?> Title</label>
            <input type="text" name="defectTitle" id="defectTitle">
        </div>
        <div class="formItem">
            <label for="defectProject">Project</label>
            
        </div>
        <div class="formItem">
            <label for="defectDescription">Description</label>
            <textarea cols="5" rows="20"></textarea>
        </div>
        <a class="button">
            <span>Create <?php echo getSetting('defectTitle'); ?></span>
        </a>
    </div>
    
</div>
