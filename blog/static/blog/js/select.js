function select_ctl() {
    var type = $("#drop_list");
    var open = 0;
    type.click(function () {
        if (open == 0) {
            $('.select_box').css("display", "inline-block");
            open = 1;
        } else {
            $('.select_box').css("display", "none");
            open = 0;
        }
    })
    $('#body').click(function() {
        $('.select_box').hide(); 
        open = 0;                         
    });
   
}


function zanshang_box_ctl() {
    var type = $("#zanshang");
    var open = 0;
    type.click(function () {
        $(this).css({
            "background-color": "#fff",
            "color": "rgb(0, 0, 0)"});
        if (open == 0) {
            $('.zanshang_box').css("display", "inline-block");
            open = 1;
        } else {
            $(this).css({
                "background-color": "#000",
                "color": "rgb(255, 255, 255)"});
            $('.zanshang_box').css("display", "none");
            open = 0;
        }
    })
    $('#body').click(function() {
        $("#zanshang").css({
            "background-color": "#000",
            "color": "rgb(255, 255, 255)"});
        $('.zanshang_box').hide();
        open = 0;                         
    });
   
}


