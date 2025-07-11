import math
import random

from treemap import treemap
from draw import draw, draw_vor
from r import R

if __name__ == "__main__":
    box = R(0.0, 0.0, 6.0, 4.0)
    vbox = (box.w+1, box.h+1)

    #random.seed(7)
    inp = [random.randint(1, 600) for i in range(10)]
    #inp = [int(math.fabs(random.gauss(10, 10))) for i in range(10)]
    #inp = (8.,6.,6.,4.,3.,2.,1.)
    #inp = (1,2,3,4,5,6,7,8,9,0)
    inp = sorted(filter(lambda x: x > 0, inp), reverse=True)
    print(inp)
    
    items = treemap(box, inp)
    # draw(vbox, items)
    draw_vor(vbox,items)
