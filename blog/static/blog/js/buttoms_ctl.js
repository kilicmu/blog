function page_ctl() {
    $("#prev").mouseenter(function () {
        $(this).css({
            "border": "1px solid rgb(255,255,255)",
            "color": "rgb(255,255,255)"
        });
    })
    $("#prev").mouseout(function () {
        $(this).css({
            "border": "1px solid rgb(0, 107, 102)",
            "color" : "rgb(0, 107, 102)"
        });
    })
    
    $("#prev").click(function () {
        $(this).css({
            "border": "rgb(0, 107, 102)",
            "color" : "rgb(0, 107, 102)"
        });
    })
    
    $("#next").mouseenter(function () {
        $(this).css({
            "border": "1px solid rgb(255,255,255)",
            "color": "rgb(255,255,255)"
        });
    })
    $("#next").mouseout(function () {
        $(this).css({
            "border": "1px solid rgb(0, 107, 102)",
            "color" : "rgb(0, 107, 102)"
        });
        
    })
    $("#next").click(function () {
        $(this).css({
            "border": "1px solid rgb(0, 107, 102)",
            "color" : "rgb(0, 107, 102)"
        });
    })
    
}


function to_top() {
    $(window).scroll(function () {
        var Htop = $(document).scrollTop();
        if (Htop > 430) {
            $("#to_top").css({
                "display": "block"
            });
        }
        if (Htop < 430) {
            $("#to_top").css({
                "display": "none"
            });
        }

    });

    var timer = null;
    $("#to_top").click(function () {
        cancelAnimationFrame(timer);
        timer = requestAnimationFrame(function fn() {
            var oTop = document.body.scrollTop || document.documentElement.scrollTop;
            if (oTop > 0) {
                scrollTo(0, oTop - 50);
                timer = requestAnimationFrame(fn);
            } else {
                cancelAnimationFrame(timer);
            }
        });
    })

}

function find_ctl(){
    $("#find").click(function(){
        w =$(window).width();
        if(w >= 977){
        var find = $("#find");
        find.animate({"width":300}, 200);}
    })
    $(window).resize(function(){
        var find = $("#find");
        find.animate({"width":120}, 200);
    })
    $("#body").click(function(){
        var find = $("#find");
        find.animate({"width":120}, 200);
    })

}

