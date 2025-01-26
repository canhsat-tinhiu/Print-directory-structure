import os
import tkinter as tk
from tkinter import filedialog, messagebox

def write_directory_structure(base_dir, output_file):
    def generate_structure(dir_path, prefix="", is_last=False):
        entries = sorted(os.listdir(dir_path))  # Sắp xếp để hiển thị gọn gàng
        for i, entry in enumerate(entries):
            entry_path = os.path.join(dir_path, entry)
            is_last_entry = i == len(entries) - 1
            if os.path.isfile(entry_path):
                # Gắn tiền tố cho file
                structure.append(f"{prefix}└── {entry}" if is_last_entry else f"{prefix}├── {entry}")
            elif os.path.isdir(entry_path):
                # Gắn tiền tố cho thư mục (bỏ dấu `/`)
                structure.append(f"{prefix}└── {entry}" if is_last_entry else f"{prefix}├── {entry}")
                # Đệ quy để xử lý các thư mục con
                new_prefix = f"{prefix}    " if is_last_entry else f"{prefix}│   "
                generate_structure(entry_path, new_prefix, is_last_entry)

    # Lấy tên thư mục gốc (không có dấu `/`)
    structure = [f"{os.path.basename(base_dir)}"]
    generate_structure(base_dir)

    # Ghi cấu trúc vào file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(structure))

def browse_directory():
    # Mở hộp thoại chọn thư mục
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        entry_folder.delete(0, tk.END)
        entry_folder.insert(0, folder_selected)

def save_structure():
    base_dir = entry_folder.get()
    if not os.path.isdir(base_dir):
        messagebox.showerror("Lỗi", "Vui lòng chọn một thư mục hợp lệ!")
        return

    # Tạo đường dẫn cho file đầu ra
    output_file = os.path.join(base_dir, "cautructhumuc.txt")

    # Ghi cấu trúc thư mục vào file
    write_directory_structure(base_dir, output_file)
    messagebox.showinfo("Thành công", f"Cấu trúc thư mục đã được lưu vào\n{output_file}")

# Tạo giao diện chính
root = tk.Tk()
root.title("Ghi Cấu Trúc Thư Mục")

# Nhãn và ô nhập thư mục
label_folder = tk.Label(root, text="Thư mục:")
label_folder.grid(row=0, column=0, padx=10, pady=10)

entry_folder = tk.Entry(root, width=50)
entry_folder.grid(row=0, column=1, padx=10, pady=10)

button_browse = tk.Button(root, text="Duyệt...", command=browse_directory)
button_browse.grid(row=0, column=2, padx=10, pady=10)

# Nút lưu
button_save = tk.Button(root, text="Lưu Cấu Trúc", command=save_structure, bg="lightblue")
button_save.grid(row=1, column=1, pady=20)

# Chạy giao diện
root.mainloop()
