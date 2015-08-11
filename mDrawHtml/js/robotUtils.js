/**
 * Created by Riven on 2015-08-03.
 */

var robotUtils = {

    cleanCanvas: function(){
        $("#canvas").empty();
    },

    drawCircle: function(cx,cy,r){
        var circle = document.createElementNS("http://www.w3.org/2000/svg", 'circle'); //Create a path in SVG's namespace
        circle.setAttribute("cx",cx);
        circle.setAttribute("cy",cy);
        circle.setAttribute("r",r);
        circle.style.fill = "none";
        circle.style.stroke = "#000";
        circle.style.strokeWidth = "1px";
        return circle;
    },

    drawDot: function(cx,cy,color){
        var circle = document.createElementNS("http://www.w3.org/2000/svg", 'circle'); //Create a path in SVG's namespace
        circle.setAttribute("cx",cx);
        circle.setAttribute("cy",cy);
        circle.setAttribute("r",5);
        circle.style.fill = color;
        circle.style.stroke = "none";
        return circle;
    },

    drawLine: function(x0,y0,x1,y1){
        var newLine = document.createElementNS('http://www.w3.org/2000/svg','line');
        newLine.setAttribute('x1',x0);
        newLine.setAttribute('y1',y0);
        newLine.setAttribute('x2',x1);
        newLine.setAttribute('y2',y1);
        newLine.setAttribute("stroke-width",2);
        newLine.style.stroke = "black";

        return newLine;
    },

    robotClickMove: function(x,y,robot){
        var tarx=(x-robot.centx);
        var tary=-(y-robot.centy);// y in reverse direction
        robot.robotMove(tarx,tary);
        this.G1(tarx,tary);
    },

    G1: function(x,y){
        this.send("G1 X"+ x.toFixed(2)+" Y"+ y.toFixed(2)+"\n");
    },

    G28: function(){
        this.send("G28\n");
    },

    M1: function(pos){ // pen position set
        this.send("M1 "+pos+"\n");
    },

    send: function(cmd){
        this.setRobotBusy(1);
        serial.send(cmd);
    },

    setRobotBusy: function(state){
        if(state==1){
            $("#label-idle").addClass("hidden");
            $("#label-busy").removeClass("hidden");
        }else{
            $("#label-idle").removeClass("hidden");
            $("#label-busy").addClass("hidden");
        }
    },

    parseEcho: function(msg){
        if(msg.indexOf("OK") > -1){
            this.setRobotBusy(0);
        }else{
            var psconsole = $('#console-log');
            psconsole.append(msg);
            if(psconsole.length)
                psconsole.scrollTop(psconsole[0].scrollHeight - psconsole.height());
        }
    }
};





