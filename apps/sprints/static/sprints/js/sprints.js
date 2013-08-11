/* ===========================================================
* Central Station
* https://www.centralstationproject.com
* ===========================================================
*
* Author: Divisible by Hero
* Description: Utilites and Asynchronus actions for Central Station sprints
* ========================================================== */

$(document).ready(function(){
    
    $(".error").effect("pulsate", { times:2 }, 1500);
    
    //Sprint Views
    //$('#cs-sprint-board').hide();
    //$('#cs-sprint-board .cs-tasks').hide();
    
    $("table#cs-sprint-table").tablesorter(); 
    
    $('#cs-sprint-switcher button').click(function(e){
        if ( $(this).attr('id') == 'cs-sprint-board-button' ){
            $('#cs-sprint-board').show();
            $('#cs-sprint-table').hide();
        }
        else{
            $('#cs-sprint-board').hide();
            $('#cs-sprint-table').show();            
        }
    });
    
    $( ".cs-sprint-board-column-list" ).sortable({
        connectWith: '.cs-sprint-board-column-list',
        cursor: 'move',
        stop: function(event, ui){
            data = serializeStories();
            updateStories(data);
        }
    });


    /* Story Status */
    $('.cs-story-status-item').click(function(){
        updateStatus( $(this).attr('data-story-id'), $(this).attr('data-story-status-id') );
    });

    /* Tasks  */
    $('.cs-task-item-complete').change(function(){
        var id = $(this).attr('data-task-id');
        if ( this.checked ){
            toggleTask(id, true);
        }
        else{
            toggleTask(id, false);
        }
    });


    
});

/* Story Tasks */
function toggleTask(id, value){
    $.ajax({
        type: "POST",
        url: "/ajax/update/task/" + id + "/",
        dataType: 'json',
        data: {
            "csrfmiddlewaretoken":csrf_token,
            'value':value
        },
        success: function(data){
            //console.log('success');
            updateTaskItem(id, data.value)
        }
    });
}

function updateTaskItem(id, value){
    var task = $('.cs-task-item[data-task-id=' + id +']');
    //remove btn- classes
    if (value){
        task.addClass('cs-task-item-completed');
        task.find('input').prop('checked', true);
    }
    else{
        task.removeClass('cs-task-item-completed');
        task.find('input').prop('checked', false);
    }
}


/* Story Status */
function updateStatus(id, value){
    $.ajax({
        type: "POST",
        url: "/ajax/update/story/" + id + "/",
        dataType: 'json',
        data: {
            "csrfmiddlewaretoken":csrf_token,
            "value": value,
        },
        success: function(data){
            updateStatusButton(id, data)
        }
    });
}

function updateStatusButton(id, data){
    //console.log(data)
    var button = $('.cs-story-status-item-current[data-story-id=' + id +']')
    //remove btn- classes
    button.attr('class', function(i, c){
        return c.replace(/\bbtn-\S+/g, '');
    });
    //add new button class
    button.addClass('btn-' + data.value.style_class);
    button.children('.cs-story-status-item-current-name').text(data.value.status);
    
    //update progress bar
    for (var i=0;i<data.sprint.completed_by_status.length;i++){ 
        //console.log(i)
        $('.cs-progress-bar-item:eq(' + i + ')').css('width', data.sprint.completed_by_status[i].percentage + '%');
    }
}




/*
Maybe Deprecated ?
function updateStatus(story_id, status){
	$.ajax({
		type: "POST",
		url: "/sprints/update/story-status/",
		dataType: 'json',
		data: "csrfmiddlewaretoken=" + csrf_token + "&story_id=" + story_id + "&status=" + status,
		success: function(data){
		    if ( data.success ){
		        //do something
		    }
		    else {
		        //do something else
		    }
		},
	 });
}
*/

function updateStories(post_data){
	$.ajax({
		type: "POST",
		url: "/k-state/sprints/update/stories/", //yeah, that is WRONG
		dataType: 'json',
        data: JSON.stringify(post_data),
		success: function(data){
		    if ( data.success ){
		        //do something
		    }
		    else {
		        //do something else
		    }
		},
	 });
}

function serializeStories(){
    //stuff
    var json = {'stories':[]}
    
    $( ".cs-sprint-board-column-list" ).each(function(){
        $(this).children('li.cs-story-card').each(function(){
            story = {};
            story.id = $(this).attr('data-story-id');
            story.status = $(this).parent().attr('data-column');
            story.position = $(this).index();
            json.stories.push(story);
        });
    });
    return json
}


