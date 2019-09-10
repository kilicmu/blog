{
left_open = 0;

function left_line_ctl(){
    $("#message").click(function(){
        if(left_open==0){
        $(".left_line").animate({
            "left":"0"
        }, 400);
   
        $("#message").hide();
        left_open=1;
        return;
     }

        if(left_open==1){
            $(".left_line").animate({
                "left":"-16rem"
            }, 400);
            $("#message").show();
            left_open=0;
        }
        
    })

    $("#body").click(function(){
        if(left_open==1){
            $(".left_line").animate({
                "left":"-16rem"
            }, 400);
            $("#message").show();
            left_open=0;
        }
    })

    

}
}