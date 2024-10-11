
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


def gen_line_info(lines_info):
    y_gen = 650
    lines_code = ""
    for line in lines_info:
        line_part_of_label = (
            f"^FO44,{y_gen}^FB1000,3,10,L,0^CI28^ATN,100,100^FD {line['label_title']}^FS"
            f"^FO44,{y_gen + 100}^FB900,2,15,L,0^ATN,44,44^FD {line['line_info']} ^FS"
        )
        y_gen += 200
        lines_code += line_part_of_label
    return lines_code    


def generate_label_stock(label_ins):
    labels_list = []
    for label_inst in label_ins:
        line_info = [
            (line["label_title"], line["line_info"]) 
            for line in label_inst.lines_info
        ]
        print(line_info)
        label_code = (
            f"^XA"
            f"^FO950,200^BQN,2,10,3^FDMA,{label_inst.identifier}^FS"
            f"^FO686,80^ATN,80,80^FD {label_inst.identifier}^FS"

            f"^FO44,104^FB740,2,15,L,0^ATN,60,60^FD Dostawca: {label_inst.supplier_company}^FS"
            f"^FO27,200^AUN,74,74^FD {label_inst.user}^FS"
            f"^FO27,300^AUN,74,74^FD DATA:  {label_inst.data}^FS"

            f"^FO600,300^FB740,3,10,L,0^CI28^ATN,150,150^FD {label_inst.delivery_part}^FS"

            f"^FO27,400^AUN,74,74^FD Pre-Advice: {label_inst.pre_advice}^FS"
            f"^FO27,500^AUN,74,74^FD Master: {label_inst.master_id}^FS"

            f"{gen_line_info(label_inst.lines_info)}"

            f"^XZ"
        )
        labels_list.append(label_code)
    return labels_list
