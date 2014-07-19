#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#     Copyright (C) 2012 Tristan Fischer (sphere@dersphere.de)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#

from xbmcswift2 import Plugin, xbmc

STATIC_STREAMS = (
    {
        'title': 'ISS Live Stream',
        'logo': 'stream_iss.png',
        'stream_url': ('http://sjc-uhls-proxy.ustream.tv/watch/'
                       'playlist.m3u8?cid=9408562'),
    }, {
         'title': 'ISS HD Earth Viewing Experiment',
         'logo': 'stream_iss.png',
         'stream_url': ('http://sjc-uhls-proxy.ustream.tv/watch/'
                        'playlist.m3u8?cid=17074538'),
    }, {
        'title': 'NASA TV: Public Channel',
        'logo': 'stream_public.png',
        'stream_url': ('http://public.infozen.cshls.lldns.net/infozen/public/'
                       'public/public_1000.m3u8'),
    }, {
        'title': 'NASA TV: Educational Channel',
        'logo': 'stream_education.png',
        'stream_url': ('http://edu.infozen.cshls.lldns.net/infozen/edu/'
                       'edu/edu_1000.m3u8'),
    }, {
        'title': 'NASA TV: Media Channel',
        'logo': 'stream_media.png',
        'stream_url': ('http://media.infozen.cshls.lldns.net/infozen/media/'
                       'media/media_1000.m3u8'),
    },
)

YOUTUBE_CHANNELS = (  
    {
        'name': 'NASA Main Channel',
        'logo': 'yt_main.png',
        'user': 'NASAtelevision',
    }, {
        'name': 'NASA Jet Propulsion Laboratory',
        'logo': 'yt_jpl.png',
        'user': 'JPLnews',
    }, {
        'name': 'NASA Kennedy Space Center',
        'logo': 'yt_ksc.png',
        'user': 'NASAKennedy',
    }, {
        'name': 'NASA Science Casts',
        'logo': 'yt_science_casts.jpg',
        'user': 'ScienceAtNASA',
    }, {
        'name': 'NASA Langley Research Center',
        'logo': 'yt_langley.png',
        'user': 'NASALANGLEY',
    }, {
        'name': 'NASA Goddard',
        'logo': 'yt_goddard.png',
        'user': 'NASAexplorer',
    }, {
        'name': 'NASA Marshall Center',
        'logo': 'yt_marshell.png',
        'user': 'NASAMarshallTV',
    }, {
        'name': 'NASA AMES Research Center',
        'logo': 'yt_ames.png',
        'user': 'nasaames',
    }, {
        'name': 'NASA ISS',
        'logo': 'yt_iss.png',
        'user': 'ReelNASA',
    }, {
        'name': 'NASA Inside ISS',
        'logo': 'yt_insideiss.png',
        'user': 'insideISS',
    }, {
        'name': 'NASA Armstrong Flight Research Center',
        'logo': 'yt_afrc.png',
        'user': 'DrydenTV',
    }, {
        'name': 'NASA X',
        'logo': 'yt_nasax.jpg',
        'user': 'NASAXrocks',
    }, {
        'name': 'Hubble Space Telescope',
        'logo': 'yt_hubble.png',
        'user': 'HubbleSiteChannel',
    },
)

YOUTUBE_URL = (
    'plugin://plugin.video.youtube/?'
    'path=/root&feed=uploads&channel=%s'
)

plugin = Plugin()


@plugin.route('/')
def show_root_menu():
    items = [
        {'label': 'NASA Livestreams',
         'path': plugin.url_for('show_streams'),
         'thumbnail': get_logo('root_livestream.png')},
        {'label': 'NASA YouTube Archives',
         'path': plugin.url_for('show_channels'),
         'thumbnail': get_logo('root_youtube.png')},
    ]
    return plugin.finish(items)


@plugin.route('/streams/')
def show_streams():
    items = [{
        'label': stream['title'],
        'thumbnail': get_logo(stream['logo']),
        'path': stream['stream_url'],
        'is_playable': True,
    } for stream in STATIC_STREAMS]
    return plugin.finish(items)


@plugin.route('/channels/')
def show_channels():
    items = [{
        'label': channel['name'],
        'thumbnail': get_logo(channel['logo']),
        'path': YOUTUBE_URL % channel['user'],
    } for channel in YOUTUBE_CHANNELS]
    return plugin.finish(items)

def get_logo(logo):
    addon_id = plugin._addon.getAddonInfo('id')
    return 'special://home/addons/%s/resources/media/%s' % (addon_id, logo)

def log(text):
    plugin.log.info(text)

if __name__ == '__main__':
    plugin.run()
