function showContact() {
    $('#contact-hover').fadeIn(50);
}

$(function(){
    console.log("Ready");
    $('#contact-wrapper').fadeIn(500);
});

$(document).ready(function() {
    //$('#review-dialog-box').hide();
    //
    //$('#open-review-dialog').click(function(){
    //    $('#overlay-back').fadeIn(100);
    //    $('#review-dialog-box').show();
    //});
    //
    //$('#cancel-review-btn').click(function(){
    //    $('#overlay-back').fadeOut(100);
    //    $('#review-dialog-box').hide();
    //});
    //
    //
    
    $(document).scroll(function () {
      console.log($(window).scrollTop())
      if ($(window).scrollTop() > 88) { 
        $('#navbar').addClass('navbar-fixed-top');
        $('#top-links').addClass('navbar-right');
        $('#page-brand-onscroll').show(); 
      }
      if ($(window).scrollTop() < 88) {
        $('#navbar').removeClass('navbar-fixed-top');
        $('#top-links').removeClass('navbar-right');
        $('#page-brand-onscroll').hide(); 
      }
    });
    
    $('.bxslider').bxSlider({
      adaptiveHeight: true,
      mode: 'fade',
      ticker: true,
    });
  
    $(document).scroll(function () {
        if ($(this).scrollTop() > 50) {
            $('#back-to-top').fadeIn();
        } else {
            $('#back-to-top').fadeOut();
        }
        });
        // scroll body to 0px on click
        $('#back-to-top').click(function () {
            $('#back-to-top').tooltip('hide');
            $('body,html').animate({
                scrollTop: 0
            }, 800);
            return false;
        });
        
        $('#back-to-top').tooltip('show');


});

$(function() {
    //----- OPEN
    $('[data-popup-open]').on('click', function(e)  {
        var targeted_popup_class = jQuery(this).attr('data-popup-open');
        $('[data-popup="' + targeted_popup_class + '"]').fadeIn(350);

        e.preventDefault();
    });

    //----- CLOSE
    $('[data-popup-close]').on('click', function(e)  {
        var targeted_popup_class = jQuery(this).attr('data-popup-close');
        $('[data-popup="' + targeted_popup_class + '"]').fadeOut(350);

        e.preventDefault();
    });
});

