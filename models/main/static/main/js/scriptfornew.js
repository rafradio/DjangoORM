function SaveToJson() {
    this.buttonJson = document.getElementById("json");
    this.returnButton = document.getElementById("return");
    this.id = document.getElementById("title");
    // this.initSettings();
}

SaveToJson.prototype.initSettings = function() {
    this.returnButton.addEventListener('click', () => {
        let number = this.id.value;
        let newUrl = new URL(window.location.href); 
        let fullPath = new URL("http://" + newUrl.host + '/' + number + '/data');
        location.href = fullPath;
    });
}

const saveAction = new SaveToJson();

export {saveAction};