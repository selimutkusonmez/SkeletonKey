from PyQt6.QtWidgets import QTextEdit
from PyQt6.QtGui import QPainter, QColor, QFont
from PyQt6.QtCore import Qt

class DragAndDropTextEdit(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.is_dragging = False #

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
                    self.setText(f.read())
            except Exception as e:
                self.setText(f"System Error: Could not read file.\n{str(e)}")

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.is_dragging:
            painter = QPainter(self.viewport())
            
            painter.setBrush(QColor(182, 112, 50, 100)) 
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawRect(self.viewport().rect())

            painter.setPen(QColor("white"))
            painter.setFont(QFont("Segoe UI", 14, QFont.Weight.Bold))
            painter.drawText(
                self.viewport().rect(), 
                Qt.AlignmentFlag.AlignCenter, 
                "DROP HERE"
            )
            painter.end()