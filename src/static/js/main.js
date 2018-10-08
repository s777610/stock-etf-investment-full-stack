
// layout.html
$(".draggable").draggable();


// home.html
$(document).ready(function() {
  $(function() {
    $( "#dialog" ).dialog({
      autoOpen: false,
      modal: true
    });
  });

$("#email-button").click(function(){
    $( "#dialog" ).dialog( "open" );
  })
});


// securities_list.html
$( function() {
  var state = true;
  $( "#button" ).on( "click", function() {
    if ( state ) {
      $( "#effect" ).animate({
        backgroundColor: "#5E5E5E",
        color: "#fff",
        width: 900,
        height: 150
      }, 1000 );
    } else {
      $( "#effect" ).animate({
        backgroundColor: "#fff",
        color: "#000",
        width: 900,
        height: 100
      }, 1000 );
    }
    state = !state;
  });
} );

$( function() {
    var state = true;
    $("#button").on("click", function () {
      if ( state ) {
          $("#effect").addClass("newClass");
      } else {
          $( "#effect" ).removeClass( "newClass" );
      }
      state = !state;
    });
});
