import serial
import time

"""
    Used to flash an arduino firmware (in hex file format) to the board
    @author: Wang Yu (bigeyex@gmail.com) 
"""
class UnoProgrammer(object):
    
    # Constants involved in Uno Bootloader protocol.
    STK_OK = 0x10
    STK_FAILED = 0x11
    STK_UNKONWN = 0x12
    STK_INSYNC = 0x14
    STK_NOSYNC = 0x15
    STK_GET_SYNCH = 0x30
    STK_ENTER_PROGMODE = 0x50
    STK_READ_SIGN = 0x75
    SYNC_CRC_EOP = 0x20
    STK_LOAD_ADDRESS = 0x55
    STK_PROGRAM_PAGE = 0x64
    STK_PROGRAM_FLASH = 0x46
    STK_LEAVE_PROGMODE = 0x51
    
    # Commands for Uno Bootloader
    CMD_HANDSHAKE = [STK_GET_SYNCH, SYNC_CRC_EOP]
    CMD_ENTER_PROG_MODE = [STK_ENTER_PROGMODE, SYNC_CRC_EOP]
    CMD_LEAVE_PROG_MODE = [STK_LEAVE_PROGMODE, SYNC_CRC_EOP]
    RES_OK = [STK_INSYNC, STK_OK]
    
    # Common ISP Parameters
    CONFIG_CHUNKSIZE = 128
    CONFIG_PAGESTEP = 64
    
    def __init__(self, serialName, signal, hexFileName):
        self.sig = signal
        self.serialName = serialName
        self.data = self.loadHexData(hexFileName)
        pass
    
    def downloadThread(self):
        pageIndex = 0
        with serial.Serial(self.serialName, timeout=5, baudrate=115200, dsrdtr=True) as self.serial:
            self.sig.emit("download start")
            # 0. reset IO
            self.serial.setDTR(True)
            time.sleep(0.1)
            self.serial.setDTR(False)
            time.sleep(0.1)
            self.serial.setDTR(True)
            time.sleep(0.3)
            
            # 1. handshake
            self.log("ISP: handshake")
            self.sendBytes(self.CMD_HANDSHAKE)
            if not self.expectBytes(self.RES_OK):
                return
            # 2. enter programming mode
            self.log("ISP: enter programming mode")
            self.sendBytes(self.CMD_ENTER_PROG_MODE)
            if not self.expectBytes(self.RES_OK):
                return
            # 3. alternatively send address and data chunks
            dataLength = len(self.data)
            self.log("ISP: writing firmware total %d bytes" % dataLength)
            while pageIndex*self.CONFIG_CHUNKSIZE < dataLength:
                # send address
                codeAddress = pageIndex * self.CONFIG_PAGESTEP
                lowAddress = codeAddress & 0xFF
                highAddress = codeAddress >> 8
                self.sendBytes([self.STK_LOAD_ADDRESS, lowAddress, highAddress, self.SYNC_CRC_EOP])
                if not self.expectBytes(self.RES_OK):
                    return
                
                # send data
                chunkSize = self.CONFIG_CHUNKSIZE
                if (pageIndex+1)*chunkSize > dataLength:
                    chunkSize = dataLength - pageIndex*self.CONFIG_CHUNKSIZE
                lowChunkSize = chunkSize & 0xFF
                highChunkSize = chunkSize >> 8
                self.sendBytes([self.STK_PROGRAM_PAGE, highChunkSize, lowChunkSize, self.STK_PROGRAM_FLASH] +
                               self.data[pageIndex*self.CONFIG_CHUNKSIZE : pageIndex*self.CONFIG_CHUNKSIZE+chunkSize] +
                               [self.SYNC_CRC_EOP]) 
                if not self.expectBytes(self.RES_OK):
                    return
                
                pageIndex = pageIndex + 1
                self.announceProgress(pageIndex*self.CONFIG_CHUNKSIZE *100/ dataLength)
                
            # 4. Leave programming mode
            self.sendBytes(self.CMD_LEAVE_PROG_MODE)
            if not self.expectBytes(self.RES_OK):
                return
            self.announceSuccess()
    
    def log(self, content):
        # for debug use only
        # print(content)
        pass
        
    def announceProgress(self, percentage):
        self.sig.emit("downpg %d" %(percentage))
        
    def announceSuccess(self):
        self.sig.emit("download finished")
        self.log("ISP: success")
        
    def announceFailed(self):
        self.sig.emit("download failed")
        self.log("ISP: failed")
        
    def sendBytes(self, byteContent):
        self.log("writing: %d bytes" % len(byteContent))
        self.log(''.join('{:02x}'.format(x) for x in byteContent))
#         self.serial.write(''.join([chr(x) for x in byteContent]))
        self.serial.write(bytes(byteContent))
        
    def expectBytes(self, content):
        result = self.serial.read(len(content))
        self.log("reading %d bytes %s and expect %s" % (len(result), self.formatBytes(result), self.formatBytes(content)))
        if bytes(result) != bytes(content):
            self.announceFailed()
            return False
        return True
    
    # typical format of the hex file:
    # :1003B000F0E0EE0FFF1FEC55FF4FA591B4919FB7F2
    # [':'][lengthOfData:2][address:8][data:...][CRC:2]
    def loadHexData(self, hexFileName):
        data = []
        lineNumber = 1
        with open(hexFileName, 'r') as f:
            for line in f:
                dataLength = self.hexStringToBytes(line[1:3])[0]
                data = data + self.hexStringToBytes(line[9:9+2*dataLength])
                # print("data length: %d(+%d) %d: %s", (len(data), dataLength, lineNumber, line))
                lineNumber = lineNumber + 1
        return data
                
    def hexStringToBytes(self, hexString):
        index = 0
        value = 0
        result = []
        for ch in hexString:
            value = value + self.hexToByte(ch)
            if index % 2 == 0:          # higher byte of twin bytes
                value = value * 16
            else:                       # lower byte
                result.append(value)
                value = 0
            index = index + 1
        return result
    
    def formatBytes(self, value):
        return ''.join('{:02x}'.format(x) for x in value)
    
    def hexToByte(self, hexString):
        if hexString > "9":                 # "A" ~ "F"
            return ord(hexString)-65+10     # "A" -> 0x0a
        else:
            return ord(hexString)-48        # "2" -> 0x02