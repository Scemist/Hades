from flask import render_template, session


class IndexController:
    def index(alert=None):
        key_setted = "key" in session
        drive_state_setted = "state" in session

        return render_template(
            "drive.jinja",
            alert=alert,
            key_setted=key_setted,
            drive_state_setted=drive_state_setted,
        )
