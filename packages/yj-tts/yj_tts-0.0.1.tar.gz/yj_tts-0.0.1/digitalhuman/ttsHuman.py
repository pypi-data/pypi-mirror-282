import datetime
import os
import uuid

import edge_tts
import soundfile as sf

from utils.common import is_dir_exists

file_separator = os.sep




class HumanTTS:
    def __init__(self, path):
        self.savePath = path

    def generate_speech(self, msg, voice_name,file_name):
        communicate = edge_tts.Communicate(msg, voice_name)
        current_date = datetime.datetime.today().date()
        tmp_file = self.savePath + file_separator + str(uuid.uuid4()) + ".wav"
        parent_path = self.savePath + file_separator + current_date.strftime("%Y%m%d")
        save_file = parent_path + file_separator + file_name + ".wav"
        # 如果文件已经存在，直接返回
        if os.path.exists(save_file):
            return os.path.abspath(save_file)

        print(tmp_file)
        communicate.save_sync(tmp_file)
        try:
            if not is_dir_exists(parent_path):
                try:
                    os.mkdir(parent_path)
                    print(f"文件目录 {parent_path} 不存在，已创建。")
                except OSError as e:
                    print(f"文件目录失败: {e}")

            with sf.SoundFile(tmp_file) as sound_file:
                data = sound_file.read(dtype='float32')
            sf.write(save_file, data, sound_file.samplerate)
            # 删除临时文件
            self.delete_file(tmp_file)
            return os.path.abspath(save_file)
        except OSError as e:
            print(f"文件转换失败，删除临时文件: {e}")
            self.delete_file(tmp_file)

    # 删除文件
    def delete_file(self, file):
        try:
            os.remove(file)
            print(f"文件 {file} 已被删除。")
        except OSError as e:
            print(f"文件删除失败: {e}")
