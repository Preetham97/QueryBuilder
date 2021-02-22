var rules_basic = {
    condition: 'AND',
    rules: [{
        id: "patients.subject_id",
        label: "patients.subject_id",
        type: "integer",
        value: "379926"
    }]
};

$(document).ready(function () {

    $('#builder').queryBuilder({
        plugins: ['bt-tooltip-errors'],

        default_filter: 'empty',

        filters: [{id: "apgar_events.encntr_id", label: "apgar_events.encntr_id", type: "integer"},
            {id: "apgar_events.item_id", label: "apgar_events.item_id", type: "integer"},
            {id: "apgar_events.label_name", label: "apgar_events.label_name", type: "string"},
            {id: "apgar_events.person_id", label: "apgar_events.person_id", type: "integer"},
            {id: "apgar_events.result_val", label: "apgar_events.result_val", type: "string"},
            {id: "apgar_events.result_val_num", label: "apgar_events.result_val_num", type: "integer"},
            {id: "apgar_events.result_val_str", label: "apgar_events.result_val_str", type: "string"},
            {id: "apgar_events.time_interval", label: "apgar_events.time_interval", type: "integer"},
            {
                id: "apgar_events.valid_from_dt_tm",
                label: "apgar_events.valid_from_dt_tm",
                type: "date",
                plugin: "datepicker",
                plugin_config: {
                    format: 'yyyy/mm/dd',
                    todayBtn: 'linked',
                    todayHighlight: true,
                    autoclose: true
                }
            },
            {id: "apgarscore.clinical_event_id", label: "apgarscore.clinical_event_id", type: "integer"},
            {id: "apgarscore.display_key", label: "apgarscore.display_key", type: "integer"},
            {id: "apgarscore.encntr_id", label: "apgarscore.encntr_id", type: "integer"},
            {id: "apgarscore.item_id", label: "apgarscore.item_id", type: "integer"},
            {id: "apgarscore.order_id", label: "apgarscore.order_id", type: "integer"},
            {id: "apgarscore.parent_event_id", label: "apgarscore.parent_event_id", type: "integer"},
            {id: "apgarscore.person_id", label: "apgarscore.person_id", type: "integer"},
            {id: "apgarscore.result_val", label: "apgarscore.result_val", type: "string"},
            {id: "birth_events.baby_name", label: "birth_events.baby_name", type: "string"},
            {id: "birth_events.display_key", label: "birth_events.display_key", type: "integer"},
            {id: "birth_events.encntr_id", label: "birth_events.encntr_id", type: "integer"},
            {id: "birth_events.event_tag", label: "birth_events.event_tag", type: "string"},
            {id: "birth_events.normalcy_display", label: "birth_events.normalcy_display", type: "string"},
            {id: "birth_events.person_id", label: "birth_events.person_id", type: "integer"},
            {id: "birth_events.units", label: "birth_events.units", type: "string"},
            {
                id: "birthdatetime.birth_date_time",
                label: "birthdatetime.birth_date_time",
                type: "date",
                plugin: "datepicker",
                plugin_config: {
                    format: 'yyyy/mm/dd',
                    todayBtn: 'linked',
                    todayHighlight: true,
                    autoclose: true
                }
            },
            {id: "birthdatetime.encntr_id", label: "birthdatetime.encntr_id", type: "integer"},
            {id: "birthdatetime.label_name", label: "birthdatetime.label_name", type: "string"},
            {id: "birthdatetime.person_id", label: "birthdatetime.person_id", type: "integer"},
            {id: "delivery_outcomes.encntr_id", label: "delivery_outcomes.encntr_id", type: "integer"},
            {id: "delivery_outcomes.person_id", label: "delivery_outcomes.person_id", type: "integer"},
            {id: "delivery_outcomes.primary_proc_ind", label: "delivery_outcomes.primary_proc_ind", type: "integer"},
            {
                id: "delivery_outcomes.procedure_start_date",
                label: "delivery_outcomes.procedure_start_date",
                type: "date",
                plugin: "datepicker",
                plugin_config: {
                    format: 'yyyy/mm/dd',
                    todayBtn: 'linked',
                    todayHighlight: true,
                    autoclose: true
                }
            },
            {id: "delivery_outcomes.procedure_text", label: "delivery_outcomes.procedure_text", type: "string"},
            {id: "delivery_outcomes.procedure_type", label: "delivery_outcomes.procedure_type", type: "string"},
            {id: "delivery_outcomes.schedule_type", label: "delivery_outcomes.schedule_type", type: "string"},
            {
                id: "delivery_outcomes.surgery_start_date",
                label: "delivery_outcomes.surgery_start_date",
                type: "date",
                plugin: "datepicker",
                plugin_config: {
                    format: 'yyyy/mm/dd',
                    todayBtn: 'linked',
                    todayHighlight: true,
                    autoclose: true
                }
            },
            {
                id: "delivery_outcomes.surgery_stop_date",
                label: "delivery_outcomes.surgery_stop_date",
                type: "date",
                plugin: "datepicker",
                plugin_config: {
                    format: 'yyyy/mm/dd',
                    todayBtn: 'linked',
                    todayHighlight: true,
                    autoclose: true
                }
            },
            {id: "delivery_outcomes.surgical_case_id", label: "delivery_outcomes.surgical_case_id", type: "integer"},
            {id: "diagnosis.active_ind", label: "diagnosis.active_ind", type: "integer"},
            {
                id: "diagnosis.beg_effective_dt_tm",
                label: "diagnosis.beg_effective_dt_tm",
                type: "date",
                plugin: "datepicker",
                plugin_config: {
                    format: 'yyyy/mm/dd',
                    todayBtn: 'linked',
                    todayHighlight: true,
                    autoclose: true
                }
            },
            {id: "diagnosis.d_classification_disp", label: "diagnosis.d_classification_disp", type: "string"},
            {id: "diagnosis.d_diag_type_disp", label: "diagnosis.d_diag_type_disp", type: "string"},
            {id: "diagnosis.d_present_on_admit_disp", label: "diagnosis.d_present_on_admit_disp", type: "string"},
            {id: "diagnosis.d_ranking_disp", label: "diagnosis.d_ranking_disp", type: "string"},
            {id: "diagnosis.d_severity_class_disp", label: "diagnosis.d_severity_class_disp", type: "string"},
            {id: "diagnosis.d_severity_disp", label: "diagnosis.d_severity_disp", type: "string"},
            {id: "diagnosis.diag_dt_tm", label: "diagnosis.diag_dt_tm", type: "string"},
            {id: "diagnosis.diagnosis_id", label: "diagnosis.diagnosis_id", type: "string"},
            {id: "diagnosis.encntr_id", label: "diagnosis.encntr_id", type: "integer"},
            {
                id: "diagnosis.end_effective_dt_tm",
                label: "diagnosis.end_effective_dt_tm",
                type: "date",
                plugin: "datepicker",
                plugin_config: {
                    format: 'yyyy/mm/dd',
                    todayBtn: 'linked',
                    todayHighlight: true,
                    autoclose: true
                }
            },
            {id: "diagnosis.n_active_status_disp", label: "diagnosis.n_active_status_disp", type: "string"},
            {id: "diagnosis.n_concept_source_disp", label: "diagnosis.n_concept_source_disp", type: "string"},
            {id: "diagnosis.n_contributor_system_disp", label: "diagnosis.n_contributor_system_disp", type: "string"},
            {id: "diagnosis.n_source_vocabulary_disp", label: "diagnosis.n_source_vocabulary_disp", type: "string"},
            {id: "diagnosis.n_string_source_disp", label: "diagnosis.n_string_source_disp", type: "string"},
            {id: "diagnosis.person_id", label: "diagnosis.person_id", type: "integer"},
            {id: "diagnosis.probability", label: "diagnosis.probability", type: "integer"},
            {id: "diagnosis.source_identifier", label: "diagnosis.source_identifier", type: "string"},
            {id: "diagnosis.source_string", label: "diagnosis.source_string", type: "string"},
            {id: "diagnosis.source_string_keycap_a_nls", label: "diagnosis.source_string_keycap_a_nls", type: "string"},
            {id: "dt_apgar_items.item_id", label: "dt_apgar_items.item_id", type: "integer"},
            {id: "dt_apgar_items.label", label: "dt_apgar_items.label", type: "string"},
            {id: "dt_apgarscore.event_cd", label: "dt_apgarscore.event_cd", type: "integer"},
            {id: "dt_apgarscore.event_description", label: "dt_apgarscore.event_description", type: "string"},
            {id: "dt_apgarscore.item_id", label: "dt_apgarscore.item_id", type: "integer"},
            {id: "dt_birth_events.display_key", label: "dt_birth_events.display_key", type: "string"},
            {id: "dt_birth_events.item_id", label: "dt_birth_events.item_id", type: "integer"},
            {
                id: "dt_diagnosis.n_source_vocabulary_disp",
                label: "dt_diagnosis.n_source_vocabulary_disp",
                type: "string"
            },
            {id: "dt_diagnosis.source_identifier", label: "dt_diagnosis.source_identifier", type: "string"},
            {id: "dt_diagnosis.source_string", label: "dt_diagnosis.source_string", type: "string"},
            {id: "dt_icd_procedures.code", label: "dt_icd_procedures.code", type: "string"},
            {id: "dt_icd_procedures.description", label: "dt_icd_procedures.description", type: "string"},
            {id: "dt_icd_procedures.type", label: "dt_icd_procedures.type", type: "string"},
            {id: "dt_lab_items.item_id", label: "dt_lab_items.item_id", type: "integer"},
            {id: "dt_lab_items.label", label: "dt_lab_items.label", type: "string"},
            {id: "dt_lab_items_category.category_id", label: "dt_lab_items_category.category_id", type: "integer"},
            {id: "dt_lab_items_category.label", label: "dt_lab_items_category.label", type: "string"},
            {id: "dt_labitems.labitem_description", label: "dt_labitems.labitem_description", type: "string"},
            {
                id: "dt_labitems.labitem_description_category",
                label: "dt_labitems.labitem_description_category",
                type: "string"
            },
            {id: "dt_para_events.display_key", label: "dt_para_events.display_key", type: "string"},
            {id: "dt_para_events.item_id", label: "dt_para_events.item_id", type: "integer"},
            {id: "dt_vitals.vitals_event", label: "dt_vitals.vitals_event", type: "string"},
            {id: "encounters.admission_location", label: "encounters.admission_location", type: "string"},
            {id: "encounters.admission_type", label: "encounters.admission_type", type: "string"},
            {id: "encounters.admit_reason", label: "encounters.admit_reason", type: "string"},
            {id: "encounters.admittime", label: "encounters.admittime", type: "string"},
            {
                id: "encounters.birth_dt",
                label: "encounters.birth_dt",
                type: "date",
                plugin: "datepicker",
                plugin_config: {
                    format: 'yyyy/mm/dd',
                    todayBtn: 'linked',
                    todayHighlight: true,
                    autoclose: true
                }
            },
            {id: "encounters.discharge_disposition", label: "encounters.discharge_disposition", type: "string"},
            {id: "encounters.discharge_location", label: "encounters.discharge_location", type: "string"},
            {id: "encounters.dischtime", label: "encounters.dischtime", type: "string"},
            {id: "encounters.encntr_id", label: "encounters.encntr_id", type: "integer"},
            {id: "encounters.ethnicity", label: "encounters.ethnicity", type: "string"},
            {id: "encounters.insurance", label: "encounters.insurance", type: "string"},
            {id: "encounters.language", label: "encounters.language", type: "string"},
            {id: "encounters.marital_status", label: "encounters.marital_status", type: "string"},
            {id: "encounters.person_id", label: "encounters.person_id", type: "integer"},
            {id: "encounters.reg_dt_tm", label: "encounters.reg_dt_tm", type: "string"},
            {id: "encounters.religion", label: "encounters.religion", type: "string"},
            {id: "fhr_vitals.encntr_id", label: "fhr_vitals.encntr_id", type: "integer"},
            {id: "fhr_vitals.normal_high", label: "fhr_vitals.normal_high", type: "string"},
            {id: "fhr_vitals.normal_low", label: "fhr_vitals.normal_low", type: "string"},
            {id: "fhr_vitals.person_id", label: "fhr_vitals.person_id", type: "integer"},
            {id: "fhr_vitals.c_event_disp", label: "fhr_vitals.c_event_disp", type: "string"},
            {id: "labevents.charttime", label: "labevents.charttime", type: "string"},
            {id: "labevents.contributor_system", label: "labevents.contributor_system", type: "string"},
            {id: "labevents.encntr_id", label: "labevents.encntr_id", type: "integer"},
            {id: "labevents.flag", label: "labevents.flag", type: "string"},
            {id: "labevents.item_id", label: "labevents.item_id", type: "string"},
            {id: "labevents.normal_high", label: "labevents.normal_high", type: "string"},
            {id: "labevents.normal_low", label: "labevents.normal_low", type: "string"},
            {id: "labevents.numvalue", label: "labevents.numvalue", type: "string"},
            {id: "labevents.person_id", label: "labevents.person_id", type: "integer"},
            {id: "labevents.value", label: "labevents.value", type: "string"},
            {id: "labevents.valuenum_decimal", label: "labevents.valuenum_decimal", type: "integer"},
            {
                id: "patients.dob", label: "patients.dob", type: "date", plugin: "datepicker", plugin_config: {
                    format: 'yyyy/mm/dd',
                    todayBtn: 'linked',
                    todayHighlight: true,
                    autoclose: true
                }
            },
            {id: "patients.ethnicity", label: "patients.ethnicity", type: "string"},
            {id: "patients.gender", label: "patients.gender", type: "string"},
            {id: "patients.marital_status", label: "patients.marital_status", type: "string"},
            {id: "patients.race", label: "patients.race", type: "string"},
            {id: "patients.religion", label: "patients.religion", type: "string"},
            {id: "patients.state", label: "patients.state", type: "string"},
            {id: "patients.subject_id", label: "patients.subject_id", type: "integer"},
            {id: "patients.veteran_status", label: "patients.veteran_status", type: "string"},
            {id: "patients.zip_code", label: "patients.zip_code", type: "string"},
            {id: "patients.zipcode", label: "patients.zipcode", type: "string"},
            {
                id: "procedures_icd.begin_dt_tm",
                label: "procedures_icd.begin_dt_tm",
                type: "date",
                plugin: "datepicker",
                plugin_config: {
                    format: 'yyyy/mm/dd',
                    todayBtn: 'linked',
                    todayHighlight: true,
                    autoclose: true
                }
            },
            {id: "procedures_icd.code", label: "procedures_icd.code", type: "string"},
            {id: "procedures_icd.contributor_source", label: "procedures_icd.contributor_source", type: "string"},
            {id: "procedures_icd.encntr_id", label: "procedures_icd.encntr_id", type: "integer"},
            {
                id: "procedures_icd.end_dt_tm",
                label: "procedures_icd.end_dt_tm",
                type: "date",
                plugin: "datepicker",
                plugin_config: {
                    format: 'yyyy/mm/dd',
                    todayBtn: 'linked',
                    todayHighlight: true,
                    autoclose: true
                }
            },
            {id: "procedures_icd.person_id", label: "procedures_icd.person_id", type: "integer"},
            {id: "procedures_icd.proc_desc", label: "procedures_icd.proc_desc", type: "string"},
            {id: "procedures_icd.seq_num", label: "procedures_icd.seq_num", type: "integer"},
            {id: "procedures_icd.source_vocabulary", label: "procedures_icd.source_vocabulary", type: "string"},
            {id: "procedures_icd.type", label: "procedures_icd.type", type: "string"},
            {id: 'empty', label: '----------------------', type: 'string', default_value: '  '}
        ],
        rules: rules_basic
    });
    /****************************************************************
     Triggers and Changers QueryBuilder
     *****************************************************************/


    $('#btn-get-quick').on('click', function () {
        // var x = document.getElementById("loader");
        // if (x.style.display === "none") {
        //     x.style.display = "block";
        // }
        var result = $('#builder').queryBuilder('getRules');
        if (!$.isEmptyObject(result)) {
            //alert(JSON.stringify(result, null, 2));
        } else {
            console.log("invalid object :");
        }
        console.log(result);

        var queryJson = {'quick': true, "rules": result}
        if (!$.isEmptyObject(result)) {
            callServer(queryJson)
        }
    });

    $('#btn-get').on('click', function () {
        // var x = document.getElementById("loader");
        // if (x.style.display === "none") {
        //     x.style.display = "block";
        // }
        var result = $('#builder').queryBuilder('getRules');
        if (!$.isEmptyObject(result)) {
            //alert(JSON.stringify(result, null, 2));
        } else {
            console.log("invalid object :");
        }
        console.log(result);

        // var queryJson = result
        var queryJson = {'quick': false, "rules": result}
        if (!$.isEmptyObject(result)) {
            callServer(queryJson)
        }
    });

    $('#btn-reset').on('click', function () {
        $('#builder').queryBuilder('reset');
        $("#downloadForm").hide();
    });

    $('#btn-set').on('click', function () {
        //$('#builder').queryBuilder('setRules', rules_basic);
        var result = $('#builder').queryBuilder('getRules');
        if (!$.isEmptyObject(result)) {
            rules_basic = result;
        }
    });

    //When rules changed :
    $('#builder').on('getRules.queryBuilder.filter', function (e) {
        //$log.info(e.value);
    });

});

