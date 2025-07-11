from r import R
from math import sqrt

def treemap(box, inp):
    items = []
    S = box.area
    A = sum(inp)
    W, H = box.w, box.h
    cur = None
    cur_items = []
    for v in inp:
        while True:
            if cur is None:
                if box.w > box.h:
                    w_2 = sqrt(v / A * S)
                    cur = R(box.x, box.y, w_2, box.h, 1)
                else:
                    h_2 = sqrt(v / A * S)
                    cur = R(box.x, box.y, box.w, h_2, -1)

            if cur.v > 0:
                w = cur.w
                h = v / A * S / w
            else:
                h = cur.h
                w = v / A * S / h

            r = R(0.0, 0.0, w, h, v)
            a = sum([i.area for i in cur_items])
            q = sum([i.v for i in cur_items])
            if cur_items and a + r.area > cur.area:
                if cur.v > 0:
                    w = q / A * S / cur.h
                    y = cur.y
                    for i in cur_items:
                        h = i.v / A * S / w
                        n = R(cur.x, cur.y, w, h, i.v)
                        cur.y += h
                        items.append(n)

                    x = cur.x + w
                    if x >= W:
                        x = 0
                        w = W
                        y = cur.y
                        h = H - y
                    else:
                        w = W - x
                        h = H - y
                else:
                    h = q / A * S / cur.w
                    x = cur.x
                    for i in cur_items:
                        w = i.v / A * S / h
                        n = R(cur.x, cur.y, w, h, i.v)
                        cur.x += w
                        items.append(n)

                    y = cur.y + h
                    if y >= H:
                        y = 0.0
                        h = H
                        x = cur.x
                        w = W - x
                    else:
                        h = H - y
                        w = W - x

                cur_items = []
                box = R(x, y, w, h)
                cur = None
                continue
            else:
                cur_items.append(r)
                break

    cur = R(box.x, box.y, W - box.x, H - box.y)
    q = sum([i.v for i in cur_items])
    if box.w > box.h:
        w = q / A * S / cur.h
        for i in cur_items:
            h = i.v / A * S / w
            r = R(cur.x, cur.y, w, h, i.v)
            cur.y += h
            items.append(r)
    else:
        h = q / A * S / cur.w
        for i in cur_items:
            w = i.v / A * S / h
            r = R(cur.x, cur.y, w, h, i.v)
            cur.x += w
            items.append(r)
    return items

