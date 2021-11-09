        function getLongDate() {
            //创建当前系统时间的Date对象
            var dateObj = new Date();
            //获取完整年份值
            var year = dateObj.getFullYear();
            //获取月份
            var month = dateObj.getMonth() + 1;
            //获取月份中的日
            var date = dateObj.getDate();
            //获取星期值
            var day = dateObj.getDay();
            var weeks = ["星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"];
            //根据星期值，从数组中获取对应的星期字符串
            var week = weeks[day];
            //获取小时
            var hour = dateObj.getHours();
            //获取分钟
            var minute = dateObj.getMinutes();
            //获取秒钟
            var second = dateObj.getSeconds();
            //如果月、日、时、分、秒的值小于10，在前面补0
            if (month<10) {
                month="0"+month;
            }
            if (date<10) {
                date="0"+date;
            }
            if (hour<10) {
                hour="0"+hour;
            }
            if (minute<10) {
                minute="0"+minute;
            }
            if (second<10) {
                second="0"+second;
            }
            var newDate=year+"年"+month+"月"+date+"日 "+week+" "+hour+":"+minute+":"+second;
            document.getElementById("dateStr").innerHTML="系统公告:["+newDate+"]";
            setTimeout("getLongDate()",1000);//每隔一秒重新调用一次该函数
            /*
                在实时显示系统时间时，还可以使用window对象的setIntervar()方法，
                setIntervar()方法类似于setTimeout()方法。
                不同之处是调用window对象的setIntervar()方法后，
                会一直执行setIntervar()方法所调用的JavaScript方法，
                而setTimeout()方法只能被执行一次。
                如果要通过setTimeout()方法一直执行某个JavaScript方法，
                setTimeout()必须写在被调用的JavaScript方法体内
            */
        }