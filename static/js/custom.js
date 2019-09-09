$(document).ready(function(){
  // Carousel Slide Control
  $('#myCarousel').on('slide.bs.carousel');
  
  // Collapse class - Hides navigation bar displayed on xs & sm screens only by default
  $('.collapse').collapse("hide");
  
  // Displays first FAQ answer on FAQs page
  $('.open').collapse("show");
  
  // Tooltip (Info that appears when user hovers over certain features)
  $(function () {
    $('[data-toggle="tooltip"]').tooltip();
  });
  
});