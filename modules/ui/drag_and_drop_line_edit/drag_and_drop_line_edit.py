from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtGui import QPainter, QColor, QFont
from PyQt6.QtCore import Qt

class DragAndDropLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.is_dragging = False

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            self.is_dragging = True
            event.accept()
            self.update()
        else:
            event.ignore()

    def dragLeaveEvent(self, event):
        self.is_dragging = False
        self.update()

    def dropEvent(self, event):
        self.is_dragging = False
        self.update()
        
        files = event.mimeData().urls()
        if files:
            file_path = files[0].toLocalFile()
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    self.setText(f.read().strip())
            except Exception as e:
                self.setText("System Error: Could not read file.")

    def paintEvent(self, event):
        super().paintEvent(event)
        
        if self.is_dragging:
            painter = QPainter(self)
            
            painter.setBrush(QColor(182, 112, 50, 100)) 
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawRect(self.rect())

            painter.setPen(QColor("white"))
            painter.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))
            painter.drawText(
                self.rect(),
                Qt.AlignmentFlag.AlignCenter, 
                "DROP KEY HERE"
            )
            painter.end()