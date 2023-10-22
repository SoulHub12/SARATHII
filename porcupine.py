import pvporcupine

access_key = "PnNnuG2liwLvY7MgKXtLfK8HrTkC0vHC/7vz+q5Obxe7dkyuJi2A+w==" # AccessKey obtained from Picovoice Console (https://console.picovoice.ai/)

handle = pvporcupine.create(access_key=access_key, keywords=['picovoice'])

print(pvporcupine.KEYWORDS)

keyword_paths = r'C:\Users\Sagar Vasishta\Desktop\Drowsy driver\BumbleBee_en_windows_v2_2_0.ppn'

handle = pvporcupine.create(access_key=access_key,keyword_paths=keyword_paths)

def get_next_audio_frame():
    pass

while True:
    keyword_index = handle.process(get_next_audio_frame())
    if keyword_index >= 0:
        # detection event logic/callback
        pass
    handle.delete()