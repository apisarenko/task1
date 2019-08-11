from django.shortcuts import render
import csv


def inflation_view(request):
    template_name = 'inflation.html'

    with open('inflation_russia.csv', mode='r', encoding='utf8', newline='') as file:
        reader = csv.reader(file, delimiter=';')
        inf_list = list(reader)
        list_contents_table = inf_list[0]
        del (inf_list[0])
        list_data_table = []
        for data_table in inf_list:
            list_data_in_year = []
            year = data_table[0]
            list_data_in_year.append(year)
            del (data_table[0])
            x = 0
            for data_table[x] in data_table:
                if data_table[x] != '':
                    data_table[x] = float(data_table[x])
                else:
                    data_table[x] = '-'
                x += 1
            list_data_in_year.extend(data_table)
            list_data_table.append(list_data_in_year)

    context = {'contents_list': list_contents_table,
               'data_list': list_data_table}

    return render(request, template_name,
                  context)
