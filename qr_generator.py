# import qrcode

# data = "PAYMENT SUCESSFUL"
# img = qrcode.make(data)
# img.save("payment_qr.png")
# import qrcode

# data = "PAYMENT: ₹2000"
# img = qrcode.make(data)
# img.save("payment_qr.png")
import tkinter as tk
from PIL import Image, ImageTk
import qrcode

# ---------- Generate QR ----------
def generate_qr():
    data = "PAYMENT: SUCCESS"
    img = qrcode.make(data)
    img.save("payment_qr.png")

# ---------- Show Success Screen ----------
def show_success():
    for widget in root.winfo_children():
        widget.destroy()

    success_img = Image.open("success.png")  # your image file
    success_img = success_img.resize((400, 600))
    photo = ImageTk.PhotoImage(success_img)

    label = tk.Label(root, image=photo)
    label.image = photo
    label.pack()

# ---------- Main Window ----------
root = tk.Tk()
root.title("Payment Page")
root.geometry("400x600")

# Generate QR
generate_qr()

# Show QR
qr_img = Image.open("payment_qr.png")
qr_img = qr_img.resize((250, 250))
qr_photo = ImageTk.PhotoImage(qr_img)

tk.Label(root, text="Scan to Pay", font=("Arial", 16)).pack(pady=10)

qr_label = tk.Label(root, image=qr_photo)
qr_label.image = qr_photo
qr_label.pack(pady=20)

# Simulate scan → after 3 seconds show success
root.after(200000, show_success)

root.mainloop()