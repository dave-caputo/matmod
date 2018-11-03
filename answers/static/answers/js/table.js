var answerTable;
var sectionTable;

$(document).ready(function(){
    answerTable = $('#answer_table').DataTable({
        columnDefs: [{
            targets: [2, 3, 4, 5],
            width: "10%",
        }],
        paging: false,
        scrollY: 300,
        scrollCollapse: true
    });
    sectionTable = $('#section_table').DataTable({
        paging: false,
        scrollY: 300,
        scrollCollapse: true
    });
});
