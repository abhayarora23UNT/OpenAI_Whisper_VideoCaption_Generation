
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
    const loaderElementId="loader"
    const displayBlock="block"
    document.getElementById(loaderElementId).style.display = displayBlock;
}

/**
 * Method to hide loader
 */
function hideLoader() {
    const loaderElementId="loader"
    const displayNone="none"
    document.getElementById(loaderElementId).style.display = displayNone;
}


/**
 * Method to show page transition
 */
function showPageTransition() {
    const dismissLoader = appLoaderDismiss
    showLoader();
    setTimeout(() => {
        hideLoader()
    }, dismissLoader);
}

