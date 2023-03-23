const checkFileInput = (x, y) => {
    const fileInput = document.getElementById(x);
    const submitButton = document.getElementById(y);
    if (fileInput.value) {
        submitButton.disabled = false;
    } else {
        submitButton.disabled = true;
    }
    if (x == "videoInput") {
        const video = document.createElement('video');
        video.preload = 'metadata';
        video.onloadedmetadata = function () {
            window.URL.revokeObjectURL(video.src);
            if (video.duration <= 30) {
                submitButton.disabled = false;
            } else {
                alert('Video duration should not be more than 30 seconds!');
                submitButton.disabled = true;
                fileInput.value = null;
            }
        }
        video.src = URL.createObjectURL(fileInput.files[0]);
    }
};




const buttons = document.querySelectorAll("button");
const sections = document.querySelectorAll(".content");


buttons.forEach((btn) => {
    btn.addEventListener("click", () => {
        buttons.forEach((btn) => {
            btn.classList.remove("active");
        });
        btn.classList.add("active");
        const id = btn.id;
        sections.forEach((section) => {
            section.classList.remove("active");
        });
        const req = document.getElementsByClassName(`content${id}`);
        req[0].classList.add("active");
    })
})