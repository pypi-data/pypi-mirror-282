import json
import sys

import qdarkstyle
from fake import (
    FAKER,
    PROVIDER_REGISTRY,
    get_provider_args,
    organize_providers,
    format_type_hint,
)
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QMainWindow,
    QMenu,
    QMessageBox,
    QPushButton,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)

__title__ = "fake.py"
__version__ = "0.1"
__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2024 Artur Barseghyan"
__license__ = "MIT"
__all__ = (
    "FakePyQTApp",
    "main",
)

PROVIDER_LIST = list(PROVIDER_REGISTRY["fake.Faker"])
PROVIDER_TAGS = [(provider, provider.tags) for provider in PROVIDER_LIST]


class FakePyQTApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.categories = organize_providers(PROVIDER_TAGS)
        self.setWindowTitle("fake.py GUI")
        self.setGeometry(100, 100, 900, 600)
        self.init_ui()

    def init_ui(self):
        # Main layout container
        container = QWidget()
        self.setCentralWidget(container)
        layout = QHBoxLayout()

        # Left layout for provider tree and buttons
        left_layout = QVBoxLayout()

        # Category and provider tree
        self.provider_tree = QTreeWidget()
        self.provider_tree.setHeaderLabel("Providers")
        self.provider_tree.currentItemChanged.connect(self.on_provider_selected)
        left_layout.addWidget(self.provider_tree)

        # Collapse All and Expand All buttons
        buttons_layout = QHBoxLayout()
        self.collapse_button = QPushButton("Collapse All")
        self.collapse_button.clicked.connect(self.collapse_all)
        buttons_layout.addWidget(self.collapse_button)

        self.expand_button = QPushButton("Expand All")
        self.expand_button.clicked.connect(self.expand_all)
        buttons_layout.addWidget(self.expand_button)

        left_layout.addLayout(buttons_layout)

        layout.addLayout(left_layout, 1)

        # Dynamic form for provider arguments
        self.form_widget = QWidget()
        self.form_layout = QFormLayout()
        self.form_layout.setLabelAlignment(Qt.AlignLeft)
        self.form_widget.setLayout(self.form_layout)
        layout.addWidget(self.form_widget, 2)

        # Results display
        results_layout = QVBoxLayout()
        self.results_display = QListWidget()
        self.results_display.setContextMenuPolicy(Qt.CustomContextMenu)
        self.results_display.customContextMenuRequested.connect(
            self.open_context_menu
        )
        results_layout.addWidget(self.results_display)

        # Clear list button
        self.clear_button = QPushButton("Clear List")
        self.clear_button.clicked.connect(self.clear_list)
        results_layout.addWidget(self.clear_button)

        layout.addLayout(results_layout, 1)

        container.setLayout(layout)

        self.populate_providers()

    def populate_providers(self):
        for category, providers in self.categories.items():
            category_item = QTreeWidgetItem(self.provider_tree, [category])
            for provider in providers:
                QTreeWidgetItem(category_item, [provider])

    def on_provider_selected(self, current, previous):
        if (
            current and current.parent()
        ):  # Check if it is a provider node, not a category
            provider_name = current.text(0)
            provider_func = getattr(FAKER, provider_name)
            self.build_form(provider_func)

    def build_form(self, provider_func):
        # Clear existing form widgets
        while self.form_layout.count():
            child = self.form_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        # Get provider arguments and create form fields
        args_with_types = get_provider_args(provider_func)
        for arg, arg_type in args_with_types.items():
            label = QLabel(f"{arg}:")  # Removed type hint from the label
            label.setAlignment(
                Qt.AlignLeft
            )  # Ensure label alignment to the left
            entry = QLineEdit()
            self.form_layout.addRow(label, entry)
            setattr(self, arg, entry)

            # Determine type hint details
            type_hint_details = format_type_hint(arg_type)

            # Add type hint label
            type_hint = QLabel(f"Type: {type_hint_details}")
            type_hint.setAlignment(
                Qt.AlignLeft
            )  # Ensure type hint alignment to the left
            type_hint.setStyleSheet("font-size: 10px; color: gray;")
            self.form_layout.addRow(type_hint)

        # Add generate button
        generate_button = QPushButton("Generate")
        generate_button.clicked.connect(
            lambda: self.generate_data(provider_func)
        )
        self.form_layout.addRow(generate_button)

    def generate_data(self, provider_func):
        kwargs = {}
        count = self.form_layout.count()
        for i in range(0, count - 1, 3):  # Step by 3: label, entry, type_hint
            label = self.form_layout.itemAt(i).widget().text()[:-1]
            entry = self.form_layout.itemAt(i + 1).widget()
            value = entry.text().strip()
            if value:
                try:
                    kwargs[label] = json.loads(value)
                except json.JSONDecodeError:
                    kwargs[label] = value

        try:
            result = provider_func(**kwargs)
            self.results_display.addItem(str(result))
            # Scroll to bottom when new item is added
            self.results_display.scrollToBottom()
        except Exception as e:
            QMessageBox.critical(
                self, "Error", f"Error generating data: {str(e)}"
            )

    def open_context_menu(self, position):
        menu = QMenu()
        copy_action = menu.addAction("Copy")
        delete_action = menu.addAction("Delete")
        action = menu.exec_(
            self.results_display.viewport().mapToGlobal(position)
        )

        if action == copy_action:
            selected_item = self.results_display.currentItem()
            if selected_item:
                clipboard = QApplication.clipboard()
                clipboard.setText(selected_item.text())
        elif action == delete_action:
            selected_item = self.results_display.currentItem()
            if selected_item:
                self.results_display.takeItem(
                    self.results_display.row(selected_item)
                )

    def clear_list(self):
        self.results_display.clear()

    def collapse_all(self):
        self.provider_tree.collapseAll()

    def expand_all(self):
        self.provider_tree.expandAll()


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    ex = FakePyQTApp()
    ex.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
