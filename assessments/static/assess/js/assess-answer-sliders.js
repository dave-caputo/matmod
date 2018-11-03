$(document).ready(function(){
    console.log('slider controller getting loaded');
    $('input[name*="answer"]').each(function(index, element) {

        $(element).ionRangeSlider({
            min: 0,
            max: 5,
            grid: true,
            values: [0, 1, 2, 3, 4, 5],
            onFinish: function(data){
                console.log('Data=' + data);
            }
        });
    });

});