function callServer(queryJsonObj) {

    queryJson = JSON.stringify(queryJsonObj)

    //alert(queryJson)
    fetch('http://127.0.0.1:5000//getQueryResults', {
        method: "POST",
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(queryJsonObj)
    })
        .then((response) => {
            return response.json();

        })
        .then((data) => {
            console.log("SQL excuted:\n", data['sql'])
            // console.log("data from sever", data['data_json'])
            if ($.isEmptyObject(data['data_json'])) {
                alert("The result is empty!")
            }
            var data_json = JSON.parse(data['data_json'])
            console.log(data_json)
            displayResults(data_json)
            // var x = document.getElementById("loader");
            // if (x.style.display === "block") {
            //     x.style.display = "none";
            // }
        });
}

// TO display results from sever in tabular form
function displayResults(data) {


    var arrItems = [];      // THE ARRAY TO STORE JSON ITEMS.
    $.each(data, function (index, value) {
        arrItems.push(value);       // PUSH THE VALUES INSIDE THE ARRAY.
    });


    var col = [];
    for (var i = 0; i < arrItems.length; i++) {
        for (var key in arrItems[i]) {
            if (col.indexOf(key) === -1) {
                col.push(key);
            }
        }
    }

    var titles = [];
    for (var i = 0; i < col.length; i++) {
        var title_dict = {}
        title_dict["title"] = col[i];
        titles.push(title_dict)
    }

    var dataSet = [];
    for (var i = 0; i < arrItems.length; i++) {

        var row = []

        for (var j = 0; j < col.length; j++) {
            row.push(arrItems[i][col[j]]);
        }

        dataSet.push(row)
    }


    // CREATE DYNAMIC TABLE.
    var table = document.createElement("table");
    table.id = "tb_show";

    // CREATE HTML TABLE HEADER ROW USING THE EXTRACTED HEADERS ABOVE.

    var tr = table.insertRow(-1);                   // TABLE ROW.

    for (var i = 0; i < col.length; i++) {
        var th = document.createElement("th");      // TABLE HEADER.
        th.innerHTML = col[i];
        tr.appendChild(th);
    }

    // ADD JSON DATA TO THE TABLE AS ROWS.
    for (var i = 0; i < arrItems.length; i++) {

        tr = table.insertRow(-1);

        for (var j = 0; j < col.length; j++) {
            var tabCell = tr.insertCell(-1);
            tabCell.innerHTML = arrItems[i][col[j]];
        }
    }

    // FINALLY ADD THE NEWLY CREATED TABLE WITH JSON DATA TO A CONTAINER.
    var divContainer = document.getElementById("showData");
    divContainer.innerHTML = "";
    divContainer.appendChild(table);

    $('#tb_show').DataTable({
        data: dataSet,
        columns: titles
    });

    var countLable = document.getElementById("countLable")

    countLable.innerHTML = "Total no of Records retrieved : " + arrItems.length
    countLable.style["color"] = "red"
    countLable.style["display"] = 'inline'

    $("#downloadForm").show();

}


