// counter part

let counter_num = document.querySelectorAll(".num");

let interval = 9000;  // 5000ms

counter_num.forEach((counter_Num) => {
    let startvalue = 0;
    let endvalue = parseInt(counter_Num.getAttribute("data-val"))
    let duration = Math.floor(interval / endvalue);
    let counter = setInterval(function(){
        startvalue += 1;
        counter_Num.textContent = startvalue;
        if(startvalue == endvalue){
            clearInterval(counter);
        }
    })
});

