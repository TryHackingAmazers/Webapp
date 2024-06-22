function loadFile(event) {
    var reader = new FileReader();
    reader.onload = function(){
        var output = document.getElementById('upload-content');
        output.innerHTML = `<img src="${reader.result}" alt="Uploaded image" style="width: 100%; height: 100%; object-fit: contain;">`;
    };
    reader.readAsDataURL(event.target.files[0]);
};
// Loading animation
window.addEventListener('load', function () {
    const loadingAnimation = document.getElementById('loading-animation');
    loadingAnimation.style.opacity = '0';
    setTimeout(() => {
        loadingAnimation.style.display = 'none';
    }, 500); // Matches the transition duration
});