// Modal code - Begin
$(document).ready(function () {
    $("#myModal").on('shown.bs.modal', function () {
        var saveQueryModalForm = document.getElementById("modalForm")
        saveQueryModalForm.reset()
        $(this).find('input[type="text"]').focus();
    });
});


function onSaveModalClick() {
    var queryName = document.getElementById("txtBoxQueryName").value;
    var comments = document.getElementById("txtBoxComments").value;
    var queryJsonObj = $('#builder').queryBuilder('getRules');

    if (!$.isEmptyObject(queryJsonObj)) {
        var queryJsonString = JSON.stringify(queryJsonObj)
    } else {
        swal({
            text: "invalid Query : Please check the Query",
            icon: "error",
            button: "ok",
        });
        $('#myModal').modal('hide');
        return
    }

    if (queryName == "") {
        swal({
            text: "Query Name is required",
            icon: "error",
            button: "ok",
        });
        return;
    }

    var saveObj = {"queryName": queryName, "comments": comments, "queryJsonString": queryJsonString};

    fetch('http://127.0.0.1:5000//saveQuery', {
        method: "POST",
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(saveObj)
    })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            console.log("Save Query Response", data)
            if (data["result"] == "success") {
                swal({
                    text: "Query Saved Successfuly!",
                    icon: "success",
                    button: "ok",
                });
                $('#myModal').modal('hide');
                return
            } else {
                swal({
                    text: "There was a Error while Saving the Query. Please Try Again",
                    icon: "error",
                    button: "ok",
                });
            }
        });
}

