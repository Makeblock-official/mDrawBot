import sys
import os
import time
from xml.dom import minidom
from PyQt4 import QtGui
from PyQt4.QtCore import *
from math import *


def buildBezierSegment(p0,p1,p2,p3):
    segList = []
    px=p0[0]
    py=p0[1]
    #print "bez",p0,p1,p2,p3
    for i in range(1,100):
        ratio = float(i)/100
        x00=p0[0]+(p1[0]-p0[0])*ratio;y00=p0[1]+(p1[1]-p0[1])*ratio
        x01=p1[0]+(p2[0]-p1[0])*ratio;y01=p1[1]+(p2[1]-p1[1])*ratio
        x02=p2[0]+(p3[0]-p2[0])*ratio;y02=p2[1]+(p3[1]-p2[1])*ratio
        x10=(x01-x00)*ratio+x00;y10=(y01-y00)*ratio+y00;
        x11=(x02-x01)*ratio+x01;y11=(y02-y01)*ratio+y01;
        x20=(x11-x10)*ratio+x10;y20=(y11-y10)*ratio+y10;
        dx = x20-px;dy = y20 - py;
        dis = sqrt(dx*dx+dy*dy)
        if dis>1:
            segList.append((x20,y20))
            px=x20;py=y20;
    if len(segList)==0:
        segList.append((p3[0],p3[1]))
    return segList

def buildArcSegment(rx,ry,phi,fA,fS,x1,y1,x2,y2):
    # fA: large arc flag
    # fS: sweep flag
    segList=[]
    # calc center for ellipse
    #print "from",x1,y1,x2,y2
    phi = phi/180*pi
    x1p = cos(phi)*(x1-x2)/2+sin(phi)*(y1-y2)/2
    y1p = -sin(phi)*(x1-x2)/2+cos(phi)*(y1-y2)/2
    lam = x1p*x1p/(rx*rx) + y1p*y1p/(ry*ry)
    if lam>1:
        rx = sqrt(lam)*rx
        ry = sqrt(lam)*ry
    
    # fix for math domain error
    tmp = (rx*rx*ry*ry-rx*rx*y1p*y1p-ry*ry*x1p*x1p)/(rx*rx*y1p*y1p+ry*ry*x1p*x1p)
    st = sqrt(round(tmp,5))
    if fA==fS:
        cp_sign = -1
    else:
        cp_sign = 1
    cxp = cp_sign*(st*rx*y1p/ry)
    cyp = cp_sign*(-st*ry*x1p/rx)
    cx = cos(phi)*cxp-sin(phi)*cyp+(x1+x2)/2
    cy = sin(phi)*cxp+cos(phi)*cyp+(y1+y2)/2
    #print "cent",cx,cy
    
    Vxc = (x1p-cxp)/rx
    Vyc = (y1p-cyp)/ry
    Vxc = (x1p-cxp)/rx
    Vyc = (y1p-cyp)/ry
    Vxcp = (-x1p-cxp)/rx
    Vycp = (-y1p-cyp)/ry
    
    if Vyc>=0:
        cp_sign=1
    else:
        cp_sign=-1
    th1 = cp_sign*acos(Vxc/sqrt(Vxc*Vxc+Vyc*Vyc))/pi*180
    
    if (Vxc*Vycp-Vyc*Vxcp)>=0:
        cp_sign=1
    else:
        cp_sign=-1
    tmp = (Vxc*Vxcp+Vyc*Vycp)/(sqrt(Vxc*Vxc+Vyc*Vyc)*sqrt(Vxcp*Vxcp+Vycp*Vycp))
    dth = cp_sign*acos(round(tmp,3))/pi*180
    #if fA>=1:
    #    dth=360-dth
    if fS==0 and dth>0:
        dth-=360
    elif fS>=1 and dth<0:
        dth+=360
    
    #print "angle",th1,dth
    
    # build route
    theta = th1/180*pi
    px = rx*cos(theta)+cx
    py = ry*sin(theta)+cy
    for i in range(1,101):
        ratio = float(i)/100
        theta = (th1+dth*ratio)/180*pi
        x = cos(phi)*rx*cos(theta)-sin(phi)*ry*sin(theta)+cx
        y = sin(phi)*rx*cos(theta)+cos(phi)*ry*sin(theta)+cy
        dx=x-px;dy=y-py;
        dis = sqrt(dx*dx+dy*dy)
        if dis>1:
            segList.append((x,y))
            px=x;py=y;
    return segList
    


