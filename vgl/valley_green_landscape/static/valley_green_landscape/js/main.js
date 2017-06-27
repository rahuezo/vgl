function showContact() {
    $('#contact-hover').fadeIn(50); 
}

$(function(){
    console.log("Ready"); 
    $('#contact-wrapper').fadeIn(500);     
});

$(document).ready(function() {
    $('#review-dialog-box').hide();

    $('#open-review-dialog').click(function(){
        $('#overlay-back').fadeIn(100);
        $('#review-dialog-box').show();
    });

    $('#cancel-review-btn').click(function(){
        $('#overlay-back').fadeOut(100);
        $('#review-dialog-box').hide();
    });

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