// Modal code - End

function onSelectModalClick() {
    var query_string = $("#bt-select").data('value');
    console.log("Selected Query : ", query_string);
    $('#builder').queryBuilder('setRules', query_string);

    $('#myModal-select').modal('hide');
}

// on selectFields click
function onSelectFieldsModalClick() {
    //TO-DO
    var rules = $('#builder').queryBuilder('getRules');
    var fields_interest = {"interest-fields": [], "rules": rules};
    $.each($("input[name='interest']:checked"), function () {
            fields_interest["interest-fields"].push($(this).val());
        });
    console.log("interest fileds and rules",fields_interest)
    callServer(fields_interest)
    $('#myModal-selectFields').modal('hide');
    // get the checked values of fields shown and show only those fileds in the result
}

// on click of selct fields
$(document).ready(function () {
    $("#myModal-selectFields").on('shown.bs.modal', function () {
        $('#selctFiledsContainer').empty();
        var query = $('#builder').queryBuilder('getRules');
        rules = query["rules"]

        var tablesList = []
        var selected_filters = []

        // tablesList.push("encounters")
        $('#selctFiledsContainer').append( '<div id="selctFileds-0" class="checkbox-selctFileds"></div> ')
        $(`#selctFileds-0`).append(
            '<input type="checkbox" name="select-all" id="select-all-0" class="select-all" checked>' +
            '<label for="select-all">encounters</label><br>' +
            '<p>----------</p> '+
            '<input type="checkbox" id="check_en_id" name="interest" value="encounters.encntr_id" class="selctFileds-chbox-0" checked> ' +
            '<label for="check_en_id">encounter id</label><br> ' +
            '<input type="checkbox" id="check_ps_id" name="interest" value="encounters.person_id" class="selctFileds-chbox-0" checked> ' +
            '<label for="${value}">person id</label><br>')

        for (var i = 0; i < rules.length; i++) {
            var table_name = (rules[i].id).split(".")[0]
            selected_filters.push(rules[i].id)
            if(!(tablesList.includes(table_name))){
                tablesList.push(table_name)
            }
        }
        console.log("selected_filters",selected_filters)

        //console.log(tablesToColumnsMap)
        for (var i = 0; i < tablesList.length; i++) {
            $('#selctFiledsContainer').append(`<div id="selctFileds-${i+1}" class="checkbox-selctFileds"></div>`);
            $(`#selctFileds-${i+1}`)
                .append(`<input type="checkbox" name="select-all" id="select-all-${i+1}" class="select-all"/>`)
                .append(`<label for="select-all">${tablesList[i]}</label><br>`)
                .append('<p>----------</p> ')

            columnsList = []
            columns = tablesToColumnsMap_1[tablesList[i]]
            for (var j = 0; j < columns.length; j++) {
                columnsList.push(columns[j])
            }
            for (var value of columnsList) {
                if(selected_filters.includes(`${tablesList[i]}.${value}`)){
                    $(`#selctFileds-${i+1}`)
                    .append(`<input type="checkbox" id="selctFileds-chbox-${i+1}" class="selctFileds-chbox-${i+1}" name="interest" value="${tablesList[i]}.${value}" checked>`)
                    .append(`<label for="selctFileds-chbox-${i+1}">${value}</label></div>`)
                    .append(`<br>`);
                }
                else{
                    $(`#selctFileds-${i+1}`)
                    .append(`<input type="checkbox" id="selctFileds-chbox-${i+1}" class="selctFileds-chbox-${i+1}" name="interest" value="${tablesList[i]}.${value}">`)
                    .append(`<label for="selctFileds-chbox-${i+1}">${value}</label></div>`)
                    .append(`<br>`);
                }

            }
        }

        console.log("Fileds Based on selected Tables :", columnsList)
        //var continer = document.getElementById("selctFiledsContainer")

        $('.select-all').click(function(event) {
            var chbox_id = this.id
                var number = chbox_id.split("-")[2]
                console.log(chbox_id,number )
            if(this.checked) {
            // Iterate each checkbox
            $(`.selctFileds-chbox-${number}`).each(function() {
                this.checked = true;
                });
            } else {
            $(`.selctFileds-chbox-${number}`).each(function() {
                this.checked = false;
                });
            }
        });

    });

});

