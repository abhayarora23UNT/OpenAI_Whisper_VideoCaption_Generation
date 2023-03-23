
/**
 * Method to load track
 */
function loadTrack() {

    const player = videojs('content_video');

    player.on('ready', function () {
        player.vhs = null;

    });

    const video = document.querySelector('track');
    video.addEventListener('load', function () {
        const tracks = video.track;
        tracks.mode = 'showing';
    });
}

/**
 * Method to show loader
 */
function showLoader() {
    console.log("inside showLoader")
    document.getElementById("loader").style.display = "block";
}

/**
 * Method to hide loader
 */
function hideLoader() {
    console.log("hide showLoader")
    document.getElementById("loader").style.display = "none";
}


function showPageTransition() {
    showLoader()

    setTimeout(() => {
        hideLoader()
    }, 3000);
}