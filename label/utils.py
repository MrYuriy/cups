
def generate_label(label_ins):
    labels_list = []
    for label_inst in label_ins:
        label_code = (
            f"^XA^FO 30,70^FB500,2,10,L,0^ATN,30,30^FD Dostawca:  {label_inst.supplier_company}^FS"
            f"^FO 18,170 ^ATN,30,30^FD Sklep: {label_inst.shop}^FS"
            f"^FO 18,240 ^AUN,50,50^FD USER: {label_inst.user}^FS"
            f"^FO 18,320 ^AUN,50,50^FD DATA: {label_inst.data}^FS"
            f"^FO 18,400 ^AUN,50,50^FD Order: {label_inst.order} ^FS"
            f"^FO 30,500^FB500,3,10,L,0^CI28^ATN,100,100^FD{label_inst.comment}^FS"
            f"^FO 580,90^BY3^BCB,120,N,N,N^FD{label_inst.identifier}^FS"
            f"^FO700,120 ^ASB,90,70 ^FD {label_inst.identifier}^XZ"
        )
        labels_list.append(label_code)
    return(labels_list)

def generate_label_stock(label_ins):
    labels_list = []
    for label_inst in label_ins:
        label_code = (
            f"^XA^MUd^FO 30,70^FB500,2,10,L,0^ATN,30,30^FD Dostawca:  {label_inst.supplier_company}^FS"
            f"^FO 18,240 ^AUN,50,50^FD USER: {label_inst.user}^FS"
            f"^FO 18,320 ^AUN,50,50^FD DATA: {label_inst.data}^FS"
            f"^FO 18,400 ^AUN,50,50^FD Master :: {label_inst.master_id} ^FS"
            f"^FO 30,500^FB500,3,10,L,0^CI28^ATN,100,100^FD{label_inst.comment}^FS"
            f"^FO 18,600 ^AUN,50,50^FD Order: {label_inst.pre_advice}^FS"
            f"^FO 18,700 ^AUN,50,50^FD SKU:  {label_inst.sku}^FS"
            f"^FO 30,800^FB700,2,10,L,0^ATN,30,30^FD Deskription: {label_inst.deskription}^FS"
            f"^FO 580,90^BY3^BCB,120,N,N,N^FD{label_inst.identifier}^FS"
            f"^FO700,120 ^ASB,90,70 ^FD {label_inst.identifier}^XZ"
        )
        labels_list.append(label_code)
    return(labels_list)
