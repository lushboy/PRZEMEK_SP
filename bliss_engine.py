#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:
#     Mateusz Kruszyński <mateusz.kruszynski@gmail.com>
#
import os.path, sys, time, os
from gui.ugm import ugm_helper
from logic import logic_logging as logger
LOGGER = logger.get_logger("bliss_engine", "info")
from collections import namedtuple

BlissImage = namedtuple('BlissImage', ['image', 'word'])

IMAGE_DIR = '/home/administrator/PRZEMEK_SP_N'

BLISS_IMAGES = [
	BlissImage('OBRAZKI/star.gif', u'gwiazdka'),
	BlissImage('OBRAZKI/heart.jpeg', u'serduszko'),
	BlissImage('OBRAZKI/blue.jpg', u'ptaszysko'),
	BlissImage('OBRAZKI/jesus.gif', u'Jezus'),
	BlissImage('OBRAZKI/rose.jpg', u'róża'),
	BlissImage('OBRAZKI/frog.jpg', u'żaba'),
	BlissImage('OBRAZKI/Jerry.jpeg', u'myszszsz'),
	BlissImage('OBRAZKI/Tigger.jpg', u'tygrysek'),
BlissImage('OBRAZKI/scooby.jpeg', u'scooby'),
BlissImage('OBRAZKI/yellow.jpeg', u'wielki ptak'),
BlissImage('OBRAZKI/dino.jpeg', u'dino'),
BlissImage('OBRAZKI/jesus.gif', u'Jezus'),
	BlissImage('OBRAZKI/rose.jpg', u'róża'),
	BlissImage('OBRAZKI/frog.jpg', u'żaba'),
	BlissImage('OBRAZKI/Jerry.jpeg', u'myszszsz'),
	BlissImage('OBRAZKI/Tigger.jpg', u'tygrysek')
]

PAGE_SIZE = 8
	

class BlissEngine(object):
    def __init__(self, configs):
        self._message = ""
        self.text_id = int(configs["ugm_text_id"])
        self.text_ids = [int(i) for i in configs["ugm_text_ids"].split(';')]
        self.image_ids = [int(i) for i in configs["ugm_image_ids"].split(';')]

        self.current_page = 0

    # --------------------------------------------------------------------------
    # ------------------ actions available in config ---------------------------
    def backspace(self):
		LOGGER.info("UPDATE MESSAGE: "+self._message)
		l_config = [{'id':7777, 'image_path':'/home/administrator/PRZEMEK_SP_N/OBRAZKI/smiley-star-clipart.gif'}]
		l_str_config = str(l_config)
		LOGGER.info("UPDATE: "+l_str_config)
		ugm_helper.send_config(self.conn, l_str_config, 1)

    def say(self, msg=None):
        """Run say action -> run external program with self._message
        as a paramtere.
        A place where this action is defined to be fired
        is speller config file.
        """
        if not msg:
            msg = self._message
        LOGGER.info("TRYING TO SAY: "+msg)
        self.run_ext(u''.join(
                [#u'milena_say ', msg, u" &"
                    u'echo "', msg,'" | ',
                    "festival --tts",
                    " &"
                 ]))

    def msg(self, p_message):
        """Update stored message."""
        self._message = u''.join([self._message, p_message])

    def clear(self):
        """Update stored message as empty
        """
        self._message = u''

    def close_dasher(self):
        self._message = os.popen('xsel -b').read().decode('utf-8')
        os.system('killall dasher')

	def send_image(self):
		LOGGER.info("UPDATE MESSAGE: "+self._message)
		
		l_str_config = str(l_config)
		LOGGER.info("UPDATE: "+l_str_config)
		ugm_helper.send_config(self.conn, l_str_config, 1)
		
    def _update_letters(self):
        """Sent to self._server current logic data:
        - current message,
        """
        LOGGER.info("UPDATE MESSAGE: "+self._message)
        l_config = []

        l_letters = self._compute_current_letters()
        for i, i_letters in enumerate(l_letters):
            l_conf = {'id':self.text_ids[i],
                      'message':i_letters}
            l_config.append(l_conf)
        l_config.append({'id':self.text_id,
                         'message':self._message})
        l_str_config = str(l_config)
        LOGGER.info("UPDATE: "+l_str_config)
        ugm_helper.send_config(self.conn, l_str_config, 1)


    def _update_images(self):
        """Sent to self._server current logic data:
        - current message,
        """
        LOGGER.info("UPDATE MESSAGE: "+self._message)
        l_config = []
        for i in range(PAGE_SIZE):
            rel_path = BLISS_IMAGES[self.current_page * PAGE_SIZE + i].image
            full_path = os.path.join(IMAGE_DIR, rel_path)
            LOGGER.info("image path:" + full_path)
            l_config.append({
                    'id' : self.image_ids[i],
                    'image_path' : full_path
            })
        
        l_str_config = str(l_config)
        LOGGER.info("UPDATE IMAGES: "+l_str_config)
        ugm_helper.send_config(self.conn, l_str_config, 1)
            

    def _compute_current_letters(self):    
        """Return collection of strings representing current`s state graphics. 
        See _compute_current_param for details.
        """
        return self._compute_current_param('letters', 'letters_solver')

        
