from talon.voice import Context
from talon_plugins import eye_mouse

ctx = Context("eye_control")


def _start_calibration():
    return lambda m: eye_mouse.calib_start()


ctx.keymap(
    {
        # "debug overlay": lambda m: eye_mouse.on_menu(
        #     "Eye Tracking >> Show Debug Overlay"
        # ),
        # "control mouse": lambda m: eye_mouse.on_menu("Eye Tracking >> Control Mouse"),
        # "camera overlay": lambda m: eye_mouse.on_menu(
        #     "Eye Tracking >> Show Camera Overlay"
        # ),
        # "run calibration": lambda m: eye_mouse.on_menu("Eye Tracking >> Calibrate")
        "run calibration": _start_calibration()
    }
)
