#
import sublime


#
_PACKAGE_NAME = 'AoikConsolePanelStartup'

_SHOW_CONSOLE_PANEL_CALLBACK_DELAY = 100  # miliseconds


# Define callback to be registered in function "plugin_loaded".
# Use callback instead of directly calling "run_command" in "plugin_loaded"
# because "sublime.active_window()" is not ready to be called in
# "plugin_loaded".
class ShowConsolePanelCallbackClass(object):

    def __init__(self, callback_delay):
        self._callback_delay = callback_delay

    def __call__(self, plugin_is_loading=False):
        """
        @param plugin_is_loading: Whether this plugin is being loaded by
         Sublime Text. Should set to True when calling this function inside
         function "plugin_loaded" at 31GM6.
        """
        #
        settings = sublime.load_settings(
            '{0}.sublime-settings'.format(_PACKAGE_NAME))

        #
        plugin_is_enabled = settings.get('enable', True)

        if not plugin_is_enabled:
            return

        #
        debug_on = settings.get('debug', False)

        def print_func(text):
            if debug_on:
                print(text)

        # If the plugin is being loaded by Sublime Text,
        # "sublime.active_window()" is not ready to be called
        if plugin_is_loading:
            window = None
        else:
            window = sublime.active_window()

        # If Sublime Text's startup work has not finished yet
        if window is None:
            #
            print_func(
                '# {0}\nWait {1} miliseconds'.format(
                    _PACKAGE_NAME, self._callback_delay))

            # 7PD4A
            # Set callback.
            # Wait "_callback_delay" miliseconds for Sublime Text's startup
            # work to finish.
            sublime.set_timeout(self, self._callback_delay)
        # If Sublime Text's startup work has finished
        else:
            #
            print_func(
                '# {0}\nShow console panel'.format(_PACKAGE_NAME))

            # Show console panel
            window.run_command("show_panel", {"panel": "console"})


# Sublime Text 3 will call "plugin_loaded" when loading a plugin
def plugin_loaded():
    # Create a callback
    callback = ShowConsolePanelCallbackClass(
        callback_delay=_SHOW_CONSOLE_PANEL_CALLBACK_DELAY
    )

    # 31GM6
    # Register the callback using "sublime.set_timeout" at 7PD4A
    callback(plugin_is_loading=True)


# Sublime Text 2 will not call "plugin_loaded" when loading a plugin
if sublime.version().startswith('2'):
    # Call it manually
    plugin_loaded()
