import os
import logging

import pywebio
from pywebio import output

from . import config
from . import tool_dashboard
from . import tool_profitcalcs
from . import tool_rpccurlhelper
from . import tool_opretreader
from . import tool_terminal

def read_candy():
    datadir = "/root/assets/"

    try:
        candyfile = os.path.join(datadir, "candy")
        logging.error("candyfile: {}".format(candyfile))
        with open(candyfile, "r") as f:
            logging.error("CANDY: {}".format(f.read()))
    except FileNotFoundError:
        logging.error("CANDY FILE NOT FOUND")

    with output.use_scope('app', clear=True):
        output.put_text("check the logs...")



@pywebio.config(title=config.APP_TITLE, theme='dark')
def main_menu():

    output.clear('app')
    with output.use_scope('main', clear=True):
        if config.DEBUG:
            output.put_text(f"DEBUG: {config.DEBUG}")

        output.put_markdown(f"# {config.APP_TITLE}")

        # here we pass this function as a callback to the buttons so that the back buttons work without an infinite import loop
        output.put_button("Bitcoin Dashboard", onclick=lambda: tool_dashboard.web_interface.main_page(main_menu))
        output.put_button("Mining Profitability Calculator", onclick=lambda: tool_profitcalcs.web_interface.main_page(main_menu))
        output.put_button("Mining Treasury Management Simulator", onclick=lambda: output.toast("Coming Soon!"))
        output.put_button("bitcoin-cli RPC curl Formatter", onclick=lambda:tool_rpccurlhelper.web_interface.main_page(main_menu))
        # output.put_button("OP_RETURN Reader", onclick=lambda: tool_opretreader.web_interface.main_page(main_menu))
        # output.put_button("terminal", onclick=lambda: tool_terminal.web_interface.main_page(main_menu))
        # output.put_markdown("---\ndebugging")
        # output.put_button("eat candy", read_candy)
