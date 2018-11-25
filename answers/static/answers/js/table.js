var answerTable;
var sectionTable;

$(document).ready(function(){
    answerTable = $('#answer_table').DataTable({
        columnDefs: [{
            targets: [2, 3, 4],
            width: "12%",
        }],
        paging: false,
        scrollY: 300,
        scrollCollapse: true,
        footerCallback: function( tfoot, data, start, end, display ) {
            var api = this.api();

            var totals = []
            $.each([2, 3, 4], function(index, value){
            // Calculate totals for each column and insert in footer.

                var colTotal = api.column( value ).data().reduce( function ( a, b ) {
                    return (parseFloat(a) + parseFloat(b)).toFixed(1);
                }, 0 )

                totals.push(colTotal);

                $( api.column( value ).footer() ).html(colTotal);
            });

            // Calculate total maturity and insert in footer based on totals previously calculated.
            var totalMaturity;
            if (totals[2] == 0) {
                totalMaturity = 0;
            } else {
                totalMaturity = (totals[1] / totals[2] * 100).toFixed(0);
            }
            $( api.column(5).footer() ).html(totalMaturity + '%')
        }
    });



    sectionTable = $('#section_table').DataTable({
        columnDefs:[
            { "width": "12%", "targets": [1, 2, 3, 4] }
        ],
        paging: false,
        scrollY: 300,
        scrollCollapse: true,
        footerCallback: function( tfoot, data, start, end, display ) {
            var api = this.api();

            var totals = []
            $.each([1, 2, 3], function(index, value){
            // Calculate totals for each column and insert in footer.

                var colTotal = api.column( value ).data().reduce( function ( a, b ) {
                    return (parseFloat(a) + parseFloat(b)).toFixed(1);
                }, 0 )

                totals.push(colTotal);

                $( api.column( value ).footer() ).html(colTotal);
            });

            // Calculate total maturity and insert in footer based on totals previously calculated.
            var totalMaturity;
            if (totals[2] == 0) {
                totalMaturity = 0;
            } else {
                totalMaturity = (totals[1] / totals[2] * 100).toFixed(0);
            }
            $( api.column(4).footer() ).html(totalMaturity + '%')
        }
    });
});
