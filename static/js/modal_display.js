var $modal = $('.modal');

// Show loader & then get content when modal is shown
$modal.on('show.bs.modal', function(e) {
  var paragraphs = $(e.relatedTarget).data('paragraphs');

  $(this)
    .addClass('modal-scrollfix')
    .find('.modal-body')
    .html('loading...')
    .load('https://baconipsum.com/api/?type=meat-and-filler&paras=' + paragraphs, function() {
      // Use Bootstrap's built-in function to fix scrolling (to no avail)
      $modal
        .removeClass('modal-scrollfix')
        .modal('handleUpdate');
    });s
});



$(document).ready(function(){
 $("#msgid").html("This is Hello World by JQuery");
});
