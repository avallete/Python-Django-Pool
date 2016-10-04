# -*- coding: utf-8 -*-

def tupple_list_to_dict(src):
    dest = {}
    for tupple in src:
        if tupple[1] in dest.keys():
            dest[tupple[1]].append(tupple[0])
        else:
            dest[tupple[1]] = [tupple[0]]
    return dest

def generate_periodic_table(periodic_data):
    periodic_html = """"""
    case_index = 0
    for elem, infos in periodic_data:
        if infos['position'] == "0":
            periodic_html += " <tr>\n"
        while case_index < int(infos['position']):
            periodic_html += """<td>&nbsp;</td>"""
            case_index += 1
        periodic_html += """
            <td style="border: 1px solid black; padding: 10px;">
                <h4>%(name)s</h4>
                <h1>%(small)s</h1>
                <ul>
                    <li>No %(number)s</li>
                    <li>%(molar)s</li>
                    <li>%(electron)s electron(s)</li>
                </ul>
            </td>
        """ % infos
        case_index += 1
        if infos['position'] == "17":
            periodic_html += " </tr>"
            case_index = 0
    return periodic_html

def generate_template(periodic_data):
    html_string = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Periodic table</title>
            <meta charset='UTF-8'>
            <style>
                td {
                    border: 1px solid black;
                    padding: 10px;
                    display: block;
                    float: left;
                }
            </style>
        </head>
        <body>
            %s
        </body>
    <html>
    """
    table_template = """
                <table style='empty-cells: show;'>
                    %s
                </table>
    """
    return(table_template % generate_periodic_table(periodic_data))

def run():
    periodic_data = []
    with open('periodic_table.txt', 'r') as fd:
        for line in fd.readlines():
            key, value = line.split('=')
            infos = value.split(',')
            periodic_data.append(
                (key, {
                    'name': key,
                    'position': infos[0].split(':')[1],
                    'number': infos[1].split(':')[1],
                    'small': infos[2].split(':')[1],
                    'molar': infos[3].split(':')[1],
                    'electron': sum(map(int, infos[4].split(':')[1].replace('\n', '').split(' '))),
                })
            )
    html_string = generate_template(periodic_data)
    with open('periodic_table.html', 'w+') as fd:
        fd.write(html_string)

if __name__ == '__main__':
    run()