// on select of a query from saved table
$(document).ready(function () {
    $("#myModal-select").on('shown.bs.modal', function () {
        fetch('http://127.0.0.1:5000//selectQuery', {
            method: "POST",
            headers: {'Content-Type': 'application/json'},
        })
            .then((response) => {
                return response.json();

            })
            .then((data) => {
                var arrItems = [];
                $.each(data, function (index, value) {
                    arrItems.push(value);
                });

                console.log(arrItems)

                var col = [];
                for (var i = 0; i < arrItems.length; i++) {
                    for (var key in arrItems[i]) {
                        if (col.indexOf(key) === -1) {
                            col.push(key);
                        }
                    }
                }

                var table = document.createElement("table");
                table.id = "table-selectquery";
                table.className = "table table-hover";

                // var table = document.getElementById("table-selectquery");

                var tr = table.insertRow(-1);

                for (var i = 0; i < col.length - 1; i++) {
                    var th = document.createElement("th");      // TABLE HEADER.
                    if (i == 0) {
                        th.setAttribute('style', 'width: 10%;')
                    } else if (i == 1) {
                        th.setAttribute('style', 'width: 30%;')
                    }
                    th.innerHTML = col[i];
                    tr.appendChild(th);
                }


                for (var i = 0; i < arrItems.length; i++) {
                    tr = table.insertRow(-1);
                    tr.setAttribute('data-value', arrItems[i]['query_string']);
                    for (var j = 0; j < col.length - 1; j++) {
                        var tabCell = tr.insertCell(-1);
                        tabCell.innerHTML = arrItems[i][col[j]];
                    }
                }

                var divContainer = document.getElementById("select-query");
                divContainer.innerHTML = "";
                divContainer.appendChild(table);
            });

    });

    $("body").on("click", "#table-selectquery tr", function () {


        $('#table-selectquery tr').removeClass('tr-onclick');
        $(this).addClass('tr-onclick');

        var query_string = $(this).data('value');
        //console.log(query_string);
        var bt_select = document.getElementById("bt-select");

        bt_select.setAttribute("data-value", JSON.stringify(query_string));

    });
});

