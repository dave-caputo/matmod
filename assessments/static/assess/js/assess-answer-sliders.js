$(document).ready(function(){
    $('input[name*="answer"]').each(function(index, element) {
        $(element).ionRangeSlider({
            min: 0,
            max: 5,
            values: [0, 1, 2, 3, 4, 5],
        });
    });

});
