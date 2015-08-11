/**
 * Created by Riven on 2015-08-03.
 */
var cos = Math.cos;
var sin = Math.sin;
var sqrt = Math.sqrt;
var atan = Math.atan;
var pi = Math.PI;

var scaraRobot = {
    L1: 168.0,
    L2: 206.0,
    centx: 0,
    centy: 0,
    biasx: 0,
    biasy: 0,
    posX: -this.L1-this.L2,
    posY: 0,
    th0: 0,
    th1: 0,

    init: function(setup){
        robotUtils.cleanCanvas();
        var svg = document.getElementsByTagName('svg')[0]; //Get svg element
        var cx = svg.offsetWidth/2;
        var cy = svg.offsetHeight/2;
        this.centx = cx;
        this.centy = cy;
        this.biasx = svg.offsetTop;
        this.biasy = svg.offsetLeft;

        var circleInner = robotUtils.drawCircle(cx, cy, this.L1);
        svg.appendChild(circleInner);
        var circleOuter = robotUtils.drawCircle(cx, cy, (this.L1+this.L2));
        svg.appendChild(circleOuter);

        var armL1 = robotUtils.drawLine(cx,cy,cx-this.L1,cy);
        armL1.setAttribute("id","armL1");
        svg.appendChild(armL1);

        var armL2 = robotUtils.drawLine(cx-this.L1,cy,cx-this.L1-this.L2,cy);
        armL2.setAttribute("id","armL2");
        svg.appendChild(armL2);

        var dotCent = robotUtils.drawDot(cx,cy,"#00A9E7");
        svg.appendChild(dotCent);
        var dotL1 = robotUtils.drawDot(cx-this.L1,cy,"#00A9E7");
        dotL1.setAttribute("id","dotL1");
        svg.appendChild(dotL1);
        var dotL2 = robotUtils.drawDot(cx-this.L1-this.L2,cy,"#00A9E7");
        dotL2.setAttribute("id","dotL2");
        svg.appendChild(dotL2);

        this.robotMove(-this.L1-this.L2+0.01,0); // avoid NaN float

    },

    directKinect: function(th1,th2){
        var L1 = this.L1;
        var L2 = this.L2;
        var x1 = -L1*cos(th1);
        var y1 = L1*sin(th1);
        var x2 = -L1*cos(th1)-L2*cos(th1+th2-pi);
        var y2 = L1*sin(th1)+L2*sin(th1+th2-pi);
        return [x2,y2,x1,y1];
    },

    inverseKinect: function(x,y){
        var L1 = this.L1;
        var L2 = this.L2;
        var th1 = 2*atan((2*L1*y + sqrt(- L1*L1*L1*L1 + 2*L1*L1*L2*L2 + 2*L1*L1*x*x + 2*L1*L1*y*y - L2*L2*L2*L2 + 2*L2*L2*x*x + 2*L2*L2*y*y - x*x*x*x - 2*x*x*y*y - y*y*y*y))/(L1*L1 - 2*L1*x - L2*L2 + x*x + y*y));
        var th2 = 2*atan(sqrt((- L1*L1 + 2*L1*L2 - L2*L2 + x*x + y*y)*(L1*L1 + 2*L1*L2 + L2*L2 - x*x - y*y))/(L1*L1 + 2*L1*L2 + L2*L2 - x*x - y*y));
        return [th1,th2];
    },

    robotMove: function(x,y) {
        var theta=this.inverseKinect(x,y);
        var pos=this.directKinect(theta[0],theta[1]);

        $("#armL1").attr("x2",pos[2]+this.centx);
        $("#armL1").attr("y2",-pos[3]+this.centy);
        $("#armL2").attr("x1",pos[2]+this.centx);
        $("#armL2").attr("y1",-pos[3]+this.centy);
        $("#armL2").attr("x2",pos[0]+this.centx);
        $("#armL2").attr("y2",-pos[1]+this.centy);

        $("#dotL1").attr("cx",pos[2]+this.centx);
        $("#dotL1").attr("cy",-pos[3]+this.centy);
        $("#dotL2").attr("cx",pos[0]+this.centx);
        $("#dotL2").attr("cy",-pos[1]+this.centy);
        $("#robot-pos-x").val(x);
        $("#robot-pos-y").val(y);

    },

    robotHome: function(){
        this.robotMove(-this.L1-this.L2+0.01,0); // avoid NaN float
    }



};


