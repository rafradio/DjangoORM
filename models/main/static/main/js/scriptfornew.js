function SaveToJson() {
    this.buttonJson = document.getElementById("json");
    this.returnButton = document.getElementById("return");
    this.id = document.getElementById("title");
    this.client = document.getElementById("client");
    this.productButton = document.getElementById("new_product");
    // this.initSettings();
}

SaveToJson.prototype.initSettings = function() {
    this.returnButton.addEventListener('click', () => {
        let number = this.id.value;
        let cl = this.client.value;
        let newUrl = new URL(window.location.href); 
        let fullPath = new URL("http://" + newUrl.host + '/' + number + '/' + cl + '/data');
        location.href = fullPath;
    });
    this.productButton.addEventListener('click', () => {
        let newUrl = new URL(window.location.href); 
        let fullPath = new URL("http://" + newUrl.host + '/new_product');
        location.href = fullPath;
    });
}

const saveAction = new SaveToJson();

export {saveAction};