// on result table row click
$(document).ready(function () {
    $("body").on("click", "#tb_show td", function () {
        var clickedTd = $(this)
        var $row = jQuery(this).closest('tr');
        $('#tb_show tr').removeClass('tr-onclick');
        $row.addClass('tr-onclick');
        //var $tableHeader = jQuery(this).closest('th');
        var $th = clickedTd.closest('table').find('th').eq($row.index());

        var tableHeaderValues = []
        $("table thead tr th").each(function (index) {
            tableHeaderValues.push($(this).text())
        });

        var rowValues = []
        jQuery(this).closest('tr').each(function () {
            $(this).find('td').each(function () {
                rowValues.push($(this)[0].innerHTML)
            })
        })

        var result = {};
        tableHeaderValues.forEach((key, i) => result[key] = rowValues[i]);
        console.log(" Im herere", result);

        var subjectId = result["person_id"]
        var encounterId = result["encntr_id"]



        if (subjectId && subjectId.length != 0 && encounterId && encounterId.length != 0) {
            // var x = document.getElementById("loader");
            // if (x.style.display === "none") {
            //     x.style.display = "block";
            // }
            //window.open("fail.html", "width=200,height=100")
            //window.open ("login.html")
            swal({
                            //text: "Please wait 11 seconds",
                            //showSpinner: true,
                            //showLoader: true,
                            //icon: "success",
                            //button: "ok",
                            //timerProgressBar: true,
                            title: "Loading...",
                            text: "Please wait",
                            //icon: "https://www.picsum.photos/g/200/300",
                            icon: "https://upload.wikimedia.org/wikipedia/commons/b/b1/Loading_icon.gif",
                            // icon: "success",
                            // imageUrl: 'https://giphy.com/gifs/mashable-3oEjI6SIIHBdRxXI40/fullscreen',
                            // imageAlt: 'Custom image',
                            //button: "ok",
                            timer: 17500,
                        });

            fetch('http://127.0.0.1:5000//launcPlottingTool', {
                method: "POST",
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(result)
            })
                .then((response) => {
                    return response.json();
                })
                .then((data) => {
                    console.log("launcPlottingTool Response", data)
                    if (data[0]["result"] == "success") {
                        console.log(data[0]["subId"],data[0]["randomNum"])
                        url = '/dashplot/'+data[0]["subId"]+data[0]["randomNum"]+'/'
                        console.log(url)
                        window.open('http://127.0.0.1:5000/'+url,'_blank');

                        //window.open("http://127.0.0.1:5000/", '_blank');
                        // var x = document.getElementById("loader");
                        // if (x.style.display === "block") {
                        //     x.style.display = "none";
                        // }
                        return
                    } else {
                        swal({
                            text: "There was a Error while Launching plotting tool",
                            icon: "error",
                            button: "ok",
                        });
                        // var x = document.getElementById("loader");
                        // if (x.style.display === "block") {
                        //     x.style.display = "none";
                        // }

                    }
                });
        }

    });
});


