
// layout.html
$(".draggable").draggable();




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



// IEX API 

// info
// const Http = new XMLHttpRequest();
// const url='https://api.iextrading.com/1.0/stock/AAPL/company';
// Http.open("GET", url);
// Http.send();
// Http.onreadystatechange=(e)=>{
// console.log(Http.responseText)
// }
// (e)=>{
// console.log(Http.responseText)
// }

// logo
// const Http = new XMLHttpRequest();
// const url='https://api.iextrading.com/1.0//stock/AAPL/logo';
// Http.open("GET", url);
// Http.send();
// Http.onreadystatechange=(e)=>{
// console.log(Http.responseText)
// }
// (e)=>{
// console.log(Http.responseText)
// }