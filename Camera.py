import cv2
import Folder
import config


class Cam:
    def __init__(self):
        self.do_break = 0
        self.usb_path = config.usb_path

    def break_cam(self):
        self.do_break = 1

    def repair_cam(self):
        self.do_break = 0

    def capture_video_to_file(self, path):
        cap = cv2.VideoCapture(0)

        frame_width = int(cap.get(3))
        frame_height = int(cap.get(4))
        frame_rate = float(cap.get(5))

        cap.set(cv2.CAP_PROP_FPS, frame_rate)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

        out = cv2.VideoWriter(path + ".mp4", cv2.VideoWriter_fourcc(*'mp4v'), frame_rate,
                              (frame_width, frame_height))

        #out.set(cv2.CAP_PROP_FPS, frame_rate)

        # Try block while saving everything to the file so that it can release the resources.
        try:
            while cap.isOpened() and Folder.does_folder_exist(self.usb_path):
                ret, frame = cap.read()

                if ret is True:
                    flipped_frame = cv2.flip(frame, 1)
                    out.write(flipped_frame)

                if self.do_break == 1:
                    break

            out.release()
            cap.release()
            cv2.destroyAllWindows()
            Folder.rename_folder(path)

        except KeyboardInterrupt:
            out.release()
            cap.release()
            cv2.destroyAllWindows()
            Folder.rename_folder(path)
            quit()


camcorder = Cam()
