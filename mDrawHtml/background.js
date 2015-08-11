/**
 * Created by Riven on 2015-08-01.
 */

chrome.app.runtime.onLaunched.addListener(function(){
    chrome.app.window.create("main.html",{
        'innerBounds':{
            'width':959,
            'height':720,
            'minWidth':959,
            'minHeight':720,
            'maxWidth':959,
            'maxHeight':720,
            'left':100,
            'top':100
        }
    });
});