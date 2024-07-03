import os

if not os.stat('LICENSE.txt').st_size:
    os.unlink('LICENSE.txt')
