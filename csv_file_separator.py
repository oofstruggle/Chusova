import csv


def create_csv_files(compiled_data_dict, titles):
    """Создать csv-файлы с выборкой по отдельным годам
    
    
    Args:
        compiled_data_dict (dict): данные о вакансиях по годам
        titles (list): заголовки колонок
    """
    for i in compiled_data_dict.items():
        title = i[0]
        with open(f"years_data/{title}", 'w', encoding='utf-8-sig') as file:
            csv_creator = csv.writer(file, lineterminator="\r")
            csv_creator.writerow(titles)
            csv_creator.writerows(i[1])


def separate_years_data(file_strings, titles):
    """Создаёт отдельный csv-файл для каждого года
    
    
        Args:
            file_strings (list): строки, считанные из общей выгрузки
            titles (list): заголовки столбцов
    """
    listed_years_dict = {}
    date_indicator = titles.index('published_at')
    for i in file_strings:
        year = f"{i[date_indicator][0:4]}.csv"
        if year not in listed_years_dict.keys():
            listed_years_dict[year] = []
        listed_years_dict[year].append(i)
    create_csv_files(listed_years_dict, titles)
