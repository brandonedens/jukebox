# Brandon Edens
# 2010-04-05
# Copyright (C) 2010 Brandon Edens <brandon@as220.org>
#
# This file is part of jukebox.
#
# jukebox is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# jukebox is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with jukebox. If not, see <http://www.gnu.org/licenses/>.
"""
"""

###############################################################################
## Imports
###############################################################################

from django.conf import settings
import cairo
import clutter
import math


###############################################################################
## Constants
###############################################################################

BLINK_OFF_OPACITY = 150

DEFAULT_SYMBOL_SIZE=150


###############################################################################
## Classes
###############################################################################

class Symbol(clutter.Box):

    def __init__(self, width=DEFAULT_SYMBOL_SIZE, color='solid'):
        super(Symbol, self).__init__(clutter.BinLayout(True, True))

        self.set_width(width)

        self.circle = clutter.CairoTexture(width, width)
        cr = self.circle.cairo_create()
        cr.set_operator(cairo.OPERATOR_CLEAR)
        cr.paint()
        cr.set_operator(cairo.OPERATOR_OVER)
        cr.arc(width/2, width/2, width/2, 0.0, 2*math.pi)

        if color == 'solid':
            pattern = cairo.SolidPattern(0.20, 0.20, 0.20, 0.9)
            cr.set_source(pattern)
            cr.fill_preserve()
            del pattern

        elif color == 'bubble':
            pattern = cairo.RadialGradient(width/2, width/2, 0,
                                           width/2, width/2, width/2)
            pattern.add_color_stop_rgba(0, 0.88, 0.95, 0.99, 0.1)
            pattern.add_color_stop_rgba(0.6, 0.88, 0.95, 0.99, 0.1)
            pattern.add_color_stop_rgba(0.8, 0.67, 0.83, 0.91, 0.2)
            pattern.add_color_stop_rgba(0.9, 0.5, 0.67, 0.88, 0.7)
            pattern.add_color_stop_rgba(1.0, 0.3, 0.43, 0.69, 0.8)
            cr.set_source(pattern)
            cr.fill_preserve()
            del pattern

            pattern = cairo.LinearGradient(0, 0, width, width)
            pattern.add_color_stop_rgba(0.0, 1.0, 1.0, 1.0, 0.0)
            pattern.add_color_stop_rgba(0.15, 1.0, 1.0, 1.0, 0.95)
            pattern.add_color_stop_rgba(0.3, 1.0, 1.0, 1.0, 0.0)
            pattern.add_color_stop_rgba(0.7, 1.0, 1.0, 1.0, 0.95)
            pattern.add_color_stop_rgba(1.0, 1.0, 1.0, 1.0, 0.0)
            cr.set_source(pattern)
            cr.fill()
            del pattern

        elif color == 'blue':
            pattern = cairo.RadialGradient(width/2, width/2, 0,
                                           width/2, width/2, width/2)
            pattern.add_color_stop_rgba(0, 0.22, 0.22, 0.99, 0.1)
            pattern.add_color_stop_rgba(0.6, 0.22, 0.22, 0.88, 0.1)
            pattern.add_color_stop_rgba(0.8, 0.22, 0.22, 0.67, 0.2)
            pattern.add_color_stop_rgba(0.9, 0.22, 0.22, 0.55, 0.7)
            pattern.add_color_stop_rgba(1.0, 0.22, 0.22, 0.44, 0.8)
            cr.set_source(pattern)
            cr.fill_preserve()
            del pattern


            pattern = cairo.RadialGradient(width/2, width/2, 0,
                                           width/2, width/2, width/2)
            pattern.add_color_stop_rgba(0.9, 0.22, 0.22, 0.99, 0.1)
            pattern.add_color_stop_rgba(0.8, 0.22, 0.22, 0.88, 0.1)
            pattern.add_color_stop_rgba(0.75, 0.22, 0.22, 0.67, 0.2)
            pattern.add_color_stop_rgba(0.7, 0.22, 0.22, 0.55, 0.7)
            pattern.add_color_stop_rgba(0.1, 0.22, 0.22, 0.44, 0.8)
            cr.set_source(pattern)
            cr.fill_preserve()
            del pattern

            pattern = cairo.LinearGradient(0, 0, width, width)
            pattern.add_color_stop_rgba(0.0, 0.0, 0.0, 1.0, 0.0)
            pattern.add_color_stop_rgba(0.15, 0.0, 0.0, 1.0, 0.95)
            pattern.add_color_stop_rgba(0.3, 0.0, 0.0, 1.0, 0.0)
            pattern.add_color_stop_rgba(0.7, 0.0, 0.0, 1.0, 0.95)
            pattern.add_color_stop_rgba(1.0, 0.0, 0.0, 1.0, 0.0)
            cr.set_source(pattern)
            cr.fill()
            del pattern

        elif color == 'green':
            pattern = cairo.RadialGradient(width/2, width/2, 0,
                                           width/2, width/2, width/2)
            pattern.add_color_stop_rgba(0, 0.22, 0.99, 0.22, 0.1)
            pattern.add_color_stop_rgba(0.6, 0.22, 0.88, 0.22, 0.1)
            pattern.add_color_stop_rgba(0.8, 0.22, 0.67, 0.22, 0.2)
            pattern.add_color_stop_rgba(0.9, 0.22, 0.55, 0.22, 0.7)
            pattern.add_color_stop_rgba(1.0, 0.22, 0.44, 0.22, 0.8)
            cr.set_source(pattern)
            cr.fill_preserve()
            del pattern

            pattern = cairo.RadialGradient(width/2, width/2, 0,
                                           width/2, width/2, width/2)
            pattern.add_color_stop_rgba(0.9, 0.22, 0.99, 0.22, 0.1)
            pattern.add_color_stop_rgba(0.8, 0.22, 0.88, 0.22, 0.1)
            pattern.add_color_stop_rgba(0.75, 0.22, 0.67, 0.22, 0.2)
            pattern.add_color_stop_rgba(0.7, 0.22, 0.55, 0.22, 0.7)
            pattern.add_color_stop_rgba(0.1, 0.22, 0.44, 0.22, 0.8)
            cr.set_source(pattern)
            cr.fill_preserve()
            del pattern


            pattern = cairo.LinearGradient(0, 0, width, width)
            pattern.add_color_stop_rgba(0.0, 0.0, 1.0, 0.0, 0.0)
            pattern.add_color_stop_rgba(0.15, 0.0, 1.0, 0.0, 0.95)
            pattern.add_color_stop_rgba(0.3, 0.0, 1.0, 0.0, 0.0)
            pattern.add_color_stop_rgba(0.7, 0.0, 1.0, 0.0, 0.95)
            pattern.add_color_stop_rgba(1.0, 0.0, 1.0, 0.0, 0.0)
            cr.set_source(pattern)
            cr.fill()
            del pattern

        elif color == 'red':
            pattern = cairo.RadialGradient(width/2, width/2, 0,
                                           width/2, width/2, width/2)
            pattern.add_color_stop_rgba(0, 0.99, 0.22, 0.22, 0.1)
            pattern.add_color_stop_rgba(0.6, 0.88, 0.22, 0.22, 0.1)
            pattern.add_color_stop_rgba(0.8, 0.67, 0.22, 0.22, 0.2)
            pattern.add_color_stop_rgba(0.9, 0.55, 0.22, 0.22, 0.7)
            pattern.add_color_stop_rgba(1.0, 0.44, 0.22, 0.22, 0.8)
            cr.set_source(pattern)
            cr.fill_preserve()
            del pattern


            pattern = cairo.RadialGradient(width/2, width/2, 0,
                                           width/2, width/2, width/2)
            pattern.add_color_stop_rgba(0.9, 0.99, 0.22, 0.22, 0.1)
            pattern.add_color_stop_rgba(0.8, 0.88, 0.22, 0.22, 0.1)
            pattern.add_color_stop_rgba(0.75, 0.67, 0.22, 0.22, 0.2)
            pattern.add_color_stop_rgba(0.7, 0.55, 0.22, 0.22, 0.7)
            pattern.add_color_stop_rgba(0.1, 0.44, 0.22, 0.22, 0.8)
            cr.set_source(pattern)
            cr.fill_preserve()
            del pattern

            pattern = cairo.LinearGradient(0, 0, width, width)
            pattern.add_color_stop_rgba(0.0, 1.0, 0.0, 0.0, 0.0)
            pattern.add_color_stop_rgba(0.15, 1.0, 0.0, 0.0, 0.95)
            pattern.add_color_stop_rgba(0.3, 1.0, 0.0, 0.0, 0.0)
            pattern.add_color_stop_rgba(0.7, 1.0, 0.0, 0.0, 0.95)
            pattern.add_color_stop_rgba(1.0, 1.0, 0.0, 0.0, 0.0)
            cr.set_source(pattern)
            cr.fill()
            del pattern

        del cr

        self.add(self.circle)

        # glowing timeline
        self.timeline = clutter.Timeline(duration=settings.ARROW_BLINK_RATE)
        self.timeline.set_loop(True)
        self.alpha = clutter.Alpha(self.timeline, clutter.LINEAR)
        self.blink = clutter.BehaviourOpacity(alpha=self.alpha,
                                              opacity_start=BLINK_OFF_OPACITY,
                                              opacity_end=255)
        self.timeline.connect('completed', self.on_blink_completed)

        # By default we enable blinking for arrow.
        self.blink_on()

    def blink_on(self):
        """
        """
        self.blink.apply(self)
        self.timeline.start()

    def blink_off(self):
        """
        Start blinking text.
        """
        self.timeline.stop()
        self.set_opacity(FONT_OPACITY)
        self.blink.remove(self)

    def on_blink_completed(self, timeline):
        """
        Blink completed function.
        """
        if self.timeline.get_direction() == clutter.TIMELINE_FORWARD:
            self.timeline.set_direction(clutter.TIMELINE_BACKWARD)
        else:
            self.timeline.set_direction(clutter.TIMELINE_FORWARD)

