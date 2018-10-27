var assessTable;

$(document).ready(function(){
    assessTable = $('#assess_table').DataTable({
        // columnDefs: [{
        //     targets: -1,
        //     className: 'dt-body-right',
        // }],
        order: [[1, 'desc'],],
        paging: false,
        scrollY: 300,
        scrollCollapse: true
    });
});

$(document).on('assessmentListUpdated', function(event){
    var tr = $('#assess_table_body tr')
    assessTable.clear();
    assessTable.rows.add(tr).draw();
});
