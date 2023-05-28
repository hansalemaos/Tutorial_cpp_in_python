import ctypes
import sys
import numpy as np

def change_unchangeable(v, new):
    # tuple value to buffer
    buff = (ctypes.c_uint8 * (sys.getsizeof(v))).from_address(id(v))
    ax = np.frombuffer(buff, dtype=np.uint8)

    # new value to buffer
    buff2 = (ctypes.c_uint8 * (sys.getsizeof(new))).from_address(id(new))
    ax2 = np.frombuffer(buff2, dtype=np.uint8)

    # copying each byte from one buffer to the other one.
    for i in range(len(ax2)):
        try:
            ax[i] = ax2[i]
        except Exception:
            return False
    return True

tu = (22,3,4,5,6)
print(f'{id(tu)}')
newvar=4
change_unchangeable(v=tu[0], new=newvar)
print(f'{id(tu)}')
