/* This script unfolds the whole dialogue process once the user has validated his question.
It goes from sending the question to the routes module, down to displaying the replies. */
document.getElementById("validate").onclick = function(){
    $('html').css('cursor', 'wait');
    var question = document.getElementsByName("question");
    question  = DOMPurify.sanitize(question[0].value);
    $("#dialogue_box").append(`<div class="row mb-2"><row_question class="col-4">${question}</row_question>`);
    $.getJSON($SCRIPT_ROOT + '/process_question', {
    question: question
    }, 
    function(data){
      if (data.wikipedia_response == "None"){
        $("#dialogue_box").append('<div class="row mb-2">\
        <row_answer class="col-4 offset-4">Je n\'ai pas compris ta question... Peux-tu la reformuler ?</row_answer></div>');
      } else if  (data.wikipedia_response == ""){
        $("#dialogue_box").append('<div class="row mb-2">\
        <row_answer class="col-4 offset-4">Je n\'ai rien trouvé qui réponde à ta question... :-/ Tu peux en poser une autre, please ?</row_answer></div>');
      } else {
        $("#dialogue_box").append('<div class="row align-items-start mb-4">\
        <row_answer class="col-8 offset-4">' + data.wikipedia_response +'</row_answer>');
        $("#dialogue_box").append('<row_picture class="col-8 offset-4"><iframe src=' + data.url_google_dynamic +' allowfullscreen></iframe></row_picture');
      };
      var element = document.getElementById("dialogue_box");
      element.scrollIntoView({block:"end"});
      $('html').css('cursor', 'default');
      });
      var clear_question = document.getElementById("question");
      clear_question.value = "";
  };
