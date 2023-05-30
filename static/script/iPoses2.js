
// pose_Countdown
let start_btn = document.getElementById('start');
let restart_btn = document.querySelector('.pose_next');


function play_song(){
    document.getElementById('mySong').play();
    // after completing this sound it will redircet to the result page
    redirect();
}

// redirect after the counter stops
function redirect(){
    setTimeout(mywebURL, 47000);
}

function mywebURL(){
    window.location.href = "http://127.0.0.1:8000/iresults2?";
}




function restart_pose(){
    location.reload();
}


// restart_pose
restart_btn.addEventListener('click', restart_pose);
