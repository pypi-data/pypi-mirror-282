"""Módulo que contiene la clase EmailDeliverySistem que se encarga de crear un registro de correo electrónico para ser enviado por Appsheet"""
from src.roche_datachapter_lib.google_services import GoogleServices

class EmailDeliverySystem():

    @classmethod
    def create_email_record(cls, to, subject, body, attachment, attachment_name, appsheet_mails_folder_id):
        """Crea un registro de correo electrónico para ser enviado por Appsheet"""
        folder_name = GoogleServices.get_file_name_by_file_id(appsheet_mails_folder_id)
        return [{
            "destinatario/s": to,
            "asunto": subject,
            "cuerpo": body,
            "file": f"{folder_name}/{attachment}",
            "tabla": attachment_name
        }]
