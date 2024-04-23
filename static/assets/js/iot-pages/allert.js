setInterval(function () {
    $.ajax({
        url: '/allert/',  // Django视图的URL
        success: function (data) {
            // 更新页面的代码
            // location.reload();
            // 例如，你可以使用jQuery的.html()方法更新一个元素的内容
            // $('#my-element').html(data);
            // console.log(data);
            for (var i = 0; i < data['msg'].length; i++) {
                alert('有新的警报 \n 内容：' + data[i]);
            }
        }
    });
}, 1000);  