class LeftArrow(Symbol):

    def __init__(self, width=DEFAULT_SYMBOL_SIZE):
        super(LeftArrow, self).__init__(width=width, color='red')

        self.arrow = clutter.CairoTexture(width, width)
        cr = self.arrow.cairo_create()
        cr.set_source_rgba(1, 1, 1, 0.4)
        cr.move_to(width/2, width/2 - width/3)
        cr.line_to(width/9, width/2)
        cr.line_to(width/2, width/2 + width/3)
        cr.close_path()
        cr.rectangle(width/2, width/3, width/3, width/3)
        cr.fill()
        del cr
        self.add(self.arrow)

class RightArrow(Symbol):

    def __init__(self, width=DEFAULT_SYMBOL_SIZE):
        super(RightArrow, self).__init__(width=width, color='green')

        self.arrow = clutter.CairoTexture(width, width)
        cr = self.arrow.cairo_create()
        cr.set_source_rgba(1, 1, 1, 0.4)
        cr.move_to(width/2, width/2 - width/3)
        cr.line_to(width - width/9, width/2)
        cr.line_to(width/2, width/2 + width/3)
        cr.close_path()
        cr.rectangle(width/6, width/3, width/3, width/3)
        cr.fill()
        del cr
        self.add(self.arrow)

class PlaySymbol(Symbol):

    def __init__(self, width=DEFAULT_SYMBOL_SIZE):
        super(PlaySymbol, self).__init__(width=width, color='blue')

        self.box = clutter.Box(clutter.BinLayout(clutter.BIN_ALIGNMENT_CENTER,
                                                 clutter.BIN_ALIGNMENT_CENTER))
        self.play = clutter.Text('Router Ultra Bold 25', 'PLAY')
        self.play.set_color(clutter.Color(255, 255, 255, 102))
        self.box.add(self.play)
        self.add(self.box)

