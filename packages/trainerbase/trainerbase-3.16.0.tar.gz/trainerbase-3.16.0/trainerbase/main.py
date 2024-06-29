from collections.abc import Callable
from os import _exit as force_exit
from traceback import print_exc
from typing import NoReturn

from trainerbase.codeinjection import safely_eject_all_code_injections
from trainerbase.gameobject import update_frozen_objects
from trainerbase.gui.objects import update_displayed_objects
from trainerbase.process import show_message_and_shutdown_if_process_exited
from trainerbase.scriptengine import (
    Script,
    process_healthcheck_script_engine,
    rainbow_script_engine,
    system_script_engine,
)
from trainerbase.speedhack import SpeedHack


def run(  # pylint: disable=too-complex
    run_gui: Callable[[Callable], None],
    on_gui_initialized_hook: Callable | None = None,
    on_shutdown_hook: Callable | None = None,
) -> NoReturn:
    def on_shutdown() -> NoReturn:
        system_script_engine.stop()
        process_healthcheck_script_engine.stop()
        rainbow_script_engine.stop()

        safely_eject_all_code_injections()
        SpeedHack.disable()

        if on_shutdown_hook is not None:
            on_shutdown_hook()

        force_exit(0)

    def on_gui_initialized() -> None:
        system_script_engine.start()
        process_healthcheck_script_engine.start()
        rainbow_script_engine.start()

        if on_gui_initialized_hook is not None:
            try:
                on_gui_initialized_hook()
            except Exception:
                print_exc()
                on_shutdown()

    system_script_engine.register_script(Script(update_frozen_objects, enabled=True))
    system_script_engine.register_script(Script(update_displayed_objects, enabled=True))
    process_healthcheck_script_engine.register_script(Script(show_message_and_shutdown_if_process_exited, enabled=True))

    try:
        run_gui(on_gui_initialized)
    except Exception:
        print_exc()

    on_shutdown()
