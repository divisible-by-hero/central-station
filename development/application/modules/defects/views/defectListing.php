<?php $this->data['page'] = 2; ?>
<?php $this->load->view('header', $this->data); ?>

<?php echo projectDropdownList(); ?>


<?php echo getGravatar('dstegelman@gmail.com', '45'); ?>
<table>
<?php foreach($defectData->result() as $defect) { ?>
    <tr>
        <td><?php echo $defect->defectID; ?></td>
    </tr>


<?php } ?>
</table>
    </body>
</html>
