<?php $this->load->view('header'); ?>

<?php echo validation_errors(); ?>

<?php echo form_open('users/login'); ?>
<h5>Email</h5>
<input type="text" name="userEmail" value="<?php echo set_value('userEmail'); ?>" size="50" />

<h5>Password</h5>
<input type="text" name="userPassword" value="<?php echo set_value('userPassword'); ?>" size="50" />

<div><input type="submit" value="Login" /></div>

</form>

</body>
</html>
