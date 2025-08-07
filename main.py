import unittest
import time
from app_connect import App_Connect
from key_word import *
from play_wav_file import *
import os
from ggsheet_write_text import *
from get_file_name import *

START_XPATH = '//android.view.View[contains(@content-desc, "Nói để tạo đơn")]'
INPUT_WIDGET_XPATH = "//android.widget.EditText"
WAIT_SECONDS = 3
FOLDER = "./wav-data"

files = os.listdir(FOLDER)

connection = App_Connect()

class TestAppium(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        connection.teardown()

    def test_voice_to_text(self):
        for file in files:
            try:
                id = get_file_id(file)
                wav_path = f"./wav-data/{file}"
                connection.open_app()
                wait = connection.wait()
                click_element(START_XPATH, wait=wait, print_text="Recording start 🎬")
                play_audio(wav_path)
                time.sleep(WAIT_SECONDS)
                click_element(INPUT_WIDGET_XPATH, wait=wait, print_text="Get Text_______")
            except Exception as error:
                print(error)
            else:
                text_regconation = get_text(INPUT_WIDGET_XPATH, wait=wait)
                write_text(id, f"{id} {text_regconation}")
            finally:
                connection.terminate_app()

unittest.main()
