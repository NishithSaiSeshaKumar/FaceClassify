import os
import cv2
import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from PIL import Image, ImageTk
from functools import partial

class FaceClassifierApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Detection and Classification")
        self.root.geometry("1200x700")

        # Variables
        self.image_paths = []
        self.current_index = -1
        self.output_dir = ""
        self.detected_faces = []
        self.classified_names = []
        self.load_classified_names()

        # UI Elements
        self.setup_ui()

    def setup_ui(self):
        # Input and Output folder selection
        self.folder_frame = ttk.Frame(self.root)
        self.folder_frame.pack(fill=tk.X, padx=10, pady=10)

        self.input_label = ttk.Label(self.folder_frame, text="Input Folder:")
        self.input_label.pack(side=tk.LEFT, padx=5)

        self.input_entry = ttk.Entry(self.folder_frame, width=50)
        self.input_entry.pack(side=tk.LEFT, padx=5)

        self.input_button = ttk.Button(self.folder_frame, text="Browse", command=self.select_input_folder)
        self.input_button.pack(side=tk.LEFT, padx=5)

        self.output_label = ttk.Label(self.folder_frame, text="Output Folder:")
        self.output_label.pack(side=tk.LEFT, padx=5)

        self.output_entry = ttk.Entry(self.folder_frame, width=50)
        self.output_entry.pack(side=tk.LEFT, padx=5)

        self.output_button = ttk.Button(self.folder_frame, text="Browse", command=self.select_output_folder)
        self.output_button.pack(side=tk.LEFT, padx=5)

        # Image display and navigation
        self.image_frame = ttk.Frame(self.root)
        self.image_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.left_panel = ttk.Frame(self.image_frame)
        self.left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.left_panel, bg="white", width=600, height=400)
        self.canvas.pack(padx=10, pady=10)

        self.path_entry = ttk.Entry(self.left_panel, width=80)
        self.path_entry.pack(pady=5)

        self.copy_button = ttk.Button(self.left_panel, text="Copy Path", command=self.copy_path)
        self.copy_button.pack(pady=5)

        self.right_panel = ttk.Frame(self.image_frame)
        self.right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.faces_frame = ttk.Frame(self.right_panel)
        self.faces_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.detected_faces_label = ttk.Label(self.right_panel, text="Detected Faces: 0")
        self.detected_faces_label.pack(pady=5)

        # Navigation buttons
        self.nav_frame = ttk.Frame(self.root)
        self.nav_frame.pack(fill=tk.X, padx=10, pady=10)

        self.prev_button = ttk.Button(self.nav_frame, text="Previous", command=self.show_previous_image)
        self.prev_button.pack(side=tk.LEFT, padx=5)

        self.next_button = ttk.Button(self.nav_frame, text="Next", command=self.show_next_image)
        self.next_button.pack(side=tk.RIGHT, padx=5)

    def select_input_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.input_entry.delete(0, tk.END)
            self.input_entry.insert(0, folder_path)
            self.image_paths = self.get_image_paths(folder_path)
            self.current_index = -1
            self.show_next_image()

    def select_output_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, folder_path)
            self.output_dir = folder_path

    def get_image_paths(self, folder):
        extensions = (".png", ".jpg", ".jpeg", ".webp")
        return [os.path.join(root, file)
                for root, _, files in os.walk(folder)
                for file in files if file.lower().endswith(extensions)]

    def load_classified_names(self):
        if not os.path.exists("classified_faces.txt"):
            return
        with open("classified_faces.txt", "r") as file:
            self.classified_names = [line.strip() for line in file.readlines()]

    def save_classified_name(self, name):
        if name not in self.classified_names:
            self.classified_names.append(name)
            with open("classified_faces.txt", "a") as file:
                file.write(name + "\n")

    def show_next_image(self):
        self.current_index += 1
        if self.current_index < len(self.image_paths):
            self.process_image(self.image_paths[self.current_index])
        else:
            messagebox.showinfo("End of Folder", "No more images to process.")
            self.current_index -= 1

    def show_previous_image(self):
        self.current_index -= 1
        if self.current_index >= 0:
            self.process_image(self.image_paths[self.current_index])
        else:
            messagebox.showinfo("Start of Folder", "No previous images.")
            self.current_index += 1

    def process_image(self, image_path):
        image = cv2.imread(image_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        self.detected_faces = [(x, y, w, h) for x, y, w, h in faces]

        # Skip if no faces
        if not self.detected_faces:
            self.show_next_image()
            return

        # Display original image
        self.display_image(image_path)

        # Display detected faces
        self.display_faces(image)

    def display_image(self, image_path):
        img = Image.open(image_path)
        img.thumbnail((600, 400))
        photo = ImageTk.PhotoImage(img)
        self.canvas.delete("all")
        self.canvas.create_image(300, 200, image=photo)
        self.canvas.image = photo
        self.path_entry.delete(0, tk.END)
        self.path_entry.insert(0, image_path)

    def display_faces(self, image):
        # Clear existing widgets
        for widget in self.faces_frame.winfo_children():
            widget.destroy()

        # Create a canvas and scrollbar for scrolling if needed
        faces_canvas = tk.Canvas(self.faces_frame, width=300, height=400)
        scrollbar = ttk.Scrollbar(self.faces_frame, orient=tk.VERTICAL, command=faces_canvas.yview)
        faces_container = ttk.Frame(faces_canvas)

        # Configure canvas and scrollbar
        faces_container.bind(
            "<Configure>",
            lambda e: faces_canvas.configure(scrollregion=faces_canvas.bbox("all"))
        )
        faces_canvas.create_window((0, 0), window=faces_container, anchor="nw")
        faces_canvas.configure(yscrollcommand=scrollbar.set)

        faces_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Iterate through detected faces and add tiles
        for i, (x, y, w, h) in enumerate(self.detected_faces):
            face_img = image[y:y + h, x:x + w]
            face_img_rgb = cv2.cvtColor(face_img, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(face_img_rgb)
            img.thumbnail((100, 100))
            photo = ImageTk.PhotoImage(img)

            frame = ttk.Frame(faces_container)
            frame.pack(side=tk.TOP, pady=5, padx=5)

            face_button = ttk.Button(frame, image=photo, command=partial(self.classify_face, face_img, i))
            face_button.image = photo
            face_button.pack()

            ttk.Label(frame, text=f"Face {i + 1}").pack()

        self.detected_faces_label.config(text=f"Detected Faces: {len(self.detected_faces)}")

    def classify_face(self, face_img, face_index):
        class_name = tk.simpledialog.askstring("Class Name", "Enter class name for this face:")
        if not class_name:
            return

        self.save_classified_name(class_name)

        class_dir = os.path.join(self.output_dir, class_name)
        os.makedirs(class_dir, exist_ok=True)

        save_path = os.path.join(class_dir, f"face_{self.current_index}_{face_index}.jpg")
        cv2.imwrite(save_path, face_img)

        log_path = os.path.join(class_dir, "faces_log.txt")
        with open(log_path, "a") as log_file:
            log_file.write(f"{self.image_paths[self.current_index]}\n")

        messagebox.showinfo("Saved", f"Face saved in {class_dir}.")

    def copy_path(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.path_entry.get())
        self.root.update()
        messagebox.showinfo("Copied", "File path copied to clipboard.")


if __name__ == "__main__":
    root = tk.Tk()
    app = FaceClassifierApp(root)
    root.mainloop()
