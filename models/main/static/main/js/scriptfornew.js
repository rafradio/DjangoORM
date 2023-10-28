function SaveToJson() {
    this.buttonJson = document.getElementById("json");
    this.returnButton = document.getElementById("return");
    // this.initSettings();
}

SaveToJson.prototype.initSettings = function() {
    this.returnButton.addEventListener('click', () => {
        let newUrl = new URL(window.location.href); 
        let fullPath = new URL("http://" + newUrl.host + '/');
        location.href = fullPath;
    });
}

const saveAction = new SaveToJson();

export {saveAction};