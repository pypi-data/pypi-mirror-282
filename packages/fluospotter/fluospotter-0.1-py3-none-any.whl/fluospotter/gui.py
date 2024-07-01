import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QSlider, QHBoxLayout, QAction, QFileDialog, QToolTip
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
import tifffile as tiff  # For loading TIFF files


class VolumeViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.volume = None
        self.filename = None
        self.current_slice = 0
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Volume Viewer | Fluospotter')

        # Create menu bar
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')

        # Add actions to the menu
        load_action = QAction('Load Volume...', self)
        load_action.triggered.connect(self.load_volume)
        file_menu.addAction(load_action)
        file_menu.addSeparator()
        exit_action = QAction('Exit', self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Main widget
        self.main_widget = QWidget()
        self.main_layout = QHBoxLayout()

        # Image display
        self.image_label = QLabel()
        self.main_layout.addWidget(self.image_label)

        # Control panel
        self.control_panel = QVBoxLayout()

        # File name label
        self.file_label = QLabel('File: ')
        self.control_panel.addWidget(self.file_label)

        # Slice slider
        slice_layout = QHBoxLayout()
        self.slice_label = QLabel('Slice: 0')
        slice_layout.addWidget(self.slice_label)
        self.slice_slider = QSlider(Qt.Horizontal)
        self.slice_slider.setMinimum(0)
        self.slice_slider.setMaximum(0)
        self.slice_slider.setValue(0)
        self.slice_slider.valueChanged.connect(self.change_slice)
        slice_layout.addWidget(self.slice_slider)

        self.control_panel.addLayout(slice_layout)
        self.main_layout.addLayout(self.control_panel)
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)

        # Delete later #
        self.filename = r"C:\Users\arnau.blanco\OneDrive - Bruker Physik GmbH\Documents\GitHub\Fluospotter\data\test\Location-03.tif"
        self.volume = tiff.imread(self.filename)
        self.slice_slider.setMaximum(self.volume.shape[0] - 1)
        self.slice_slider.setValue(0)
        filename = self.filename
        if len(filename) > 30: filename = filename[:30] + "..."
        self.file_label.setText(f'File: {filename}')
        self.file_label.setToolTip(self.filename)  # Set tooltip with full file name
        self.update_image()
        ##

    def load_volume(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Volume File", "", "TIFF Files (*.tif);;All Files (*)",
                                                   options=options)

        if file_name:
            self.filename = file_name
            self.volume = tiff.imread(file_name)
            self.slice_slider.setMaximum(self.volume.shape[0] - 1)
            self.slice_slider.setValue(0)
            filename = self.filename
            if len(filename) > 30: filename = filename[:30] + "..."
            self.file_label.setText(f'File: {filename}')
            self.file_label.setToolTip(self.filename)  # Set tooltip with full file name
            self.update_image()

    def change_slice(self, value):
        self.current_slice = value
        self.slice_label.setText(f"Slice: {value}")
        self.update_image()

    def update_image(self):
        if self.volume is not None:
            slice_image = self.volume[self.current_slice]
            qimage = QImage(slice_image.data, slice_image.shape[1], slice_image.shape[0], QImage.Format_Grayscale16)
            pixmap = QPixmap.fromImage(qimage)
            self.image_label.setPixmap(pixmap)
            self.image_label.setFixedSize(pixmap.size())


def main():
    app = QApplication(sys.argv)
    viewer = VolumeViewer()
    viewer.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()