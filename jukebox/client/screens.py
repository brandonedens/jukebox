# Brandon Edens
# 2010-02-06
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
from pango import ALIGN_CENTER
import clutter
import logging


###############################################################################
## Constants
###############################################################################

FONT_COLOR = clutter.Color(200, 200, 200)
FONT_HIGHLIGHT_COLOR = clutter.Color(255, 170, 170)
FONT_OPACITY = 80


###############################################################################
## Classes
###############################################################################

class Screen(clutter.Box):

    def __init__(self, layout_manager):
        super(Screen, self).__init__(layout_manager)
        self.set_size(settings.SCREEN_WIDTH,
                      settings.SCREEN_HEIGHT)
        self.desired_x = 0

        # Set variables that relate to all screens.
        self.header = None
        self.footer = None

    def set_x(self, value):
        super(Screen, self).set_x(value)
        self.desired_x = value

    def slide_left(self):
        self.desired_x -= self.get_width()
        animation = self.animate(clutter.LINEAR, settings.SCREEN_SLIDE_RATE,
                                 'x', self.desired_x)

    def slide_right(self):
        self.desired_x += self.get_width()
        animation = self.animate(clutter.LINEAR, settings.SCREEN_SLIDE_RATE,
                                 'x', self.desired_x)

    def get_selected(self):
        """
        Returns the currently selected item.
        """
        logging.warning("Get selected called on generic Screen object.")
        return None

    def on_press(self, actor, event):
        """
        Callback for key presses.
        """
        logging.warning("on_press called for generic Screen.")

    def on_second(self):
        """
        Callback that is called each second.
        """
        pass

    def update(self):
        """
        Update the contents of oneself.
        """
        self.header.update()

class ScreenContainer(clutter.Box):
    """
    A container for screens.
    """

    def __init__(self):
        """
        Initialize the screen container.
        """
        super(ScreenContainer, self).__init__(clutter.FixedLayout())

        # Setup screens.
        self.screens = []
        self.active_screen = None

    def add_screen(self, screen, offscreen=None):
        """
        Add a screen to the current list of screens.
        """
        self.screens.append(screen)
        self.add(screen)
        if offscreen == 'right':
            screen.set_x(settings.SCREEN_WIDTH)
        elif offscreen == 'left':
            screen.set_x(-settings.SCREEN_WIDTH)
        else:
            screen.set_position(0, 0)
        return screen

    def clear_screens(self, current_screen):
        """
        Removes all screens stored in the screens array after the
        current_screen.
        """
        while self.screens[-1] != current_screen:
            # Pop a screen off the stack.
            screen = self.screens.pop()
            logging.debug("Clearing screen %s." % screen)
            # Remove the screen from the box.
            self.remove(screen)

    def new_screen(self, new_screen):
        """
        Add a screen to the current list of screens slide that screen to the
        foreground.

        If the new_screen already exists in the list of screens then simply
        activate the existing version of that screen.
        """
        current_screen_index = self.screens.index(self.active_screen)
        next_screen = None
        try:
            next_screen = self.screens[current_screen_index + 1]
        except IndexError:
            pass

        if next_screen and next_screen.get_name() == new_screen.get_name():
            # We have existing screen so simply use that one.
            self.active_screen.slide_left()
            self.active_screen = next_screen
            self.active_screen.slide_left()
        else:
            self.clear_screens(self.active_screen)
            self.active_screen.slide_left()
            self.active_screen = self.add_screen(new_screen, 'right')
            self.active_screen.slide_left()

    def on_press(self, actor, event):
        """
        Pass keypresses off to the active screen.
        """
        self.active_screen.on_press(actor, event)

    def on_second(self):
        """
        One second tick.
        """
        self.active_screen.on_second()

    def remove_screen(self, screen):
        """
        Remove a screen which really means sliding the current screen out of
        the way moving the virtual camera to the left. We leave the previous
        screen in the screen's list in case the user immediately wants to
        return to that screen.
        """
        self.active_screen.slide_right()
        self.active_screen = self.screens[self.screens.index(screen) - 1]
        self.active_screen.slide_right()

    def update_screens(self):
        """
        Iterate over screens asking them to update their contents.

        This functionality is used to update credits information.
        """
        for screen in self.screens():
            screen.update()

