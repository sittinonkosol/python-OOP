import sys
import sqlite3
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt
from layoutapp import Ui_MainWindow

class DatabaseManager:
    def __init__(self, db_name="mydatabase.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        sql = """
            CREATE TABLE IF NOT EXISTS user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                year TEXT,
                is_admin INTEGER
            )
        """
        self.cursor.execute(sql)
        self.conn.commit()
    
    def add_user(self, name, year, is_admin):
        sql = "INSERT INTO user (name, year, is_admin) VALUES (?,?,?)"
        self.cursor.execute(sql, (name, year, is_admin))
        self.conn.commit()
    
    def get_all_user(self):
        sql = "SELECT * FROM user"
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def update_user(self, user_id, name, year, is_admin):
        sql = "UPDATE user SET name=?, year=?, is_admin=? WHERE id=?"
        self.cursor.execute(sql, (name, year, is_admin, user_id))
        self.conn.commit()
    
    def delete_user(self, user_id):
        sql = "DELETE FROM user WHERE id=?"
        self.cursor.execute(sql, (user_id,))
        self.conn.commit()
        
    def close(self):
        self.conn.close()
        
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.db = DatabaseManager()
        self.tableWidget.setColumnWidth(0,50)
        self.tableWidget.setColumnWidth(1,250)
        self.tableWidget.setColumnWidth(2,100)

        self.pushButton_add.clicked.connect(self.create_data)
        self.pushButton_update.clicked.connect(self.update_user)
        self.pushButton_delete.clicked.connect(self.delete_data)
        
        self.tableWidget.cellClicked.connect(self.select_data)
    
    def load_data(self):
        result = self.db.get_all_user()
        self.tableWidget.setRowCount(0)
        
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            
            for column_number, data in enumerate(row_data):
                if column_number == 3:
                    display_text = "Yes" if data == 1 else "No"
                else:
                    display_text = str(data)
                    
                item = QTableWidgetItem(display_text)
                item.setFlags(item.flags() ^ Qt.ItemIsEditable)
                self.tableWidget.setItem(row_number, column_number, item)
    
    def create_data(self):
        name = self.lineEdit_name.text()
        year = self.lineEdit_year.text()
        is_admin = 1 if self.checkBox_isadmin.isChecked() else 0
        
        if name and year:
            self.db.add_user(name, year, is_admin)
            self.load_data()
            self.clear_form()
            QMessageBox.information(self, "Success", "User added successfully!")
        else:
            QMessageBox.warning(self, "Input Error", "Please provide both Name and Year.")
     
    def select_data(self):
        row = self.tableWidget.currentRow()
        self.selected_id = int(self.tableWidget.item(row, 0).text())
        self.lineEdit_name.setText(self.tableWidget.item(row, 1).text())
        self.lineEdit_year.setText(self.tableWidget.item(row, 2).text())
        is_admin = self.tableWidget.item(row, 3).text()
        self.checkBox_isadmin.setChecked(True if is_admin == "Yes" else False)
    
    def update_user(self):
        if not hasattr(self, 'selected_id'):
            QMessageBox.warning(self, "Selection Error", "Please select a user to update.")
            return
        name = self.lineEdit_name.text()
        year = self.lineEdit_year.text()
        is_admin = 1 if self.checkBox_isadmin.isChecked() else 0
        
        if name and year:
            self.db.update_user(self.selected_id, name, year, is_admin)
            self.load_data()
            self.clear_form()
            QMessageBox.information(self, "Success", "User updated successfully!")
        else:
            QMessageBox.warning(self, "Input Error", "Please provide both Name and Year.")
            
    def delete_data(self):
        if not hasattr(self, 'selected_id'):
            QMessageBox.warning(self, "Selection Error", "Please select a user to delete.")
            return
        
        confirm = QMessageBox.question(self, "Confirm Delete", "Are you sure you want to delete this user?", QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.db.delete_user(self.selected_id)
            self.load_data()
            self.clear_form()
            QMessageBox.information(self, "Success", "User deleted successfully!")
    
    def clear_form(self):
        self.lineEdit_name.clear()
        self.lineEdit_year.clear()
        self.checkBox_isadmin.setChecked(False)
        
#        if hasattr(self, 'select_id'):
#            def self.selected_id
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())