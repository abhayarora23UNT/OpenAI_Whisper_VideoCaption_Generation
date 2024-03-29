
document.addEventListener("DOMContentLoaded", () => {
    executeJsCode()
});

/**
 * Method to receive event from python script
 */
function receiveDismissEvent(){
    $.ajax({
        url: '/send_event',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ 'event_name': 'dismissEvent', 'data': 'True' }),
        success: function(response) {
            hideLoader()
            console.log(response.message); // log the response message to the console
        }
    });
}

/**
 * Method to execute JS code when DOM Content Loaded
 */
function executeJsCode() {
    handleYoutubeUploadButtonState()
    handleUploadButtonState()
    handleButtonActiveStates()
}


/**
 * Method to handle state of youtube upload button
 */
function handleYoutubeUploadButtonState() {
    const yTubeInputClass = ".form-input-youtube"
    const yTubeButtonClass = ".form-button-youtube"
    const eventType = "keyup"

    // get dom elements //
    const formInput = document.querySelector(yTubeInputClass);
    const formButton = document.querySelector(yTubeButtonClass);

    // the default state is 'disabled'
    formButton.disabled = true;

    formInput.addEventListener(eventType, () => {
        if (document.querySelector(yTubeInputClass).value === "") {
            formButton.disabled = true; // return disabled as true whenever the input field is empty
        } else {
            formButton.disabled = false; // enable the button once the input field has content
        }
    });
}

/**
 * Method yo handle state for custom video upload button
 */
function handleUploadButtonState() {
    const custVideoInputClass = ".form-input-video"
    const custVideoButtonClass = ".form-button-upload"
    const eventType = "change"

    // get dom elements //
    const formInput = document.querySelector(custVideoInputClass);
    const formButton = document.querySelector(custVideoButtonClass);

    // the default state is 'disabled'
    formButton.disabled = true;

    formInput.addEventListener(eventType, () => {
        if (document.querySelector(custVideoInputClass).value === "") {
            formButton.disabled = true; // return disabled as true whenever the input field is empty
        } else {
            setTimeout(() => {
                checkVideoDuration(formInput, formButton);
            }, 1000);

        }
    });

}



/**
 * Method to handle active button states
 */
function handleButtonActiveStates() {
    const buttons = document.querySelectorAll("button");
    const sections = document.querySelectorAll(".content");

    const eventType = "click";
    const activeClass = "active";
    buttons.forEach((btn) => {
        btn.addEventListener(eventType, () => {
            buttons.forEach((btn) => {
                btn.classList.remove(activeClass);
            });
            btn.classList.add(activeClass);
            const id = btn.id;
            sections.forEach((section) => {
                section.classList.remove(activeClass);
            });
            const req = document.getElementsByClassName(`content${id}`);
            req[0].classList.add(activeClass);
        })
    })
}


/**
 * Method to check video duration
 * @param {*} input formInput
 * @param {*} formButton formButton
 */
function checkVideoDuration(input, formButton) {
    if (input) {
        const timeLimit = videoDurationAllowed; // time in seconds
        const file = input.files[0];
        const video = document.createElement('video');
        video.src = URL.createObjectURL(file);
        video.onloadedmetadata = function () {
            if (video.duration > timeLimit) {
                alert(`Video duration should not be more than ${timeLimit} seconds!`);
                input.value = "";
                formButton.disabled = true;
                URL.revokeObjectURL(video.src);
            } else {
                formButton.disabled = false; // enable the button once the input field has content
            }
        };
    }
};








