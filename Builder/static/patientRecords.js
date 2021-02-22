$(document).ready(function () {
    $("#patientRecordsNav button").click(function () {
        $('#patientRecordsNav button').removeClass('active');
        $(this).addClass('active');

        var patientId = document.getElementById("patientID-select").value;
        var encounterId = document.getElementById("encntrID-select").value;
        var tab_id = this.id;
        var para = {"patientId":patientId,"encntrId":encounterId,"tab_id":tab_id}
        console.log(tab_id)
        callServer(para)
    });

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
        // console.log("clicked row", result);

        var subjectId = result["person_id"]
        var encounterId = result["encntr_id"]
        $("#encntrID-select").val(encounterId)

    });
});

function callServer(para) {
    fetch('http://127.0.0.1:5000//patientID_select', {
            method: "POST",
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(para)
        })
            .then((response) => {

                return response.json();

            })
            .then((data) => {
                var data_json = JSON.parse(data);

                displayResults(data_json)
            });
}

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
    var divContainer = document.getElementById("showData_pr");
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

}

$(document).ready(function () {
    $('.date_select_id').change(function(){

        var parentNode = document.getElementById(this.id).parentElement;
        console.log(parentNode.childNodes)
        var data_name = parentNode.childNodes[3].name;
        var startdate = parentNode.childNodes[3].value;
        var enddate = parentNode.childNodes[5].value;

        var patientId = document.getElementById("patientID-select").value;

        var date_para = {"data_name":data_name,"startdate":startdate,"enddate":enddate,"patientId":patientId}
        console.log(data_name,startdate,enddate)

        fetch('http://127.0.0.1:5000//id_group_by_date', {
            method: "POST",
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(date_para)
        })
            .then((response) => {

                return response.json();

            })
            .then((data) => {
                var data_json = JSON.parse(data);

                console.log(data_json)

                var arrItems = [];      // THE ARRAY TO STORE JSON ITEMS.
                $.each(data_json, function (index, value) {
                    arrItems.push(value);       // PUSH THE VALUES INSIDE THE ARRAY.
                });

                var id_type = "";
                var id_select = "";
                if(data_name == "birth_dt"){
                    id_type = 'person_id'
                    id_select = "#patientID-select"

                    $(id_select).empty();

                    for (var i = 0; i < arrItems.length; i++) {
                        var option_value = arrItems[i][id_type]
                        $(id_select).append(`<option value=${option_value}>
                                       ${option_value}
                                  </option>`);
                    }
                }else{
                    id_type = 'encntr_id'
                    id_select = "#encntrID-select1"

                    $(id_select).empty();

                    for (var i = 0; i < arrItems.length; i++) {
                    var option_value = arrItems[i][id_type]
                    $(id_select).append(`<option value=${option_value}>`);
                    }
                }

            });
    });

    $('#encntrID-select1').change(function(){
        $("#encntrID-select").val(this.value);
    });

});