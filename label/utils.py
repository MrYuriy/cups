
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
            f"^XA"
            f"^FO44,104^FB740,2,15,L,0^ATN,44,44^FD Dostawca:  {label_inst.supplier_company}^FS"
            f"^FO27,300^AUN,74,74^FD USER: {label_inst.user}^FS"
            f"^FO27,400^AUN,74,74^FD DATA: {label_inst.data}^FS"
            f"^FO27,500^AUN,74,74^FD Master: {label_inst.master_id}^FS"
            f"^FO44,650^FB740,3,10,L,0^CI28^ATN,100,100^FD{label_inst.comment}^FS"
            f"^FO27,800^AUN,74,74^FD Order: {label_inst.pre_advice}^FS"
            f"^FO27,900^AUN,74,74^FD SKU: {label_inst.sku}^FS"
            f"^FO44,1000^FB1036,2,15,L,0^ATN,44,44^FD Deskription: {label_inst.deskription}^FS"
            f"^FO860,133^BY5^BCB,177,N,N,N^FD{label_inst.identifier}^FS"
            f"^FO1036,177^ASB,133,104^FD {label_inst.identifier}^XZ"
        )
        labels_list.append(label_code)
    return labels_list
