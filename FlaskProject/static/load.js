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


