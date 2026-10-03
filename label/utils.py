
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
            f"^FO44,{y_gen + 100}^FB1000,2,15,L,0^ATN,44,44^FD {line['line_info'][:90]} ^FS"
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


# ---- returned orders: 10x10 cm at 203 dpi ----
RETURN_LABEL_DOTS = 800
RETURN_ROWS_PER_LABEL = 10
RETURN_ROW_HEIGHT = 44
RETURN_FIRST_ROW_Y = 310
RETURN_KIND_TITLES = {"intact": "PEŁNOWARTOŚCIOWE", "damaged": "USZKODZONE"}


def _return_label(kind, page, pages, data, oh_number, rows):
    """One 10x10 cm sheet: header, the kind of goods, and up to ten reference/quantity rows."""
    side = RETURN_LABEL_DOTS
    parts = [
        "^XA",
        "^CI28",  # UTF-8, so Polish letters print
        f"^PW{side}^LL{side}^LH0,0",
        f"^FO12,12^GB{side - 24},{side - 24},3^FS",
        # Which sheet of the set this is, so a missing one is noticed even when there is only one.
        f"^FO30,28^A0N,40,40^FD{page}/{pages}^FS",
        "^FO30,80^A0N,34,34^FDDATA^FS",
        f"^FO30,118^A0N,52,52^FD{data}^FS",
        "^FO430,80^A0N,34,34^FDNR OH^FS",
        f"^FO430,112^A0N,60,60^FD{oh_number}^FS",
        # The kind of goods is the first thing to see: white on a black bar.
        f"^FO12,190^GB{side - 24},62,62^FS",
        f"^FO36,202^A0N,44,44^FR^FD{RETURN_KIND_TITLES.get(kind, kind)}^FS",
        "^FO30,264^A0N,30,30^FDREFERENCJA^FS",
        "^FO520,264^A0N,30,30^FDILOŚĆ^FS",
        f"^FO30,296^GB{side - 60},2,2^FS",
    ]
    y = RETURN_FIRST_ROW_Y
    for line in rows:
        parts.append(f"^FO36,{y}^A0N,40,40^FD{line.get('reference', '')}^FS")
        parts.append(f"^FO520,{y}^A0N,40,40^FD{line.get('quantity', '')}^FS")
        y += RETURN_ROW_HEIGHT
    parts.append("^XZ")
    return "".join(parts)


def generate_return_labels(label_ins):
    labels_list = []
    for label_inst in label_ins:
        rows = label_inst.lines_info or []
        pages = [
            rows[i : i + RETURN_ROWS_PER_LABEL] for i in range(0, len(rows), RETURN_ROWS_PER_LABEL)
        ] or [[]]
        for number, page_rows in enumerate(pages, 1):
            labels_list.append(
                _return_label(
                    label_inst.kind,
                    number,
                    len(pages),
                    label_inst.data,
                    label_inst.oh_number,
                    page_rows,
                )
            )
    return labels_list
