import time
    self.lastPos = self.pos
    self.lastSum = (self.pinA.value() << 1) | self.pinB.value()
      var = round(self.pos / 4)
      if (((self.pos - self.originalPos) % 4) == 0) and (var != round(self.lastPos / 4)):
        currentTime = time.ticks_us()
        self.passTime = currentTime - self.lastTime
        self.lastTime = currentTime
        self.lastPos = self.pos
        if self.cbCoderStatus == 1:
          dict = {"pos" : 0, "time" : 0}
          dict["pos"] = var
          dict["time"] = self.passTime
          self.cbCoder(dict)
    varTime = self.passTime
    self.passTime = 0
    dict["pos"] = round(self.pos / 4)
    dict["time"] = varTime
    self.lastPos = self.pos