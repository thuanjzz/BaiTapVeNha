from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

root = Tk()
root.title("Hệ thống quản lý sinh viên")
root.geometry("600x800")


# Kết nối tới cơ sở dữ liệu và tạo bảng nếu chưa tồn tại
def tao_bang():
    conn = sqlite3.connect('student_management.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            masv TEXT,
            ho TEXT,
            ten TEXT,
            malop TEXT,
            manamhoc TEXT,
            diemtrungbinh REAL
        )
    ''')
    conn.commit()
    conn.close()


# Gọi hàm tạo bảng khi khởi động
tao_bang()


def them():
    conn = sqlite3.connect('student_management.db')
    c = conn.cursor()

    # Lấy dữ liệu đã nhập
    masv_value = masv.get()
    ho_value = ho.get()
    ten_value = ten.get()
    malop_value = malop.get()
    manamhoc_value = manamhoc.get()
    diemtrungbinh_value = diemtrungbinh.get()

    # Thực hiện câu lệnh để thêm
    c.execute('''
        INSERT INTO 
        students (masv, ho, ten, malop, manamhoc, diemtrungbinh)
        VALUES 
        (?, ?, ?, ?, ?, ?)
    ''', (masv_value, ho_value, ten_value, malop_value, manamhoc_value, diemtrungbinh_value))

    conn.commit()
    conn.close()

    # Reset form
    masv.delete(0, END)
    ho.delete(0, END)
    ten.delete(0, END)
    malop.delete(0, END)
    manamhoc.delete(0, END)
    diemtrungbinh.delete(0, END)

    # Hiển thị lại dữ liệu
    truy_van()


def xoa():
    conn = sqlite3.connect('student_management.db')
    c = conn.cursor()
    c.execute('DELETE FROM students WHERE id=?', (delete_box.get(),))
    delete_box.delete(0, END)
    conn.commit()
    conn.close()
    messagebox.showinfo("Thông báo", "Đã xóa!")
    truy_van()


def truy_van():
    for row in tree.get_children():
        tree.delete(row)

    conn = sqlite3.connect('student_management.db')
    c = conn.cursor()
    c.execute("SELECT * FROM students")
    records = c.fetchall()

    for r in records:
        tree.insert("", END, values=(r[0], r[1], r[2], r[3], r[4], r[5], r[6]))

    conn.close()


def chinh_sua():
    global editor
    editor = Tk()
    editor.title('Cập nhật bản ghi')
    editor.geometry("400x300")

    conn = sqlite3.connect('student_management.db')
    c = conn.cursor()
    record_id = delete_box.get()
    c.execute("SELECT * FROM students WHERE id=?", (record_id,))
    records = c.fetchall()

    global masv_editor, ho_editor, ten_editor, malop_editor, manamhoc_editor, diemtrungbinh_editor

    masv_editor = Entry(editor, width=30)
    masv_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    ho_editor = Entry(editor, width=30)
    ho_editor.grid(row=1, column=1, padx=20)
    ten_editor = Entry(editor, width=30)
    ten_editor.grid(row=2, column=1)
    malop_editor = Entry(editor, width=30)
    malop_editor.grid(row=3, column=1)
    manamhoc_editor = Entry(editor, width=30)
    manamhoc_editor.grid(row=4, column=1)
    diemtrungbinh_editor = Entry(editor, width=30)
    diemtrungbinh_editor.grid(row=5, column=1)

    for record in records:
        masv_editor.insert(0, record[1])
        ho_editor.insert(0, record[2])
        ten_editor.insert(0, record[3])
        malop_editor.insert(0, record[4])
        manamhoc_editor.insert(0, record[5])
        diemtrungbinh_editor.insert(0, record[6])

    edit_btn = Button(editor, text="Lưu bản ghi", command=cap_nhat)
    edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=145)


def cap_nhat():
    conn = sqlite3.connect('student_management.db')
    c = conn.cursor()
    record_id = delete_box.get()

    c.execute("""UPDATE students SET
           masv = ?,
           ho = ?,
           ten = ?,
           malop = ?,
           manamhoc = ?,
           diemtrungbinh = ?
           WHERE id = ?""",
              (
                  masv_editor.get(),
                  ho_editor.get(),
                  ten_editor.get(),
                  malop_editor.get(),
                  manamhoc_editor.get(),
                  diemtrungbinh_editor.get(),
                  record_id
              ))

    conn.commit()
    conn.close()
    editor.destroy()
    truy_van()


# Khung nhập liệu
input_frame = Frame(root)
input_frame.pack(pady=10)

# Các ô nhập liệu
masv = Entry(input_frame, width=30)
masv.grid(row=0, column=1, padx=20, pady=(10, 0))
ho = Entry(input_frame, width=30)
ho.grid(row=1, column=1)
ten = Entry(input_frame, width=30)
ten.grid(row=2, column=1)
malop = Entry(input_frame, width=30)
malop.grid(row=3, column=1)
manamhoc = Entry(input_frame, width=30)
manamhoc.grid(row=4, column=1)
diemtrungbinh = Entry(input_frame, width=30)
diemtrungbinh.grid(row=5, column=1)

# Các nhãn
masv_label = Label(input_frame, text="Mã SV")
masv_label.grid(row=0, column=0, pady=(10, 0))
ho_label = Label(input_frame, text="Họ")
ho_label.grid(row=1, column=0)
ten_label = Label(input_frame, text="Tên")
ten_label.grid(row=2, column=0)
malop_label = Label(input_frame, text="Mã Lớp")
malop_label.grid(row=3, column=0)
manamhoc_label = Label(input_frame, text="Mã Năm Học")
manamhoc_label.grid(row=4, column=0)
diemtrungbinh_label = Label(input_frame, text="Điểm trung bình")
diemtrungbinh_label.grid(row=5, column=0)

# Khung nút chức năng
button_frame = Frame(root)
button_frame.pack(pady=10)

submit_btn = Button(button_frame, text="Thêm sinh viên", command=them)
submit_btn.grid(row=0, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
query_btn = Button(button_frame, text="Hiển thị danh sách", command=truy_van)
query_btn.grid(row=1, column=0, columnspan=2, pady=10, padx=10, ipadx=137)
delete_box_label = Label(button_frame, text="Chọn ID")
delete_box_label.grid(row=2, column=0, pady=5)
delete_box = Entry(button_frame, width=30)
delete_box.grid(row=2, column=1, pady=5)
delete_btn = Button(button_frame, text="Xóa sinh viên", command=xoa)
delete_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=136)
edit_btn = Button(button_frame, text="Chỉnh sửa sinh viên", command=chinh_sua)
edit_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=125)

# Khung cho Treeview
tree_frame = Frame(root)
tree_frame.pack(pady=10)

# Treeview để hiển thị bản ghi
columns = ("ID", "Mã SV", "Họ", "Tên", "Mã Lớp", "Mã Năm Học", "Điểm TB")
tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=15)
for column in columns:
    tree.column(column, anchor=CENTER)
    tree.heading(column, text=column)
tree.pack()

# Hiển thị danh sách sinh viên khi khởi động
truy_van()

root.mainloop()
