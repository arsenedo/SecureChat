import sys
from PyQt6.QtWidgets import *
from commands.command_invoker import CommandInvoker
from commands import command_invoker
from payload import PayloadType
from PyQt6 import uic
from commands import send_text_command
from commands.caesar_shift_command import *
from commands.select_message_to_buffer import *
from commands.vigenere_command import *
from commands.rsa_command import *
from encoder import difhel_half_key, difhel_secret, Encoder
from commands.hash_command import *

class MainWindow(QMainWindow):
    def __init__(self, command_invoker: CommandInvoker, encoder: Encoder):
        super().__init__()

        self.command_invoker = command_invoker

        self.encoder = encoder

        uic.loadUi("src/securechat.ui", self)

        self.setupListeners();

        self.setupPages()

        self.show()

    def setupPages(self):
        self.setupShiftPage()

        self.setupVigenerePage()

        self.setupRSAPage()

        self.setupDifHel()

        self.setupHash()

    def setupListeners(self):
        btnSendText: QPushButton = self.btnSendText
        btnSelectMsgToBuffer: QPushButton = self.selectMsgToBuffer

        btnSendText.clicked.connect(self.onSendPlainTextClick)
        btnSelectMsgToBuffer.clicked.connect(self.onSelectMsgToBufferClick)

    def appendToMessageDisplay(self, msg: str):
        messageDisplay: QLabel = self.messageDisplay
        messageDisplay.setText(f"{messageDisplay.text()}{msg}\n")

    def onSendPlainTextClick(self):
        msgInput: QLineEdit = self.msgInput

        self.command_invoker.set_command(send_text_command.SendTextCommand(msgInput.text(), self.getCurrentPayloadType()))
        self.command_invoker.execute_command()

    def onSelectMsgToBufferClick(self):
        self.show_input_popup()

    def getCurrentPayloadType(self):
        chk_payload_type: QCheckBox = self.chkSendToServerOnly

        return PayloadType.TEXT if not chk_payload_type.isChecked() else PayloadType.SERVER_TEXT

    def show_input_popup(self):
        # Create the dialog
        dialog = QDialog()
        dialog.setWindowTitle("Select to buffer")
        
        # Create layout
        layout = QVBoxLayout()
        
        # Input field
        input_field = QLineEdit()
        input_field.setPlaceholderText("Enter message ID...")
        layout.addWidget(input_field)
        
        # Buttons
        button_layout = QHBoxLayout()
        btn_plain = QPushButton("In Plain")
        btn_encoded = QPushButton("In Encoded")
        
        button_layout.addWidget(btn_plain)
        button_layout.addWidget(btn_encoded)
        layout.addLayout(button_layout)
        
        # Logic for buttons
        btn_plain.clicked.connect(lambda: self.set_and_execute_command(SelectMessageToBuffer(f"{input_field.text()} c")))
        btn_plain.clicked.connect(dialog.accept)
        
        btn_encoded.clicked.connect(lambda: SelectMessageToBuffer(f"{input_field.text()} e"))
        btn_encoded.clicked.connect(dialog.accept)
        
        dialog.setLayout(layout)
        dialog.exec()

    def set_and_execute_command(self, command: command_invoker.ICommand):
        self.command_invoker.set_command(command)
        self.command_invoker.execute_command()


    def setupShiftPage(self):
        txtShiftKey: QLineEdit = self.txtShiftKey
        pbEncode: QPushButton = self.pbShiftEncode
        pbDecode: QPushButton = self.pbShiftDecode

        pbEncode.clicked.connect(lambda: self.set_and_execute_command(CaesarShiftCommand(f"{txtShiftKey.text()}", True)))
        pbDecode.clicked.connect(lambda: self.set_and_execute_command(CaesarShiftCommand(f"{txtShiftKey.text()}", False)))

    def setupVigenerePage(self):
        txtVigenereKey: QLineEdit = self.txtVigenere
        pbEncode: QPushButton = self.pbVigenereEncode
        pbDecode: QPushButton = self.pbVigenereDecode

        pbEncode.clicked.connect(lambda: self.set_and_execute_command(VigenereCommand(f"{txtVigenereKey.text()}", True)))
        pbDecode.clicked.connect(lambda: self.set_and_execute_command(VigenereCommand(f"{txtVigenereKey.text()}", False)))

    def setupRSAPage(self):
        txtRSAKey: QLineEdit = self.txtRSAKey
        txtRSAMod: QLineEdit = self.txtRSAMod
        pbEncode: QPushButton = self.pbRSAEncode
        pbDecode: QPushButton = self.pbRSADecode

        pbEncode.clicked.connect(lambda: self.set_and_execute_command(RSACommand(f"{txtRSAKey.text()} {txtRSAMod.text()}", True)))
        pbDecode.clicked.connect(lambda: self.set_and_execute_command(RSACommand(f"{txtRSAKey.text()} {txtRSAMod.text()}", False)))

    def setupDifHel(self):
        txtDifHelMod: QLineEdit = self.txtDifHelMod
        txtDifHelGen: QLineEdit = self.txtDifHelGen
        txtDifHelPrivKey: QLineEdit = self.txtDifHelPrivKey
        txtDefHelPartnerKey: QLineEdit = self.txtDefHelPartnerKey
        pbGenerateHalfKey: QPushButton = self.pbGenerateHalfKey
        pbCalculateSecret: QPushButton = self.pbCalculateSecret
        lbMyHalfKey: QLabel = self.lbMyHalfKey
        lbSecret: QLabel = self.lbSecret

        pbGenerateHalfKey.clicked.connect(
            lambda: lbMyHalfKey.setText(
                f"Your halfkey is: {difhel_half_key(int(txtDifHelMod.text()), int(txtDifHelGen.text()), int(txtDifHelPrivKey.text()))}"
            ))
        pbCalculateSecret.clicked.connect(
            lambda: lbSecret.setText(
                f"The shared secret is: {difhel_secret(int(txtDifHelMod.text()), int(txtDifHelPrivKey.text()), int(txtDefHelPartnerKey.text()))}"
            )
        )

    def setupHash(self):
        pbHash: QPushButton = self.pbHash
        lbHash: QLabel = self.lbHash

        pbHash.clicked.connect(lambda: lbHash.setText(
            f"The hash is : {sha256(self.encoder.plain_buffer.decode("utf-32-be").encode("utf-8")).hexdigest().encode("utf-32-be").decode("utf-32-be")}"
            ))        