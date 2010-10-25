<!--
To change this template, choose Tools | Templates
and open the template in the editor.
-->
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title></title>
    </head>
    <body>
        <?php foreach($defectData->result() as $defect) { ?>
        <div class="defectContent">
          <h1>#<?php echo $defect->defectID; ?> is <span>In Development</span></h1>
          <a class="button" href="#"><span>Save</span></a>
          <a class="button" href="#"><span>Move to Testing</span></a>
          <a class="button" href="#"><span>Move back to Dev Queue</span></a>
          <div class="form">
              <div class="formItem">
                  <label for="title">Title</label>
                  <input type="text" name="title" id="title" value="The Method getDefecInfo is failing on load">
              </div>
              <div class="formItem">
                  <label for="desc">Description</label>
                  <textarea id="editor1" rows="10" cols="40"></textarea>
                  <script type="text/javascript">
                      CKEDITOR.replace( 'editor1' );
                  </script>
              </div>

          </div>
          <div class="subInfo">
              <h3>Comments</h3>

              <h3>Files</h3>
              <h3>Git integration</h3>
          </div>

      </div>
      <div class="sidebar">
          <h2>Defect Status</h2>
          <div class="form">
              <div class="formItem">
                  <label for="project">Project</label>
                  <select name="project" id="project">
                      <option name="project1">Project1</option>
                      <option name="project2">Project2</option>
                  </select>
              </div>
              <div class="formItem">
                  <label for="severity">Severity</label>
                  <select name="severity" id="severity">
                      <option value="high">High</option>
                      <option value="med">Medium</option>
                      <option value="low">Low</option>
                  </select>
              </div>
              <div class="formItem">
                  <label for="status">Status</label>
                  <select name="status" id="status">
                      <option value="indev">In Development</option>
                      <option value="intesting">In Testing</option>
                  </select>
              </div>


          </div>


      </div>
        <?php } ?>
  </body>
</html>
