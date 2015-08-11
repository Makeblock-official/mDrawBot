/**
 * Created by Riven on 2015-08-03.
 */

/* assume all msg on serial is based on gcode protocol */
var SerialConnection = function() {
    this.connectionId = -1;
    this.lineBuffer = "";
    this.boundOnReceive = this.onReceive.bind(this);
    this.boundOnReceiveError = this.onReceiveError.bind(this);
    this.onReadLine = new chrome.Event();
};

/* Interprets an ArrayBuffer as UTF-8 encoded string data. */
var ab2str = function(buf) {
    var bufView = new Uint8Array(buf);
    var encodedString = String.fromCharCode.apply(null, bufView);
    return decodeURIComponent(escape(encodedString));
};

/* Converts a string to UTF-8 encoding in a Uint8Array; returns the array buffer. */
var str2ab = function(str) {
    var encodedString = unescape(encodeURIComponent(str));
    var bytes = new Uint8Array(encodedString.length);
    for (var i = 0; i < encodedString.length; ++i) {
        bytes[i] = encodedString.charCodeAt(i);
    }
    return bytes.buffer;
};

SerialConnection.prototype.getDevices = function(callback) {
    chrome.serial.getDevices(callback);
};

SerialConnection.prototype.onReceive = function(receiveInfo) {
    if (receiveInfo.connectionId !== this.connectionId) {
        return;
    }
    //console.log("buf "+receiveInfo.data.byteLength+">>"+ab2str(receiveInfo.data));
    this.lineBuffer += ab2str(receiveInfo.data);
    var index;
    while ((index = this.lineBuffer.indexOf('\n')) >= 0) {
        var line = this.lineBuffer.substr(0, index + 1);
        this.onReadLine.dispatch(line);
        this.lineBuffer = this.lineBuffer.substr(index + 1);
    }

};

SerialConnection.prototype.onReceiveError = function(errorInfo) {
    if (errorInfo.connectionId === this.connectionId) {
        console.log("on receive error "+errorInfo);
    }
};

SerialConnection.prototype.onConnect = function(callback,connectionInfo){
    if (!connectionInfo) {
        console.log("Connection failed.");
        return;
    }
    this.connectionId = connectionInfo.connectionId;

    chrome.serial.onReceive.addListener(this.boundOnReceive);
    chrome.serial.onReceiveError.addListener(this.boundOnReceiveError);
    this.lineBuffer = "";
    if (callback) callback(connectionInfo);
};

SerialConnection.prototype.onClosed = function(callback,result){
    //console.log("serial disconnect "+result);
    this.connectionId = -1;
    // remove listeners
    chrome.serial.onReceive.removeListener(this.boundOnReceive);
    chrome.serial.onReceiveError.removeListener(this.boundOnReceiveError);
    if (callback) callback();
};

SerialConnection.prototype.connect = function(path, option, callback) {
    chrome.serial.connect(path, option, this.onConnect.bind(this, callback));
};

SerialConnection.prototype.disconnect = function(callback){
    if(this.connectionId==-1) return;
    chrome.serial.disconnect(this.connectionId, this.onClosed.bind(this,callback));
};

SerialConnection.prototype.send = function(msg){
    if(this.connectionId==-1) return;
    console.log("send "+msg);
    chrome.serial.send(this.connectionId, str2ab(msg), function() {});
};