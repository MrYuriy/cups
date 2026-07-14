
empty_label = '''
^XA
^FO0,0^GB0,0,0^FS
^FO30,30^A0N,0,0^FD^FS
^XZ
'''

def get_one_label(sku, barcod, x_set, y_set) -> str:
    x_sku, x_barcod, x_ean = x_set
    y_sku, y_barcod, y_ean = y_set

    label_code = (f''' 
    ^FO{x_sku},{y_sku} 
    ^ABB,30,20
    ^FD{sku}^FS

    ^FO {x_barcod},{y_barcod}
    ^BY2
    ^BEB,80,N,N,N
    ^FD{barcod[:-1]}^FS 

    ^FO{x_ean},{y_ean}
    ^ABB,25,15
    ^FD{barcod}^FS
    
    '''
    )
    return label_code


def gen_one_row(sku, barcod) -> str:
    first_label = get_one_label(sku=sku, barcod=barcod, x_set=(20,70,180), y_set=(40,50,40))
    midle_label = get_one_label(sku=sku, barcod=barcod, x_set=(320,370,480), y_set=(40,50,40))
    last_label = get_one_label(sku=sku, barcod=barcod, x_set=(570,620,730), y_set=(40,50,40))
    row_code = f"^XA{first_label} {midle_label} {last_label}^XZ"
    return row_code

def gen_labels(sku, barcod, qty):
    label_code = ""
    row_qty = int(-1 * (qty/3) // 1 * -1)
    for _ in range(row_qty):
        label_code += gen_one_row(sku=sku, barcod=barcod)
    return label_code + empty_label
