# FaceClassify 🧑‍💻🖼️

**FaceClassify** is an interactive face detection and classification application built with Python and Tkinter. It allows users to browse through a directory of images, detect faces, and classify each face into a separate folder for organization. The app provides an intuitive graphical interface to visualize the process and manage face detection and classification with ease.

---

## Features 🎯

- **Multi-Face Detection**: Detects multiple faces in an image, regardless of the image format (PNG, JPEG, JPG, WebP, etc.).
- **Image Navigation**: Navigate through images with next and previous buttons.
- **Classified Face Management**: Automatically create a folder for each detected face and store images.
- **Face Tiles**: Display tiles of all detected faces for easy selection.
- **Auto-Classification**: Allows auto-completion of the previously defined class of faces.
- **Face Classification**: Click to classify each face and save it into a dedicated folder, including a log of all classified faces and their image paths.
- **Path Display**: Displays the image path and allows you to copy it for easy referencing.

## How to Use 💻


### 1. Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone [[https://github.com/NishithSaiSeshaKumar/FaceClassify.git)](https://github.com/NishithSaiSeshaKumar/FaceClassify.git))](https://github.com/NishithSaiSeshaKumar/FaceClassify.git)
```
Replace yourusername with your actual GitHub username.

### 2. Install Dependencies
Install the required dependencies using either pip or conda:

Using pip:


```Bash
pip install -r requirements.txt
```
Using conda:



```Bash
conda install --file requirements.txt
```
### 3. Run the Application
Navigate to the folder containing the Python script (faceclassify_app.py) and run the program:



```Bash
python faceclassify_app.py
```
### 4. Select Input Folder
Select the folder containing the images you want to process. The app will process each image, detect faces, and display them in a split window.

### 5. Classify Faces
Click on the face tiles to classify each face. You can either type a name for the class or select from previously defined categories. Each classified face will be saved in a separate folder along with a log file containing the face paths.

### 6. Save the Classified Faces
Click the save button to save the classified faces in their respective folders.


## Requirements 📦
* Python 3.6+
* Tkinter (for GUI)
* OpenCV (for face detection and processing)
* Pillow (for image manipulation)
* os, shutil (for directory operations)

## File Structure 📂
```bash
/FaceClassify
│
├── /input_images/        # Folder to store input images
│
├── /classified_faces/    # Folder where classified face images are saved
│   ├── /person_name/
│       ├── face_image1.jpg
│       └── face_image2.jpg
│   └── /another_person/
│       └── face_image3.jpg
│
├── faceclassify_app.py    # Main script for the app
└── requirements.txt       # Python dependencies file
```
## How It Works 🔍
Image Loading and Face Detection:
The program reads images from the input folder and uses OpenCV for face detection. Once faces are detected, it visualizes them as tiles on the right side of the interface.

### User Interface:
The user can select a face from the tiles and classify it. The app will automatically create a folder for the person and store the image in that folder along with a log of classified faces.

### Face Class Log:
Each face folder contains a log file, which records the names of classified faces and the image paths they appear in. This helps with tracking face classification history.

### Path Copy:
The file path of each image is displayed and can be copied for reference or further processing.

## Contributing 🤝
Contributions are welcome! If you have suggestions, bug fixes, or improvements, feel free to open an issue or submit a pull request.

Steps for contributing:
  * Fork the repository
   * Create a new branch for your changes
   * Commit your changes
  * Push to your forked repository
  * Open a pull request with a detailed description of your changes
# License 📜
   This project is licensed under the MIT License - see the LICENSE file for details.

# Acknowledgments 🙏
OpenCV for computer vision and face detection.
Tkinter for creating the user interface.
Pillow for image manipulation and display.
