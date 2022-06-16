from googleapiclient.discovery import build
from google.oauth2 import service_account


SERVICE_ACCOUNT_FILE = 'credentials.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

SAMPLE_SPREADSHEET_ID = '1f-qZEX1k_3nj5cahOzntYAnvO4ignbyesVO7yuBdv_g'


def read():
    """
    Получение данных из Гугл-таблиц.
    """
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range="Лист1!A1:D51").execute()
    values = result.get('values', [])
    return values


def main():
    read()


if __name__ == '__main__':
    main()
