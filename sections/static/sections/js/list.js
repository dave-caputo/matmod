var listQreSections = (function() {

    /*=============================================
    =            LOAD URL AND GET LIST            =
    =============================================*/

    var qreSectionListUrl;
    $(document).ready(function() {
        qreSectionListUrl = $('#page_urls').data('qreSectionListUrl');
        $.ajax({
                url: qreSectionListUrl,
                type: 'GET',
            })
            .done(function(data) {
                $('#qre_section_list_div').html(data);
                console.log("success");
            })
            .fail(function() {
                console.log("error");
            });
    });
})();
