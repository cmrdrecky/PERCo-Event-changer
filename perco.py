from PyQt5           import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QInputDialog
from PyQt5.QtWidgets import *
from random import randint
from main import Ui_MainWindow
import sys
import fdb
import re
import configparser

#Создаем аппликейшен
app = QtWidgets.QApplication(sys.argv)
#Создаем форму и иницируем графический интерфейс
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

ui.pushButton_2.setEnabled(False) # Активируем после введеных личных данных
#ui.btn_toggle_menu.setEnabled(False) # На будущее

# Настройка подключения к БД
global ip,db_path,db_user,db_password #con
configparser = configparser.RawConfigParser()
configparser.read(r'db_conf.txt')
ip = configparser.get('db-config', 'ip')
db_path = configparser.get('db-config', 'db_path')
db_user = configparser.get('db-config', 'db_user')
db_password = configparser.get('db-config', 'db_password')
# Проверка на правильный ввод данных
def has_cyrillic(text):
    return bool(re.search('[а-яА-Я]', text))
def has_symbols(text):
    return bool(re.search('[0-9]', text))
# Кнопка "Ввести данные"
def id_check(self):
    ui.tableWidget.setRowCount(0)
    first_name = ui.lineEdit.text()
    last_name = ui.lineEdit_2.text()
    Data = ui.dateEdit.date().toPyDate()
    if has_cyrillic(last_name) == 0 or has_cyrillic(first_name) == 0:
        QMessageBox.warning(None, "Ошибка", "Допустима только кириллица")
        return
    elif has_symbols(last_name) == 1 or has_symbols(first_name) == 1:
        QMessageBox.warning(None, "Ошибка", "Присутствуют цифры в личных данных")
        return
    elif ' ' in last_name or ' ' in first_name:
        QMessageBox.warning(None, "Ошибка", "Уберите пробелы из личных данных")
        return
    # Подключаемся к БД
    con = fdb.connect(host=ip, database=db_path, user=db_user, password=db_password, charset='UTF8')
    con.begin()
    cur = con.cursor()
    # Узнаем ID по данным
    cur.execute("SELECT ID_STAFF FROM STAFF WHERE LAST_NAME LIKE '%s' AND FIRST_NAME LIKE '%s'" % (last_name, first_name))
    staff_id = str(cur.fetchall())
    staff_id = re.sub('[^0-9]', '', staff_id)
    if staff_id == '':
        QMessageBox.warning(None, "Ошибка", "Такой сотрудник не найден.\nПроверьте данные.")
        con.close()
        return
    # Шапка таблицы REG_EVENTS: "select rdb$field_name from rdb$relation_fields where rdb$relation_name='REG_EVENTS'"
    # Узнаем проходы сотрудника за выбранную дату
    cur.execute("SELECT DATE_EV, TIME_EV, STAFF_ID, AREAS_ID FROM REG_EVENTS WHERE DATE_EV LIKE '%s' AND STAFF_ID LIKE '%s'" % (Data, staff_id))
    result = cur.fetchall()
    """AREAS_ID: 10640 - Вход | 10653 - Выход"""
    for i, n in enumerate(result):
      if n[3] == 10640:
        n = list(n)
        n[3] = "Вход"
        result[i] = tuple(n)
      elif n[3] == 10653:
        n = list(n)
        n[3] = "Выход"
        result[i] = tuple(n)
    ui.tableWidget.setSortingEnabled(False) # Если включить сортировку в начале, то она потрет все строки.
    # Вписываем выборку в таблицу программы
    for row_number, row_data in enumerate(result):
        ui.tableWidget.insertRow(row_number)
        for column_number, data in enumerate(row_data):
            ui.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
    con.close()
    ui.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) # Закрываем редактирование таблицы
    ui.tableWidget.horizontalHeader().setDefaultSectionSize(122) # Выровняли столбцы по горизонтали
    ui.tableWidget.setSortingEnabled(True) # Включаем сортировку столбцов
    ui.pushButton_2.setEnabled(True)
ui.pushButton.clicked.connect(id_check)
# Кнопка "Изменить событие"
def rowToChange():
    if not ui.tableWidget.selectedIndexes(): # Проверка на пустой список (Выбрал ли пользователь строку в таблице)
        QMessageBox.warning(None, "Ошибка", "Выберите строку для изменения!")
        return
    row_date = ui.tableWidget.selectedItems()[0].text()
    row_time = ui.tableWidget.selectedItems()[1].text()
    row_id = ui.tableWidget.selectedItems()[2].text()
    def hourToChange(): # Меняем на нужный час
        if row_time[:2] == '12' and row_time[3:5] <= '10':
            hour_time = '11'
            return hour_time
        elif row_time[:2] == '08':
            hour_time = '07'
            return hour_time
        else:
            return row_time[:2]
    def randTime(): # Меняем на нужные минуты
        rsm = '00'
        if row_time[:2] == '11' and row_time[3:5] >= '30' or row_time[:2] == '12' and row_time[3:5] <= '10':
            rsm = randint(18,29)
            return str(rsm)
        elif row_time[:2] == '08':
            rsm = randint(45,58)
            return str(rsm)
        else:
            return row_time[3:5]
    new_row_time =  '%s:%s:%s' % (hourToChange(), randTime(), randTime())
    # Изменяем запись в БД
    con = fdb.connect(host=ip, database=db_path, user=db_user, password=db_password, charset='UTF8')
    con.begin()
    cur = con.cursor()
    #TABEL_INTERMEDIADATE = Вкладка с отчетами
    cur.execute("UPDATE TABEL_INTERMEDIADATE SET TIME_PASS = '%s' WHERE STAFF_ID LIKE '%s' AND DATE_PASS LIKE '%s' AND TIME_PASS = '%s'" % (new_row_time, row_id, row_date, row_time))
    con.commit()
    # REG EVENTS - Вкладка События
    cur.execute("UPDATE REG_EVENTS SET TIME_EV = '%s' WHERE STAFF_ID = '%s' AND DATE_EV = '%s' AND TIME_EV = '%s'" % (new_row_time, row_id, row_date, row_time))
    con.commit()
    con.close()
    QMessageBox.warning(None, "Успех", "Готово")
ui.pushButton_2.clicked.connect(rowToChange)
# Кнопка "Помощь"
def helpButton(event):
    QMessageBox.warning(None, "Описание", "При изменении события:\nПроход в 8 часов меняется на 7:%%:%%\nПроход в промежутке между 11:30-12:10 меняется на 11:%%:%%\nПроходы в других промежутках остаются прежними")
ui.label_user_icon.mousePressEvent = helpButton
#Запускаем цикл
sys.exit(app.exec_())