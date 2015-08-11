var serial = null;

robotSetup={

};

$(document).ready(function () {

    $('#h-slider').slider({
        range: "min",
        min: 0,
        max: 100,
        value: 60,
        slide: function (event, ui) {
            //$("#amount").val(ui.value);
        }
    });

    $("#penup-spin").spinner();
    $("#pendown-spin").spinner();

    $("#btnLoadPic").on("click",function(event){
        chrome.fileSystem.chooseEntry({type: 'openFile', accepts: [{extensions: ['svg']}]}, function (fileEntry) {
            if (!fileEntry) {
                console.log('No file selected, restore aborted.');
                return;
            }
            loadFileEntry(fileEntry);
        });
    });

    $("#robot-dropdown").on("click","li a",function(event){
        var robotType = event.target.text;
        $("#robot-current").html(robotType+"<span class='caret'>");
        changeRobot(robotType);
    });

    serial = new SerialConnection();
    console.log(serial);
    serial.getDevices(function(ports){
        console.log(ports);
        var serialDrop = $("#serial-dropdown");
        serialDrop.empty();
        ports.forEach(function(port){
            var portStr = port.path;
            serialDrop.append("<li><a href='#'>"+portStr+"</a></li>");
        });
    });

    serial.onReadLine.addListener(onReadLine);

    //robot = new robotScara();

    $("#serial-dropdown").on("click",'li a',function(event){
        $("#serial-current").html(event.target.text+"<span class='caret'>");
    });

    $("#btnConnect").on("click",function(event) {
        if (serial.connectionId == -1) {
            var portStr = $("#serial-current").text();
            serial.connect(portStr, {bitrate: 115200}, onOpen);
        }else{
            var portStr = $("#serial-current").text();
            serial.disconnect(onClose);
        }
    });

    $("#btnSend").on("click", function(event){
        var txt = $("#input-line").val();
        serial.send(txt+"\n");
    });

    $("#btnHome").on("click",function(event){
        robotUtils.G28();
        window.robot.robotHome();
    });

    $("#canvas").on("dblclick", userMove);

    $("#btnPenUp").on("click",function(){
        var pos = $("#penup-spin").val();
        robotUtils.M1(pos);
    });

    $("#btnPenDown").on("click",function(){
        var pos = $("#pendown-spin").val();
        robotUtils.M1(pos);
    });

    // init robot type
    changeRobot("mScara");
    robotUtils.setRobotBusy(0);
});

function onOpen(openInfo){
    $("#btnConnect").text("disconn");
    setTimeout(function () {
        serial.send("M10\n");
    }, 2500); // late probe
}

function onClose(){
    $("#btnConnect").text("connect");
}

function onReadLine(msg){
    console.log('read line: ' + msg);
    robotUtils.parseEcho(msg);
}

function changeRobot(robot) {

    if (robot == "mScara") {
        $("#image-robot").attr("src", "./res/scara.png");
        scaraRobot.init(robotSetup);
        window.robot = scaraRobot;
    }else if(robot == "mSpider"){
        $("#image-robot").attr("src", "./res/spider.png");
    }else if(robot == "mEgg"){
        $("#image-robot").attr("src", "./res/egg.png");
    }else if(robot == "mCar"){
        $("#image-robot").attr("src", "./res/car.png");
    }else if(robot == "XY"){
        $("#image-robot").attr("src", "./res/xy.png");
    }
}

function userMove(event){
    var x = event.offsetX;
    var y = event.offsetY;
    console.log("X "+x+" Y "+y);
    robotUtils.robotClickMove(x,y,window.robot);

}

function errorHandler(e) {
    console.error(e);
}

function loadFileEntry(fileEntry) {
    fileEntry.file(function(file) {
        var reader = new FileReader();

        reader.onerror = errorHandler;
        reader.onload = function(e) {
            //callback(e.target.result);
            //console.log("read:\n"+ e.target.result);
            $("#load-pic").html(e.target.result);
        };

        reader.readAsText(file);
    });
}
