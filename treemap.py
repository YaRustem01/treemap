from r import R
from math import sqrt


def treemap(box, inp):
    items = []
    S = box.area
    A = sum(inp)
    X1, Y1, X2, Y2 = box.x, box.y, box.x + box.w, box.y + box.h
    cur = None
    cur_items = []
    for v in inp:
        while True:
            cur_area = v / A * S
            if cur is None:
                if box.w > box.h:
                    w_2 = sqrt(cur_area)
                    cur = R(box.x, box.y, w_2, box.h, 1)
                else:
                    h_2 = sqrt(cur_area)
                    cur = R(box.x, box.y, box.w, h_2, -1)

            if cur.v > 0:
                w = cur.w
                h = cur_area / w
            else:
                h = cur.h
                w = cur_area / h

            r = R(0.0, 0.0, w, h, v)
            a = sum([i.area for i in cur_items])
            q = sum([i.v for i in cur_items])
            if cur_items and a + r.area > cur.area:
                first = cur_items[0]
                vbox = None
                if cur.v > 0:

                    w = q / A * S / cur.h
                    h = first.v / A * S / w

                    first.x, first.y, first.w, first.h = cur.x, cur.y, w, h

                    if len(cur_items) > 1:
                        vbox = R(cur.x, cur.y + h, w, cur.h - h, 1)

                    x = cur.x + w
                    y = cur.y
                    if x >= X2:
                        x = X1
                        y += cur.h

                    w = X2 - x
                    h = Y2 - y

                    box = R(x, y, w, h, 1)
                else:
                    h = q / A * S / cur.w
                    w = first.v / A * S / h

                    first.x, first.y, first.w, first.h = cur.x, cur.y, w, h

                    if len(cur_items) > 1:
                        vbox = R(cur.x + w, cur.y, cur.w - w, h, -1)

                    x = cur.x
                    y = cur.y + h
                    if y >= Y2:
                        x += cur.w
                        y = Y1

                    w = X2 - x
                    h = Y2 - y

                    box = R(x, y, w, h, -1)

                items.append(first)
                if vbox:
                    items.extend(treemap(vbox, list(map(lambda x: x.v, cur_items[1:]))))

                cur_items = []
                cur = None
                continue
            else:
                cur_items.append(r)
                break

    cur = R(box.x, box.y, X2 - box.x, Y2 - box.y)
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
