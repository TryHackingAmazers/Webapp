function loadFile(event) {
    var reader = new FileReader();
    reader.onload = function(){
        var output = document.getElementById('upload-content');
        output.innerHTML = `<img src="${reader.result}" alt="Uploaded image" style="width: 100%; height: 100%; object-fit: contain;">`;
    };
    reader.readAsDataURL(event.target.files[0]);
};