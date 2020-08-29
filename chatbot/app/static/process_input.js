$(function() {
    $("#validate").bind('click', function(){
      $.getJSON($SCRIPT_ROOT + '/process_question', {
      question: $('input[name="question"]').val()
      }, function(data){
        $("#dialogue_box").append('<div class="row align-items-start mb-3"><row_box class=col-4>' + data.question + '</row_box>\
          <row_box class=col-4>' + data.wikipedia_response +'</row_box><row_box class=col-4><img src='+ data.google_map +'width="100px" height="100px"></row_box>');
        var element = document.getElementById("dialogue_box");
        element.scrollIntoView({block:"end"});
    });

    var clear_question = document.getElementById("question");
    clear_question.value = "";
  });
});