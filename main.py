import threading
import time
from Camera import camcorder
import Folder
import config


class App:
    def __init__(self):
        self.usb_path = config.usb_path

    def cut_video(self, cut_time):
        print(cut_time)
        time.sleep(cut_time)
        camcorder.break_cam()

    def run(self):
        counter = 0
        while counter < 2:
            folder_name = Folder.generate_folder_name()
            Folder.create_folder(folder_name)

            file_name = Folder.generate_file_name()
            cut_time = Folder.calculate_record_time(file_name)

            wait_thread = threading.Thread(target=self.cut_video, daemon=True, args=[cut_time])
            wait_thread.start()

            try:
                camcorder.capture_video_to_file(Folder.return_whole_file_path(folder_name, file_name))
                wait_thread.join()
            except KeyboardInterrupt:
                quit()

            camcorder.repair_cam()
            counter += 1


app = App()
app.run()
