import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

spreadsheet = client.open("voice-to-text")
worksheet = spreadsheet.worksheet("Voice1")  # ví dụ "Trang tính1"

def write_text(id, text):
    cell = worksheet.find(id)
    worksheet.update(f"C{cell.row}", [[text]])
    print("Overwriting_____________")
