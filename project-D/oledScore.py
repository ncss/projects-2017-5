from microbit import *
import ustruct
import radio

radio.on()
radio.config(channel=6, address= 0x12341234)

def color565(r, g, b):
  return (r & 0xf8) << 8 | (g & 0xfc) << 3 | b >> 3

class Display:
  _INIT = (
    (0xFD, b'\x12'), (0xFD, b'\xb1'), (0xAE, b''), (0xB2, b'\xa4\x00\x00'), (0xB3, b'\xf0'), (0xCA, b'\x7f'), (0xA0, b'\x74'), (0xA1, b'\x00'), (0xA2, b'\x00'), (0xB5, b'\x00'), (0xAB, b'\x01'), (0xB1, b'\x32'), (0xBB, b'\x1f'), (0xBE, b'\x05'), (0xA6, b''), (0xC1, b'\xc8\x80\xc8'), (0xC7, b'\x0a'), (0xB4, b'\xa0\xb5\x55'), (0xB6, b'\x01'), (0xAF, b''),
  )

  def __init__(self):
    spi.init(baudrate=2000000)
    pin0.write_digital(1) # cs
    pin1.write_digital(0) # dc
    pin2.write_digital(0) # rst

    self.reset()

    for command, data in self._INIT:
      self._write(command, data)

  def _block(self, x0, y0, x1, y1, data=None):
    self._write(0x15, self._encode_pos(x0, x1))
    self._write(0x75, self._encode_pos(y0, y1))
    if data is None:
      size = ustruct.calcsize(">BBB")
      return self._read(0x5D, (x1 - x0 + 1) * (y1 - y0 + 1) * size)
    self._write(0x5C, data)

  def _encode_pos(self, a, b):
    return ustruct.pack(">BB", a, b)

  def _encode_pixel(self, color):
    return ustruct.pack(">H", color)

  def _decode_pixel(self, data):
    return color565(*ustruct.unpack(">BBB", data))

  def pixel(self, x, y, color=None):
    if color is None:
      return self._decode_pixel(self._block(x, y, x, y))
    if not 0 <= x < 128 or not 0 <= y < 128:
      return
    self._block(x, y, x, y, self._encode_pixel(color))

  def fill_rectangle(self, x, y, w, h, color):
    x = min(128 - 1, max(0, x))
    y = min(128 - 1, max(0, y))
    w = min(128 - x, max(1, w))
    h = min(128 - y, max(1, h))
    self._block(x, y, x + w - 1, y + h - 1, b'')
    chunks, rest = divmod(w * h, 512)
    pixel = self._encode_pixel(color)
    if chunks:
      data = pixel * 32
      for i in range(16):
        for count in range(chunks):
          self._write(None, data)
    self._write(None, pixel * rest)

  def fill(self, color=0):
    self.fill_rectangle(0, 0, 128, 128, color)

  def reset(self):
    pin2.write_digital(0)
    sleep(50)
    pin2.write_digital(1)
    sleep(50)

  def _write(self, command=None, data=None):
    if command is not None:
      pin1.write_digital(0)
      pin0.write_digital(0)
      spi.write(bytearray([command]))
      pin0.write_digital(1)
    if data is not None:
      pin1.write_digital(1)
      pin0.write_digital(0)
      spi.write(data)
      pin0.write_digital(1)

  def _read(self, command=None, count=0):
    pin1.write_digital(0)
    pin0.write_digital(0)
    if command is not None:
      spi.write(bytearray([command]))
    if count:
      data = spi.read(count)
    pin0.write_digital(1)
    return data
    
  def display_number(self, number, x, y, c, s):
      img = Image(str(number))
      for xx in range(5):
          for yy in range(5):
              p = c if img.get_pixel(xx, yy) == 9 else 0
              self.fill_rectangle(x + xx*s, y + yy*s, s, s, p)

d = Display()

while True:
    d.fill()
    #try:
    #    score = radio.receive()
    #except ValueError:
    #    radio.receive_bytes()
    #if score is None:
    #    continue
    sleep(2)
    digits = [int(d) for d in str(score)]
    d.display_number(digits[2], 85, 50, color565(255, 0, 0), 7)
    d.display_number(digits[1], 45, 50, color565(255, 0, 0), 7)
    d.display_number(digits[0], 5, 50, color565(255, 0, 0), 7)
    sleep(500)

