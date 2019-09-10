
/* 长宽占位 rem算法, 根据root的rem来计算各元素相对rem, 默认html 320/20 = 16px */
function placeholderPic(){

    var w = document.documentElement.offsetWidth;
//  if(w >1262){
    // document.documentElement.style.fontSize = 12 + 'px';
    // return;
//  }
    document.documentElement.style.fontSize=w/100+'px';
}
placeholderPic();
window.onresize=function(){
    placeholderPic();
}
