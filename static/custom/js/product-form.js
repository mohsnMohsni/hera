let metaFieldContainer = $('#meta-field-container');
let imageInputContainer = $('#image-input-container');
var state = $('#state-count').text();
var num = 1;

function addFieldValue(labelName, valueName) {
    state += 1;
    metaFieldContainer.append(`
        <div class="row col-12" id="meta-field">
            <div class="col-sm-6">
                <input type="text" class="form-control" name="label${state}" id="meta-label"
                       placeholder="${labelName}">
            </div>
            <div class="col-11 col-sm-5">
                <input type="text" class="form-control" name="value${state}" id="meta-value"
                       placeholder="${valueName}">
            </div>
            <div class="col-1">
                <button class="btn-add" type="button" onclick="callAddField()">
                    <i class="fa fa-plus-circle add-icon" style="font-size: 1.5em;"></i>
                </button>
            </div>
        </div>
    `);
}

function callAddField() {
    let labelName = document.getElementById('meta-label').getAttribute('placeholder');
    let valueName = document.getElementById('meta-value').getAttribute('placeholder');
    addFieldValue(labelName, valueName);
}

function addImageInput() {
    num += 1;
    let imageLabel = $('#image-label').text()
    imageInputContainer.append(`
        <div class="form-group choose-file row col-12 col-md-6">
            <label class="col-2 h-100 pt-2">
                <span>${imageLabel}</span>${num}
            </label>
            <i class="fa fa-file-image-o text-center px-2 mx-2 col-1"></i>
            <input type="file" name="image${num}" class="col-6 form-control-file mt-2 pt-1" accept="image/*"
                   id="id_image">
            <div class="col-1">
                <button class="btn-add" type="button" onclick="addImageInput()">
                    <i class="fa fa-plus-circle add-icon"
                       style="font-size: 1.5em;position: relative; top: -6px;"></i>
                </button>
            </div>
        </div>
    `)
}
