$(document).ready(function(){
    $('#myCarousel').on('slide.bs.carousel');
    $('.collapse').collapse();
    $('#myModal').modal('toggle');
    
    $(function () {
      $('[data-toggle="tooltip"]').tooltip();
    });
});