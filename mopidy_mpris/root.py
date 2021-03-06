"""Implementation of org.mpris.MediaPlayer2 interface.

https://specifications.freedesktop.org/mpris-spec/2.2/Media_Player.html
"""

from __future__ import unicode_literals

import logging
import os

from mopidy_mpris.interface import Interface


logger = logging.getLogger(__name__)


class Root(Interface):
    """
    <node>
      <interface name="org.mpris.MediaPlayer2">
        <method name="Raise"/>
        <method name="Quit"/>
        <property name="CanQuit" type="b" access="read"/>
        <property name="CanRaise" type="b" access="read"/>
        <property name="Fullscreen" type="b" access="readwrite"/>
        <property name="CanSetFullscreen" type="b" access="read"/>
        <property name="HasTrackList" type="b" access="read"/>
        <property name="Identity" type="s" access="read"/>
        <property name="DesktopEntry" type="s" access="read"/>
        <property name="SupportedUriSchemes" type="as" access="read"/>
        <property name="SupportedMimeTypes" type="as" access="read"/>
      </interface>
    </node>
    """

    INTERFACE = 'org.mpris.MediaPlayer2'

    def Raise(self):
        logger.debug('%s.Raise called', self.INTERFACE)
        # Do nothing, as we do not have a GUI

    def Quit(self):
        logger.debug('%s.Quit called', self.INTERFACE)
        # Do nothing, as we do not allow MPRIS clients to shut down Mopidy

    CanQuit = False

    @property
    def Fullscreen(self):
        return False

    @Fullscreen.setter
    def Fullscreen(self, value):
        pass

    CanSetFullscreen = False
    CanRaise = False
    HasTrackList = False  # NOTE Change if adding optional track list support
    Identity = 'Mopidy'

    @property
    def DesktopEntry(self):
        return os.path.splitext(os.path.basename(
            self.config['mpris']['desktop_file']))[0]

    @property
    def SupportedUriSchemes(self):
        return self.core.get_uri_schemes().get()

    # NOTE Return MIME types supported by local backend if support for
    # reporting supported MIME types is added.
    SupportedMimeTypes = [
        'audio/mpeg',
        'audio/x-ms-wma',
        'audio/x-ms-asf',
        'audio/x-flac',
        'audio/flac',
        'audio/l16;channels=2;rate=44100',
        'audio/l16;rate=44100;channels=2',
    ]
