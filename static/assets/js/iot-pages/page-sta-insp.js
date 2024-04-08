'use strict';
$(document).ready(function () {
    setTimeout(settable(mydata), 200);
    setTimeout(smooth_line_table(mydata_line), 300);
});
console.log("page-sta-insp.js");

function settable(mydata) {
    console.log("mydata:", mydata);
    if (mydata.length != 0) {
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

function smooth_line_table(mydata_line) {
    console.log("mydata_line:", mydata_line);
    // [ line-smooth-chart ] start
    if (mydata_line.length != 0) {
        // [ line-smooth-chart ] start
        console.log("mydata_line not null");
        Morris.Line({
            element: 'morris-line-smooth-chart',
            data: mydata_line,
            xkey: 'y',
            redraw: true,
            resize: true,
            ykeys: ['a', 'b'],
            hideHover: 'auto',
            responsive: true,
            labels: ['Series A', 'Series B'],
            lineColors: ['#1de9b6', '#A389D4']
        });
        // [ line-smooth-chart ] end
    } else {
        // [ line-smooth-chart ] start
        Morris.Line({
            element: 'morris-line-smooth-chart',
            data: [{
                y: '2006',
                a: 100,
                b: 90
            },
            {
                y: '2007',
                a: 75,
                b: 65
            },
            {
                y: '2008',
                a: 50,
                b: 40
            },
            {
                y: '2009',
                a: 75,
                b: 65
            },
            {
                y: '2010',
                a: 50,
                b: 40
            },
            {
                y: '2011',
                a: 75,
                b: 65
            },
            {
                y: '2012',
                a: 100,
                b: 90
            }
            ],
            xkey: 'y',
            redraw: true,
            resize: true,
            ykeys: ['a', 'b'],
            hideHover: 'auto',
            responsive: true,
            labels: ['Series A', 'Series B'],
            lineColors: ['#1de9b6', '#A389D4']
        });
        // [ line-smooth-chart ] end
    }
}