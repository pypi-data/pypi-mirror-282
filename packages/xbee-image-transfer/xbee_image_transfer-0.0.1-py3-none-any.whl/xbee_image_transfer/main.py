from digi.xbee.devices import XBeeDevice, RemoteXBeeDevice, XBee64BitAddress
from sys import getsizeof
from math import ceil
from os.path import join, exists
from os import remove, mkdir
from hashlib import md5
from time import sleep
from PIL import Image
from datetime import datetime as dt


class XBeeImageTransfer:
    def __init__(self, port, chunk_size, ack_time):
        self.CHUNK_SIZE = chunk_size
        self.PORT = port
        self.ACK_TIMEOUT = ack_time
        self.FILENAME_FORMAT = ["data_%s.jpg", "%Y-%m-%d_%H-%M-%S"]

        self.DEST_ADD = None
        self.SRC_IMAGE_FOLDER = None
        self.DEST_IMAGE_FOLDER = None

        self.device = XBeeDevice(self.PORT, 9600)
        self.device.open()

    @classmethod
    def send_init(cls, port, dest_add, src_image_folder="images_src", chunk_size=250, ack_time=3):
        instance = cls(port, chunk_size, ack_time)
        instance.DEST_ADD = dest_add  # "0013A20041E56CE1"
        instance.SRC_IMAGE_FOLDER = src_image_folder
        instance.remote = RemoteXBeeDevice(instance.device, XBee64BitAddress.from_hex_string(instance.DEST_ADD))
        instance.create_missing_dirs()
        return instance

    @classmethod
    def receive_init(cls, port, dest_image_folder="images_dest", chunk_size=250, ack_time=3):
        instance = cls(port, chunk_size, ack_time)
        instance.DEST_IMAGE_FOLDER = dest_image_folder
        instance.create_missing_dirs()
        return instance

    @classmethod
    def general_init(cls, port, dest_add, src_image_folder="images_src", dest_image_folder="images_dest", chunk_size=250, ack_time=3):
        instance = cls(port, chunk_size, ack_time)
        instance.DEST_ADD = dest_add  # "0013A20041E56CE1"
        instance.SRC_IMAGE_FOLDER = src_image_folder
        instance.remote = RemoteXBeeDevice(instance.device, XBee64BitAddress.from_hex_string(instance.DEST_ADD))
        instance.DEST_IMAGE_FOLDER = dest_image_folder
        instance.create_missing_dirs()
        return instance

    def create_missing_dirs(self):
        for i in [self.SRC_IMAGE_FOLDER, self.DEST_IMAGE_FOLDER]:
            if i and not exists(i):
                mkdir(i)

    def send(self, image_file):
        try:
            compressed_img = self.compress_image(join(self.SRC_IMAGE_FOLDER, image_file))
            with open(compressed_img, 'rb') as infile:
                print(infile.name)
                file_content = infile.read()
                total_chunks = ceil(getsizeof(file_content) / self.CHUNK_SIZE)
                hash = md5(file_content).hexdigest()
                self.display("Data: %d %s" % (total_chunks, hash))

                i = 0
                infile.seek(0)
                while True:
                    chunk = infile.read(self.CHUNK_SIZE)
                    if not chunk:
                        self.device.send_data_async(self.remote, "END OF FILE - %d - %s" % (total_chunks, hash))
                        break
                    i += 1
                    print(getsizeof(chunk), i, getsizeof(infile))
                    self.device.send_data(self.remote, chunk)
                    self.variable_time_delay(i)
            try:
                xbee_message = self.device.read_data(self.ACK_TIMEOUT)
                if xbee_message.data.decode() == "RECEIVED":
                    self.display("File sent successfully")
            except Exception as e:
                print(e)
                self.display("Something went wrong! Retrying...")
                self.device.send_data(self.remote, "ERROR")
                self.send()

        except KeyboardInterrupt:
            self.display("PROGRAM TERMINATED")

        finally:
            if exists(compressed_img):
                remove(compressed_img)
            self.device.close()

    def receive(self):
        try:
            self.temp_file = self.open_file()
            self.i = 0

            def data_receive_callback(xbee_message):
                try:
                    if xbee_message.data.decode() == "ERROR":
                        self.display("ERROR")
                        self.temp_file = self.open_file(self.temp_file)
                        self.i = 0
                        return
                    end_packet = xbee_message.data.decode().split(" - ")
                    total_chunks = int(end_packet[1])
                    hash = end_packet[2]
                    if total_chunks == self.i and self.check_file(self.temp_file, hash):
                        self.display("File received successfully")
                        remote = xbee_message.remote_device
                        self.device.send_data(remote, "RECEIVED")
                    self.temp_file = self.open_file(self.temp_file)
                    self.i = 0
                except Exception as e:
                    self.i += 1
                    print("Into %s - %d - %d" % (self.temp_file.name, getsizeof(xbee_message.data), self.i))
                    self.temp_file.write(xbee_message.data)

            self.device.add_data_received_callback(data_receive_callback)
            self.display("WAITING FOR A FILE")
            input()

        except KeyboardInterrupt:
            self.display("PROGRAM TERMINATED")

        finally:
            if self.device is not None and self.device.is_open():
                file_to_be_deleted = self.temp_file.name
                self.temp_file.close()
                remove(file_to_be_deleted)
                self.device.close()

    def open_file(self, f=None):
        if f is not None:
            f.close()
        curr_time = dt.now()
        file_name = self.FILENAME_FORMAT[0] % curr_time.strftime(self.FILENAME_FORMAT[1])
        file = open(join(self.DEST_IMAGE_FOLDER, file_name), "wb+")
        return file

    @staticmethod
    def display(content, padding=16):
        content = str(content)
        l = len(content) + padding
        before = "+" + "-" * l + "+"
        middle = "|" + content.center(l) + "|"
        after = "+" + "-" * l + "+"
        print("\n%s\n%s\n%s" % (before, middle, after))

    @staticmethod
    def check_file(file, original_hash):
        file.seek(0)
        file_content = file.read()
        received_hash = md5(file_content).hexdigest()
        return original_hash == received_hash

    @staticmethod
    def variable_time_delay(i):
        if not i % 100:
            sleep(2)
        elif not i % 50:
            sleep(1)
        elif not i % 10:
            sleep(0.5)
        else:
            sleep(0.3)

    @staticmethod
    def compress_image(filepath, quality=50):
        filename = filepath.split(".")[0]
        picture = Image.open(filepath)
        picture.save(filename + "_compressed.jpg",
                     "JPEG",
                     optimize=True,
                     quality=quality)
        return filename + "_compressed.jpg"
