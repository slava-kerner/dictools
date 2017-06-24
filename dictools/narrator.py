import os
# import csv
import gtts
from tqdm import tqdm
from pydub import AudioSegment


class Narrator:
    def __init__(self, config=None):
        self.config = config or self.default_config

    def narrate(self, dic, output_path):
        slow = self.config.get('slow', False)
        verbose = self.config.get('verbose', False)

        os.makedirs(os.path.abspath(os.path.join(output_path, os.pardir)), exist_ok=True)
        with open(output_path, 'wb') as fi:
            for pair in tqdm(dic, desc='narrating', disable=not verbose):
                gtts.gTTS(text=pair[0], lang=dic.lng_src, slow=slow).write_to_fp(fi)
                gtts.gTTS(text=pair[1], lang=dic.lng_dst, slow=slow).write_to_fp(fi)

    @property
    def default_config(self):
        config = {
            'slow': False,
            'verbose': True,
        }
        return config
