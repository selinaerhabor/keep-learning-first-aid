$(document).ready(function(){
  // Carousel Slide Control
  $('#myCarousel').on('slide.bs.carousel');
  
  // Collapse class
  $('.collapse').collapse();
  
  // Tooltip (Info that appears when user hovers over certain features)
  $(function () {
    $('[data-toggle="tooltip"]').tooltip();
  });
  
  // Controls CSS for Active class for current page displayed on xs & sm screens only
  $("li").click(function(){
    $("li").addClass("active");
  });
});