class BlinkingText(clutter.Text):
    """
    """

    def __init__(self, obj):
        super(BlinkingText, self).__init__(
            settings.SCROLLING_TEXT_FONT, obj.__str__()
            )
        self.obj = obj

        # Setup text attributes
        self.set_color(FONT_COLOR)
        self.set_opacity(FONT_OPACITY)
        self.set_property('scale-gravity', clutter.GRAVITY_CENTER)
        self.set_line_alignment(ALIGN_CENTER)
        self.set_line_wrap(True)

        # Setup blinking timeline.
        self.timeline = clutter.Timeline(duration=settings.BLINKING_TEXT_RATE)
        self.timeline.set_loop(True)
        self.alpha = clutter.Alpha(self.timeline, clutter.LINEAR)
        self.blink = clutter.BehaviourOpacity(alpha=self.alpha,
                                              opacity_start=FONT_OPACITY,
                                              opacity_end=255)
        self.timeline.connect('completed', self.on_blink_completed)

    def blink_on(self):
        """
        Start blinking text.
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

    def highlight(self):
        """
        """
        self.animate(clutter.LINEAR, settings.HIGHLIGHT_RATE,
                     "scale-x", 1.3,
                     "scale-y", 1.3,
                     'color', FONT_HIGHLIGHT_COLOR,
                     )

    def unhighlight(self):
        """
        """
        self.animate(clutter.LINEAR, settings.HIGHLIGHT_RATE,
                     "scale-x", 1,
                     "scale-y", 1,
                     'color', FONT_COLOR,
                     )

class ScrollingText(clutter.Box):

    def __init__(self, contents, items_on_screen=8):
        """
        """
        super(ScrollingText, self).__init__(clutter.BoxLayout())

        layout = self.get_layout_manager()
        layout.set_vertical(True)
        layout.set_spacing(20)
        layout.set_use_animations(True)

        # Contents stores the possible on screen elements.
        self.contents = contents
        # Set selected item to None
        self.selected = contents[0]

        for item in self.contents[:items_on_screen]:
            layout.pack(item, True, False, False,
                        clutter.BOX_ALIGNMENT_CENTER,
                        clutter.BOX_ALIGNMENT_CENTER)
        self.selected = contents[0]
        self.selected.highlight()
        self.selected.blink_on()

    def on_press(self, actor, event):
        """
        """
        if event.keyval == clutter.keysyms.Up:
            children = self.get_children()
            index = children.index(self.selected)
            self.selected.unhighlight()
            self.selected.blink_off()
            if index == 0:
                if len(children) < len(self.contents):
                    # We have less on screen elements then we have contents so
                    # we are at the top of the displayed list and we need to
                    # add an object from earlier in the list.
                    layout = self.get_layout_manager()
                    obj = self.contents[self.contents.index(children[0]) - 1]
                    self.selected = obj
                    layout.pack(obj, True, False, False,
                                clutter.BOX_ALIGNMENT_CENTER,
                                clutter.BOX_ALIGNMENT_CENTER)
                    self.lower_child(obj, None)
                    self.remove(children[-1])
                else:
                    # We have the same number of on screen elements (children)
                    # as we have in our contents so we're just going to switch
                    # the selected element to the bottom-most displayed child.
                    self.selected = children[-1]
            else:
                # Not at the top of the list so just change selected to the
                # previous child.
                self.selected = children[index - 1]
            self.selected.blink_on()
            self.selected.highlight()

        elif event.keyval == clutter.keysyms.Down:
            children = self.get_children()
            index = children.index(self.selected)

            self.selected.unhighlight()
            self.selected.blink_off()
            if index == len(children) - 1:
                if len(children) < len(self.contents):
                    # We have less on screen elements then we have contents so
                    # we are at the bottom of the displayed list and we need to
                    # add an object from later in the contents list.
                    layout = self.get_layout_manager()
                    try:
                        obj = self.contents[
                            self.contents.index(children[-1]) + 1
                            ]
                    except IndexError:
                        # We have hit the very bottom of items in contents. So
                        # we go ahead and start back at the top.
                        obj = self.contents[0]
                    self.selected = obj
                    layout.set_pack_start(False)
                    layout.pack(obj, True, False, False,
                                clutter.BOX_ALIGNMENT_CENTER,
                                clutter.BOX_ALIGNMENT_CENTER)
                    self.remove(children[0])
                else:
                    # We have the same number of on screen elements (children)
                    # as we have in our contents so we're just going to switch
                    # to the top-most displayed child.
                    self.selected = children[0]
            else:
                self.selected = children[index + 1]
            self.selected.blink_on()
            self.selected.highlight()

    def debug_contents(self):
        print '============================================================'
        print "DEBUGING SONGS"
        children = self.get_children()
        for child in children:
            print child.get_text()
        print '============================================================'


