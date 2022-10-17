import user_interface as ui
import view_data as vd
import data_interface as di


while True:
    comm_list = ui.get_command_str('\nФормат данных запроса: Команда,Фамилия,Имя,Телефон,Комментарий, если данные не указываются, то фильтрация не применяется\n' 
                                 + 'Команда \'v\' - просмотр БД, например:\n'
                                 + '              v,,,, - посмотреть все записи БД;\n'
                                 + '              v,Iv,,+7(963),, - посмотреть записи с фамилией начинающейся на Iv и телефоном начинающемся на +7(963);\n'
                                 + 'Команда \'e\' - редактирование записи БД, например:\n'
                                 + '              e,,Ivan,, - отредактировать записи с именем \'Ivan\', откроется диалог по редактированию;\n'
                                 + 'Команда \'d\' - удаление записи, например:\n'
                                 + '              d,,,, - откроется диалог по удалению;\n'
                                 + 'Команда \'a\' - добавление новой записи, например:\n'
                                 + '              a,Sidorov,Ivan,+7(963)555-1234,Work - добавили Sidorov Ivan, тел.:+7(963)555-1234, комментарий: Work;\n'
                                 + 'Команда \'init\' - заполняет БД тестовыми значениями;\n'
                                 + 'Команда \'q\' - выход из программы\n\n'
                                 + 'Введите команду: ')
    if comm_list[0] == 'e':     # редактирование записи
        comm_list.pop(0)
        if ui.edit_request(comm_list) == di.OK_RETURN:
            vd.print_ok()
        else:
            vd.print_err()
    elif comm_list[0] == 'd':   # Удаление записи
        comm_list.pop(0)
        if ui.del_request(comm_list) == di.OK_RETURN:
            vd.print_ok()
        else:
            vd.print_err
    elif comm_list[0] == 'a':   # Добавление записи
        comm_list.pop(0)
        if ui.add_request(comm_list) == di.OK_RETURN:
            vd.print_ok()
        else:
            vd.print_err()
    elif comm_list[0] == 'v':   # Просмотр записей
        comm_list.pop(0)
        ui.view_request(comm_list)
    elif comm_list[0] == 'init':    # Заполнение БД тестовыми записями
        if ui.init_data() == di.OK_RETURN:
            vd.print_ok()
        else:
            vd.print_err()
    elif comm_list[0] == 'q':   # Выход из программы
        break
    else:
        vd.print_message('ТАКОЙ КОМАНДЫ НЕТ')

