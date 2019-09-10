function fix_header() {
    // var navH=$(".header").offset().top;
    //         $(window).scroll(function(){
    //             // var scroH = $(this).scrollTop();

    //                 $(".header").css({"position":"fixed", "top":0})

    //         })

}

function set_select() {
    var station = $("#drop_list").offset().left;
    $(".select_box").css({
        "left": station
    });
    $(window).resize(function () {
        var station = $("#drop_list").offset().left;
        $(".select_box").css({
            "left": station
        })
    });
};

is_open = 0;
function show_type(){
    var type=$("#type");
    var list=$(".l_tag_l");
    list.hide();
    type.click(function(){
        if(is_open == 0){
        list.show();
        
        is_open=1;
        return;
    }
        
        if(is_open == 1){
            list.hide();
            is_open=0;
            
    }    
    })

    
    
    $("#body").click(function(){
        list.hide();
        is_open=0;
    })

    $("#l_back").click(function(){
        list.hide();
        is_open=0;
    })
    
}

function set_zanshang_box() {
    var station = $("#zanshang").offset().left;
    $(".zanshang_box").css({
        "left": station
    });
    $(window).resize(function () {
        var station = $("#zanshang").offset().left;
        $(".zanshang_box").css({
            "left": station
        })
    });
};