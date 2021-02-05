let metaFieldContainer = $('#meta-field-container');

var state = $('#state-count').text();

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
