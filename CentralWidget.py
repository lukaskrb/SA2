from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QRadioButton, QButtonGroup, QGridLayout, QCheckBox


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        label_username = QLabel("Benutzername:")
        label_password = QLabel("Benutzerkennwort:")
        label_password.setAlignment(Qt.AlignmentFlag.AlignRight)

        label_customer_number = QLabel("Kundennummer:")
        lineedit_customer_number = QLineEdit()
        lineedit_customer_number.setInputMask(">AAAaa;?")


        lineedit_username = QLineEdit()
        lineedit_password = QLineEdit()
        lineedit_password.setMaxLength(10)
        lineedit_password.setEchoMode(QLineEdit.EchoMode.Password)

        headline_extra = QLabel("Extras:")
        headline_extra.setAlignment(Qt.AlignmentFlag.AlignLeft)



        radio_button_kaese = QRadioButton("Käse")
        radio_button_schinken = QRadioButton("Schinken")
        radio_button_salami = QRadioButton("Salami")
        radio_button_oliven = QRadioButton("Oliven")

        radio_button_group = QButtonGroup()
        radio_button_group.addButton(radio_button_kaese)
        radio_button_group.addButton(radio_button_schinken)
        radio_button_group.addButton(radio_button_salami)
        radio_button_group.addButton(radio_button_oliven)

        label_sonsitges = QLabel("Sonstiges:")

        check_box_schnell = QCheckBox("Schnelle Lieferung")
        check_box_klinel = QCheckBox("Nicht klingeln")
        check_box_trinkgeld = QCheckBox("Trinkgeld")
        check_box_abholen = QCheckBox("Selbstabholer")

        label_info = QLabel("Weitere Informationen:")
        lineedit_info = QLineEdit()


        layout = QGridLayout()
        layout.addWidget(label_username, 1, 1)
        layout.addWidget(lineedit_username, 1, 2)
        layout.addWidget(label_customer_number, 2, 1)
        layout.addWidget(lineedit_customer_number, 2, 2)
        layout.addWidget(label_password, 3, 1)
        layout.addWidget(lineedit_password, 3, 2)
        layout.addWidget(headline_extra, 4, 1)
        layout.addWidget(radio_button_kaese, 5, 1)
        layout.addWidget(radio_button_schinken, 6, 1)
        layout.addWidget(radio_button_salami, 7, 1)
        layout.addWidget(radio_button_oliven, 8, 1)
        layout.addWidget(label_sonsitges, 4, 2)
        layout.addWidget(check_box_klinel, 5, 2)
        layout.addWidget(check_box_schnell, 6, 2)
        layout.addWidget(check_box_trinkgeld, 7, 2)
        layout.addWidget(check_box_abholen, 8, 2)
        layout.addWidget(label_info, 9, 1, 1, 2)
        layout.addWidget(lineedit_info, 10, 1, 1, 2)


        self.setLayout(layout)


