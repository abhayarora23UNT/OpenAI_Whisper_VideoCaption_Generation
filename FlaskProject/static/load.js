function loadTrack(){

    var player = videojs('content_video');

    player.on('ready', function() {
    player.vhs = null;
    
    });

    var  video = document.querySelector('track');
    video.addEventListener('load', function() {
        var tracks = video.track;
        tracks.mode = 'showing';
        console.log("hello")
    });
}

function showLoader(){
    console.log("inside showLoader")
    document.getElementById("loader").style.display = "block";
}

function hideLoader(){
    console.log("hide showLoader")
    document.getElementById("loader").style.display = "none";
}


function showPageTransition(){
    showLoader()

    setTimeout(() => {
        hideLoader()
    }, 3000);
}