$(document).ready(function () {
    $("#downloadForm").hide();
});

$(document).ready(function () {
    $('#searchFormsubmit').on('click', function () {
        var searchValue = document.getElementById("searchValue").value;
        var rules = $('#builder').queryBuilder('getRules');
        var data = {'searchfield': false, "keywords": searchValue, "rules": rules};

        // console.log("rules here:",data)

        if (!$.isEmptyObject(data)) {
            searchKeywordsByValue(data)
        }
    });

    $('#searchfilterFormsubmit').on('click', function () {
        var searchValue = document.getElementById("searchfilterValue").value;
        var rules = $('#builder').queryBuilder('getRules');
        var data = {'searchfield': true, "keywords": searchValue, "rules": rules};

        // console.log("rules here:",data)

        if (!$.isEmptyObject(data)) {
            searchKeywords(data)
        }
    });

    $('#searchfield-add').on('click', function () {

        var rules = $('#builder').queryBuilder('getRules');
        var fields_select = {'searchfield': true, "fields": [], "rules": rules};
        $.each($("input[name='fieldcheckbox']:checked"), function () {
            fields_select["fields"].push($(this).val());
        });
        console.log(fields_select)
        fetch('http://127.0.0.1:5000//get_search_rules', {
            method: "POST",
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(fields_select)
        })
            .then((response) => {

                return response.json();

            })
            .then((data) => {
                $('#builder').queryBuilder('setRules', data);
            });
    });

    $('#searchvalue-add').on('click', function () {

        var rules = $('#builder').queryBuilder('getRules');
        var fields_select = {'searchfield': false, "fields": [], "rules": rules};
        $.each($("input[name='valuecheckbox']:checked"), function () {
            fields_select["fields"].push($(this).val());
        });
        console.log(fields_select)
        fetch('http://127.0.0.1:5000//get_search_rules', {
            method: "POST",
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(fields_select)
        })
            .then((response) => {

                return response.json();

            })
            .then((data) => {
                $('#builder').queryBuilder('setRules', data);
            });
    });

});

