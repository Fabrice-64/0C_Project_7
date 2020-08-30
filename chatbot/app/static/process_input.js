$(function() {
    $("#validate").bind('click', function(){
      $('html').css('cursor', 'wait');
      $.getJSON($SCRIPT_ROOT + '/process_question', {
      question: $('input[name="question"]').val()
      }, 
      function(data){
        if (data.wikipedia_response == "None"){
          $("#dialogue_box").append('<div class="row align-items-start mb-3"><row_box class=col-4>Je n\'ai pas compris ta question... Peux-tu la reformuler ?</row_box>');
        } else {
          $("#dialogue_box").append('<div class="row align-items-start mb-3"><row_box class=col-4>' + data.question + '</row_box>\
          <row_box class=col-4>' + data.wikipedia_response +'</row_box>\
          <row_box class=col-4><a href=' + data.google_map + ' target="_blank"><img src='+ data.google_map +' width="100px" height="100px"></a></row_box>');
        };
        var element = document.getElementById("dialogue_box");
        element.scrollIntoView({block:"end"});
        $('html').css('cursor', 'default');
        });
        var clear_question = document.getElementById("question");
        clear_question.value = "";
    });
  });