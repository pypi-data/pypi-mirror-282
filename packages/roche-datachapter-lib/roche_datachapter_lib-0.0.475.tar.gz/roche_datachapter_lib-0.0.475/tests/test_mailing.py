"""Test module for mailing module."""
import pandas as pd
import os
from roche_datachapter_lib.db_config import DB_CONFIG
from roche_datachapter_lib.result_type import ResultType
from roche_datachapter_lib.google_services import GoogleServices
from roche_datachapter_lib.email_service import EmailDeliverySystem
from roche_datachapter_lib.excel_generator import ExcelGenerator
from roche_datachapter_lib.appsheet_service import AppsheetService

query="SELECT * FROM gtm_latam_arg.stg_oceo.oceo_omuser_latest"
bind="rdi_latam_ar"
df = DB_CONFIG.execute_custom_select_query(
            query, bind, result_set_as=ResultType.PANDAS_DATA_FRAME)
df['bookmark_dts'] = pd.to_datetime(df['bookmark_dts']).dt.strftime('%Y-%m-%d')
df['load_dts'] = pd.to_datetime(df['load_dts']).dt.strftime('%Y-%m-%d')

file_name='prueba_roche_datachapter_lib.xlsx'
destinatario='lucas.frias@roche.com, uciel.bustamante@contractors.roche.com'
subject='Test email from roche_datachapter_lib'
body='Esto es una prueba de envío de email desde roche_datachapter_lib'
data_source_name ='Usuarios RDI'
mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
appsheet_mails_folder_id='1RMviKkcw5XGgfjgVOcWxke-IvQZfNjjW'
tabla_appsheet='Mails'

app_id = os.getenv('MAILING_APPLICATION_ID')
access_key = os.getenv('MAILING_APPLICATION_ACCESS_KEY')

file_path=ExcelGenerator.get_file_path(file_name)
ExcelGenerator.generate_excel(df, file_path)
file_id=GoogleServices.upload_file_to_drive(file_path, file_name, appsheet_mails_folder_id, mimetype)
file_name_modified=GoogleServices.get_file_name_by_file_id(file_id)
email_record=EmailDeliverySystem.create_email_record(destinatario, subject, body, file_name_modified, data_source_name, appsheet_mails_folder_id)
AppsheetService = AppsheetService(app_id, access_key)
AppsheetService.add_registers_to_table(email_record, tabla_appsheet)