class SvgParser():
    def __init__(self, filename,scene,scale=(1,1)):
        self.pathList = []
        self.originPathList = []
        self.ptrList = []
        self.tmpPath = None
        self.xbias = 0
        self.ybias = 0
        self.whratio = 1
        self.scene = scene
        self.scale = scale
        self.tf = []
        self.parse(filename)
    
    # tranform matrix = [ a c e ]
    #                   [ b d f ]
    def moveTo(self,x,y):
        for i in range(len(self.tf)):
            tf = self.tf[-1-i]
            x1=tf[0]*x+tf[2]*y+tf[4]
            y1=tf[1]*x+tf[3]*y+tf[5]
            x=x1
            y=y1

        initpoint = [(x,y)]
        self.originPathList.append(initpoint)
    
    def lineTo(self,x,y):
        for i in range(len(self.tf)):
            tf = self.tf[-1-i]
            x1=tf[0]*x+tf[2]*y+tf[4]
            y1=tf[1]*x+tf[3]*y+tf[5]
            x=x1
            y=y1

        point = (x,y)
        self.originPathList[-1].append(point)
    
    def plotToScene(self):
        self.ptrList = []
        pen = QtGui.QPen(QtGui.QColor(124, 124, 124))
        for line in self.pathList:
            tmpPath = QtGui.QPainterPath()
            for i in range(len(line)):
                point = line[i]
                if i==0:
                    tmpPath.moveTo(point[0],point[1])
                else:
                    tmpPath.lineTo(point[0],point[1])
            ptr = self.scene.addPath(tmpPath,pen=pen)
            self.ptrList.append(ptr)
    
   
    def resize(self,drawRect=(150,150,150,150)):
        #self.pathList = copy.deepcopy(self.originPathList)
        self.pathList=[]
        for p in self.originPathList:
            self.pathList.append(p)
        
        (x,y) = self.pathList[0][0]
        xmin = x*self.scale[0]
        xmax = x*self.scale[0]
        ymin = y*self.scale[1]
        ymax = y*self.scale[1]
        # find max min pos on x and y
        for line in self.pathList:
            for p in line:
                x = p[0]*self.scale[0]
                y = p[1]*self.scale[1]
                if x<xmin:
                    xmin = p[0]
                if x>xmax:
                    xmax = p[0]
                if y<ymin:
                    ymin = p[1]
                if y>ymax:
                    ymax = p[1]
        #print "size",xmin,ymin,xmax,ymax
        dx = xmax-xmin
        dy = ymax-ymin
        self.whratio = dx/dy
        scaler = min(drawRect[2]/dx,drawRect[3]/dy)

        for i in range(len(self.pathList)):
            for j in range(len(self.pathList[i])):
                x = self.pathList[i][j][0]*self.scale[0]
                y = self.pathList[i][j][1]*self.scale[1]
                x = (x-xmin)*scaler+drawRect[0]                    
                y = (y-ymin)*scaler+drawRect[1]
                self.pathList[i][j] = (x,y)
        return (dx*scaler,dy*scaler)
    
    # stretch for eggbot surface curve
    # eq: x^2/a^2+y^2/b^2 = 1
    # todo: apply a real egg shape equation: http://www.mathematische-basteleien.de/eggcurves.htm
    # http://www.geocities.jp/nyjp07/Egg/index_egg_E.html
    def stretch(self,ycent,h,da=20):
        a = h+da
        for i in range(len(self.pathList)):
            for j in range(len(self.pathList[i])):
                (x,y) = self.pathList[i][j]
                y0=y-ycent
                x0 = h-sqrt(1-y0*y0/a/a)*h
                x = x+x0
                self.pathList[i][j] = (x,y)
    
    def parsePath(self,node):
        pbuff=[]
                
        d = node.getAttribute("d")
        ds = d.replace("e-","ee")
        ds=ds.replace("-"," -").replace("s", " s ").replace("S", " S ").replace("c", " c ").replace("C", " C ").replace("v", " v ").replace("V", " V ")
        ds=ds.replace("l", " l ").replace("L"," L ").replace("A", " A ").replace("a", " a ").replace(",", " ").replace("M", "M ").replace("h", " h ").replace("H", " H ").replace("m"," m ").replace('z',' z ')
        ss=ds.split()
        for i in range(len(ss)):
            ss[i] = ss[i].replace("ee","e-")
        ptr=0
        state=""
        prevstate = ""
        curvecnt=0 # todo: Bezier Curve
        lastControl = (0,0) # the last control point buffer for s command
        x=self.xbias
        y=self.ybias
        x0=x;y0=y;
        #path = QtGui.QPainterPath()
        #print ">> path:",ss
        while ptr<len(ss):
            #print "parse",ss[i]
            if ss[ptr].isalpha():
                #print "into state",ss[ptr]
                prevstate = state
                state = ss[ptr]
                ptr+=1
                curvecnt=0
                if state=='C' or state=='c':
                    pbuff=[(x,y)]
                elif state=='z' or state=='Z':
                    x=x0;y=y0;
                    #path.moveTo(x0,y0)
                    self.lineTo(x0,y0)
                    #print ">>\tz:x",x,"y",y
                elif state=="s" or state=="S":
                    pbuff=[(x,y)]
            else:
                if state=="h":
                    dis=float(ss[ptr])
                    #print "h",dis
                    self.lineTo(x+dis,y)
                    x=x+dis;y=y
                    ptr+=1
                elif state=="H":
                    dis=float(ss[ptr])
                    self.lineTo(dis,y)
                    x=dis;y=y
                    ptr+=1
                elif state=="v":
                    dis=float(ss[ptr])
                    self.lineTo(x,y+dis)
                    x=x;y=y+dis
                    ptr+=1
                elif state=="V":
                    dis=float(ss[ptr])
                    self.lineTo(x,dis)
                    x=x;y=dis
                    ptr+=1
                elif state=="M":
                    ax=float(ss[ptr])+self.xbias
                    ay=float(ss[ptr+1])+self.ybias
                    ptr+=2
                    curvecnt+=1
                    #print ">>\tM:x",x,"y",y,curvecnt
                    x=ax;y=ay
                    if curvecnt>1:
                        #path.lineTo(x,y)
                        self.lineTo(x,y)
                    else:
                        #path.moveTo(x,y)
                        self.moveTo(x,y)
                        x0=x;y0=y # subpath start
                elif state=="m":
                    dx=float(ss[ptr])
                    dy=float(ss[ptr+1])
                    ptr+=2
                    x=x+dx;y=y+dy
                    curvecnt+=1
                    #print ">>\tm:x",x,"y",y,curvecnt
                    if curvecnt>1:
                        #path.lineTo(x,y)
                        self.lineTo(x,y)
                    else:
                        #path.moveTo(x,y)
                        self.moveTo(x,y)
                        x0=x;y0=y # subpath start
                elif state=='a':
                    rx = float(ss[ptr])
                    ry = float(ss[ptr+1])
                    phi = float(ss[ptr+2])
                    fA = int(ss[ptr+3])
                    fS = int(ss[ptr+4])
                    px = float(ss[ptr+5])+x # relative move
                    py = float(ss[ptr+6])+y
                    ptr+=7
                    arcSeg = buildArcSegment(rx,ry,phi,fA,fS,x,y,px,py)
                    for s in arcSeg:
                        self.lineTo(s[0],s[1])
                    x=px;y=py
                    
                elif state=='A':
                    rx = float(ss[ptr])
                    ry = float(ss[ptr+1])
                    phi = float(ss[ptr+2])
                    fA = int(ss[ptr+3])
                    fS = int(ss[ptr+4])
                    px = float(ss[ptr+5])+self.xbias
                    py = float(ss[ptr+6])+self.ybias
                    ptr+=7
                    arcSeg = buildArcSegment(rx,ry,phi,fA,fS,x,y,px,py)
                    for s in arcSeg:
                        self.lineTo(s[0],s[1])
                    x=px;y=py
                    
                elif state=="c":
                    dx=float(ss[ptr])
                    dy=float(ss[ptr+1])
                    pbuff.append((x+dx,y+dy))
                    ptr+=2
                    curvecnt+=1
                    #print ">>\tc:X",x,"Y",y,"x",dx,"y",dy,"cnt",curvecnt
                    if curvecnt==3:
                        bzseg = buildBezierSegment(pbuff[0],pbuff[1],pbuff[2],pbuff[3])
                        lastControl = pbuff[2]
                        for s in bzseg:
                            #path.lineTo(s[0],s[1])
                            self.lineTo(s[0],s[1])
                        x=x+dx;y=y+dy
                        pbuff=[(x,y)]
                        curvecnt = 0
                elif state=='C':
                    ax = float(ss[ptr])+self.xbias
                    ay = float(ss[ptr+1])+self.ybias
                    pbuff.append((ax,ay))
                    ptr+=2
                    curvecnt+=1
                    #print ">>\tC:x",ax,"y",ay,"cnt",curvecnt
                    if curvecnt==3:
                        bzseg = buildBezierSegment(pbuff[0],pbuff[1],pbuff[2],pbuff[3])
                        lastControl = pbuff[2]
                        for s in bzseg:
                            #path.lineTo(s[0],s[1])
                            self.lineTo(s[0],s[1])
                        pbuff=[(ax,ay)]
                        x=ax;y=ay
                        curvecnt = 0
                elif state=="s":
                    dx=float(ss[ptr])
                    dy=float(ss[ptr+1])
                    ptr+=2
                    curvecnt+=1
                    if curvecnt==1:
                        # set control point
                        if (prevstate=="S" or prevstate=="s" or prevstate=="C" or prevstate=="c"):
                            controlPoint = (2*pbuff[0][0]-lastControl[0],2*pbuff[0][1]-lastControl[1])
                            pbuff.append(controlPoint)
                            pbuff.append((x+dx,y+dy))
                        else:
                            pbuff.append(pbuff[0]) # if prev state not bez-curve, use current point as first control point
                            pbuff.append((x+dx,y+dy))
                            
                    if curvecnt==2:
                        # set target point
                        pbuff.append((x+dx,y+dy))
                        bzseg = buildBezierSegment(pbuff[0],pbuff[1],pbuff[2],pbuff[3])
                        lastControl = pbuff[2]
                        for s in bzseg:
                            #path.lineTo(s[0],s[1])
                            self.lineTo(s[0],s[1])
                        x=x+dx;y=y+dy
                        pbuff=[(x,y)]
                        curvecnt = 0
                elif state=="S":
                    ax = float(ss[ptr])+self.xbias
                    ay = float(ss[ptr+1])+self.ybias
                    ptr+=2
                    curvecnt+=1
                    if curvecnt==1:
                        # set control point
                        if (prevstate=="S" or prevstate=="s" or prevstate=="C" or prevstate=="c"):
                            controlPoint = (2*pbuff[0][0]-lastControl[0],2*pbuff[0][1]-lastControl[1])
                            pbuff.append(controlPoint)
                            pbuff.append((ax,ay))
                        else:
                            pbuff.append(pbuff[0]) # if prev state not bez-curve, use current point as first control point
                            pbuff.append((ax,ay))
                    if curvecnt==2:
                        # set target point
                        pbuff.append((ax,ay))
                        bzseg = buildBezierSegment(pbuff[0],pbuff[1],pbuff[2],pbuff[3])
                        lastControl = pbuff[2]
                        for s in bzseg:
                            #path.lineTo(s[0],s[1])
                            self.lineTo(s[0],s[1])
                        x=ax;y=ay
                        pbuff=[(x,y)]
                        curvecnt = 0
                    
                    
                elif state=="l":
                    dx=float(ss[ptr])
                    dy=float(ss[ptr+1])
                    ptr+=2
                    curvecnt+=1
                    x=x+dx;y=y+dy
                    #print ">>\tl:x",x,"y",y,"cnt",curvecnt
                    #path.lineTo(x,y)
                    self.lineTo(x,y)
                elif state=="L":
                    ax=float(ss[ptr])+self.xbias
                    ay=float(ss[ptr+1])+self.ybias
                    ptr+=2
                    curvecnt+=1
                    #print ">>\tL:x",ax,"y",ay,"cnt",curvecnt
                    x=ax;y=ay
                    #path.lineTo(ax,ay)
                    self.lineTo(ax,ay)
                else:
                    ptr+=1
                    print "unknow state",state
        return
        
    def parseRect(self,node):
        w = float(node.getAttribute("width"))+self.xbias
        h = float(node.getAttribute("height"))+self.xbias
        x = float(node.getAttribute("x"))+self.ybias
        y = float(node.getAttribute("y"))+self.ybias
        print ">> Rect",w,h,x,y
        self.moveTo(x,y)
        self.lineTo(x+w,y)
        self.lineTo(x+w,y+h)
        self.lineTo(x,y+h)
        self.lineTo(x,y)
        return
    
    def parseLine(self,node):
        x1 = float(node.getAttribute("x1"))+self.xbias
        x2 = float(node.getAttribute("x2"))+self.xbias
        y1 = float(node.getAttribute("y1"))+self.ybias
        y2 = float(node.getAttribute("y2"))+self.ybias
        print ">> Line",x1,y1,x2,y2
        #path = QtGui.QPainterPath()
        #path.moveTo(x1,y1)
        self.moveTo(x1,y1)
        #path.lineTo(x2,y2)
        self.lineTo(x2,y2)
        #self.scene.addPath(path)

        #self.pathList.append([(x1,y1),(x2,y2)])

        return
    
    def parsePolygon(self,node):
        tmp = []
        pstr = node.getAttribute("points")
        points = pstr.split(" ")
        print ">> polygon:"
        isinit=0
        #path = QtGui.QPainterPath()
        initx=0
        inity=0
        for p in points:
            if len(p)==0: continue
            xstr,ystr = p.split(',')
            print ">>\t",xstr,ystr
            x=float(xstr)+self.xbias
            y=float(ystr)+self.ybias
            tmp.append((x,y))
            if isinit==0:
                #path.moveTo(x,y)
                self.moveTo(x,y)
                initx=x
                inity=y
                isinit=1
            else:
                ""
                #path.lineTo(x,y)
                self.lineTo(x,y)
        #path.lineTo(x,y)
        self.lineTo(x,y)
        #self.scene.addPath(path)
        
        #self.pathList.append(tmp)
        return
    
    def parsePolyline(self,node):
        tmp = []
        pstr = node.getAttribute("points")
        points = pstr.split(" ")
        print ">> polyline:"
        isinit=0
        #path = QtGui.QPainterPath()
        #pen(0)
        for p in points:
            if len(p)==0: continue
            xstr,ystr = p.split(',')
            print ">>\t",xstr,ystr
            x=float(xstr)+self.xbias
            y=float(ystr)+self.ybias
            tmp.append((x,y))
            if isinit==0:
                #path.moveTo(x,y)
                self.moveTo(x,y)
                isinit=1
            else:
                #path.lineTo(x,y)
                self.lineTo(x,y)
        #self.scene.addPath(path)
        #self.pathList.append(tmp)
        return
    
    def parseCircle(self,node):
        cx = float(node.getAttribute("cx"))
        cy = float(node.getAttribute("cy"))
        r = float(node.getAttribute("r"))
        
        # move to start point of circle
        theta = 0
        px = r*cos(theta)+cx
        py = r*sin(theta)+cy
        self.moveTo(px, py)
        for i in range(1,100):
            ratio = float(i)/100
            theta = ratio*2*pi
            x = r*cos(theta)+cx
            y = r*sin(theta)+cy
            dx=x-px;dy=y-py;
            dis = sqrt(dx*dx+dy*dy)
            if dis>1:
                self.lineTo(x, y)
                px=x;py=y;
    
    def parseTextNode(self,n):
        # parse transform tag
        sib = n.nextSibling
        if sib == None:
            return None
        attrs = sib._attrs
        if "transform" in attrs:
            print "trans",attrs
            tf = [1,0,0,1,0,0]
            trans = attrs["transform"].value.split()
            for t in trans:
                if "scale" in t:
                    p0 = t.find('(')
                    tmp = map(float,t[p0+1:-1].split(","))
                    tf[0] = tmp[0]
                    tf[3] = tmp[1]
                    self.tf.append(tf)
                elif "translate" in t:
                    p0 = t.find('(')
                    tmp = map(float,t[p0+1:-1].split(","))
                    tf[4] = tmp[0]
                    tf[5] = tmp[1]
                    self.tf.append(tf)
                elif "matrix" in t:
                    p0 = t.find('(')
                    tmp = map(float,t[p0+1:-1].split(","))
                    tf = tmp
                    self.tf.append(tf)
            return tf
        return None
    
    def parseTransform(self,node):
        tfAttr = node.getAttribute("transform")
        if tfAttr != "":
            #print "trans",tfAttr
            trans = tfAttr.split()
            tf=[1,0,0,1,0,0]
            for t in trans:
                if "scale" in t:
                    p0 = t.find('(')
                    tmp = map(float,t[p0+1:-1].split(","))
                    tf[0] = tmp[0]
                    tf[3] = tmp[1]
                elif "translate" in t:
                    p0 = t.find('(')
                    tmp = map(float,t[p0+1:-1].split(","))
                    tf[4] = tmp[0]
                    tf[5] = tmp[1]
                elif "matrix" in t:
                    p0 = t.find('(')
                    tmp = map(float,t[p0+1:-1].split(","))
                    tf = tmp
            self.tf.append(tf)
            return trans
        else:
            return None
        
    def parseNode(self,node,deep):
        print " "*deep,">>",node.nodeName,node.nodeType
        tf = None
        if node.nodeType==1:
            tf = self.parseTransform(node)
        if node.nodeName=="path":
            self.parsePath(node)
        elif node.nodeName=="rect":
            self.parseRect(node)
        elif node.nodeName=="line":
            self.parseLine(node)
        elif node.nodeName=="polygon":
            self.parsePolygon(node)
        elif node.nodeName=="polyline":
            self.parsePolyline(node)
        elif node.nodeName=="circle":
            self.parseCircle(node)
        else:
            print " "*deep,"unknow",node.nodeName
        return tf
    
    def parseChildNodes(self,node,deep=1):
        print " "*deep,"parse->",node.nodeName
        # escape marker
        if node.nodeName == "marker" or node.nodeName == "clipPath":
            return
        for n in node.childNodes:
            if len(n.childNodes)>0:
                tf = self.parseNode(n,deep)
                self.parseChildNodes(n,deep+1)
                if tf!=None:
                    self.tf.pop()
            else:
                tf = self.parseNode(n,deep)
                if tf!=None:
                    self.tf.pop()
            
    def parse(self,filename):
        dom = minidom.parse(filename)
        root = dom.documentElement
        self.parseChildNodes(root)

if __name__ == '__main__':
    buildArcSegment(10,10,0,0,10,10,0)
    
    
