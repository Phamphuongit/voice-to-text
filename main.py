import unittest
import time
from app_connect import App_Connect
from key_word import *
from play_wav_file import *
import os
from ggsheet_write_text import *
from get_file_name import *

OS = "ios"

WAIT_SECONDS = 0.9
FOLDER = "./wav-data"

if OS == "android":
    START_XPATH = '//android.view.View[contains(@content-desc, "Nói để tạo đơn")]'
    INPUT_WIDGET_XPATH = "//android.widget.EditText"
else:
    START_XPATH = '//XCUIElementTypeOther[contains(@name, "Nói để tạo đơn")]'
    INPUT_WIDGET_XPATH = '//XCUIElementTypeTextField'

files = os.listdir(FOLDER)

class TestAppium(unittest.TestCase):
    def test_voice_to_text(self):
        for file in files:
            with self.subTest(file=file):
                id = get_file_id(file)
                print(f"{id}🆔🆔🆔🆔🆔🆔🆔🆔🆔🆔🆔🆔🆔🆔🆔🆔🆔🆔🆔🆔🆔🆔")
                if id == "Store":
                    pass
                else:
                    try:
                        wav_path = f"./wav-data/{file}"
                        connection = App_Connect(os=OS)
                        connection.open_app()
                        wait = connection.wait()
                        start_button = get_element(START_XPATH, wait=wait)
                        click_element(start_button, print_text="Recording start 🎤🎤🎤🎤🎤🎤🎤🎤🎤🎤🎤🎤🎤🎤🎤🎤🎤🎤")
                        play_audio(wav_path)
                        time.sleep(WAIT_SECONDS)
                        input_element = get_element(INPUT_WIDGET_XPATH, wait=wait)
                        click_element(input_element, print_text="Get Text 📢📢📢📢📢📢📢📢📢📢📢📢📢📢📢📢📢📢📢📢📢")
                        text_regconation = get_text(input_element, wait=wait)
                        write_text(id, f"{text_regconation}")
                        print("✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅")
                    except Exception as error:
                        print(f"{error}❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌")
                    finally:
                        time.sleep(5)
                        connection.terminate_app()
                        connection.teardown()

unittest.main()