function searchKeywords(data) {
    fetch('http://127.0.0.1:5000//searchDt', {
        method: "POST",
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            var fieldItems = []
            $.each(data, function (index, value) {
                fieldItems.push(value);
            });
            console.log("search result:", fieldItems)

            $('#checkbox-field').empty();

            for (var i = 0; i < fieldItems.length; i++) {
                var checkbox_id = Math.floor(i / 4)
                if (i % 4 == 0) {
                    $('#checkbox-field').append(`<div id="checkbox-searchfield-${checkbox_id}"></div>`);
                }
                $(`#checkbox-searchfield-${checkbox_id}`).append(
                    $(document.createElement('input')).prop({
                        id: `myCheckBox${i}`,
                        name: `fieldcheckbox`,
                        value: `${fieldItems[i]}`,
                        type: 'checkbox'
                    })
                ).append(
                    $(document.createElement('label')).prop({
                        for: `myCheckBox${i}`
                    }).html(`\xa0${fieldItems[i]}\xa0\xa0`)
                ).append(document.createElement('br'));

                // if ((i+1)%4==0){
                //     $('#checkbox-field').append(document.createElement('br'));
                // }
            }
        });
}

function searchKeywordsByValue(data) {
    fetch('http://127.0.0.1:5000//searchDt', {
        method: "POST",
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            var fieldItems = []
            $.each(data, function (index, value) {
                fieldItems.push(value);
            });
            console.log("search result:", fieldItems)

            $('#checkbox-value').empty();

            for (var i = 0; i < fieldItems.length; i++) {
                var checkbox_id = Math.floor(i / 4)
                if (i % 4 == 0) {
                    $('#checkbox-value').append(`<div id="checkbox-searchvalue-${checkbox_id}"></div>`);
                }

                $(`#checkbox-searchvalue-${checkbox_id}`).append(
                    $(document.createElement('input')).prop({
                        id: `myCheckBox${i}`,
                        name: `valuecheckbox`,
                        value: `${fieldItems[i]}`,
                        type: 'checkbox'
                    })
                ).append(
                    $(document.createElement('label')).prop({
                        for: `myCheckBox${i}`
                    }).html(`\xa0${fieldItems[i]}\xa0\xa0`)
                ).append(document.createElement('br'));

                // if ((i+1)%3==0){
                //     $('#checkbox-value').append(document.createElement('br'));
                // }
            }
        });
}
