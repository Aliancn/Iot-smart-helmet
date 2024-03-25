'use strict';
$(document).ready(function () {
    setTimeout(settable(mydata), 300);
});
console.log("page-sta-insp.js");

function settable(mydata) {
    console.log("mydata:", mydata);
    if (mydata != null) {
        // [ Donut-chart ] Start

        var graph = Morris.Donut({
            element: 'morris-donut-chart',
            data: mydata,
            colors: [
                '#1de9b6',
                '#A389D4',
                '#04a9f5',
                '#1dc4e9',
            ],
            resize: true,
            formatter: function (x) {
                return "val : " + x
            }
        });
        // [ Donut-chart ] end
    } else {
        // [ Donut-chart ] Start
        var graph = Morris.Donut({
            element: 'morris-donut-chart',
            data: [{
                value: 60,
                label: '在岗'
            },
            {
                value: 20,
                label: '休息'
            },
            {
                value: 10,
                label: '请假'
            },
            {
                value: 5,
                label: '加班'
            }
            ],
            colors: [
                '#1de9b6',
                '#A389D4',
                '#04a9f5',
                '#1dc4e9',
            ],
            resize: true,
            formatter: function (x) {
                return "val : " + x
            }
        });
        // [ Donut-chart ] end
    }

}