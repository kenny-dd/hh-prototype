#!/usr/bin/env python

# import the necessary modules....
from flask import Flask, render_template
import argparse
import os
import logging
import logging.handlers
import json
import sys

logger = logging.getLogger('')

# add a parser and rules for parsing command-line arguments...
parser = argparse.ArgumentParser(description='A quick python script to test templates.')
parser.add_argument('-t','--template_folder', metavar='DIR', type=str, help='use a non-default directory holding the template files')
# add option to turn on debugging (more verbose logging output)....
parser.add_argument('-d','--debug', action='store_true', help='toggle debugging output on')
# main argument, the template name....
parser.add_argument('template', type=str,  help='the base filename of the template to use, e.g. "mytemplate" if the file is "templates/mytemplate.html"')
# a json string to add arguments to the jinja template....
parser.add_argument('-j', '--json', type=str,  help='a json string (dictionary) to add as keywords to the template, e.g. \'{"var1": 1, "var2": "two"}\'', default='')



# parse the actual command-line arguments and feed them into variables...
args = parser.parse_args()
# if debug is set, set to debug...
if args.debug:
    logging.warning('activating debug mode')
    # make a log-handler that outputs debug-level to screen...
    SCREENLOG_LEVEL = logging.DEBUG
    screenlog_handler = logging.StreamHandler()
    screenlog_handler.setLevel(SCREENLOG_LEVEL)
    screenlog_handler.set_name('screenlog')
    # clear any default log handlers...
    logger.handlers.clear()
    # add our new debug handler...
    logger.addHandler(screenlog_handler)
    # and make sure it allows debug level...
    logger.setLevel(logging.DEBUG)
    #
template = args.template
template_folder = args.template_folder

json_args = {}
if args.json:
    try:
        json_args = json.loads(args.json)
    except Exception as e:
        print(''.join(e.args))
        print('ERROR: not valid json: %s' % args.json)
        sys.exit(1)

logging.debug('template name: %s' % template)
logging.debug('template folder: %s' % template_folder)
logging.debug('command-line args: %s' % repr(args))

# was there a template_folder in the args?
if template_folder:
    # yes, check the custom folder exists....
    if not os.path.isdir(template_folder):
        raise Exception('folder does not exist: %s' % template_folder)
    # now check the template file exists in it....
    tmpfilename = os.path.join(template_folder, template)
    if not os.path.exists(tmpfilename):
        raise Exception('file does not exist: %s' % tmpfilename)
        # initiate the flask app with custom folder added...
    app = Flask(__name__, template_folder=template_folder)
    logging.debug('initiated flask with template folder: %s' % template_folder)
else:
    # no template_folder in args, so check the default templates folder...
    template_folder='templates'
    tmpfilename = os.path.join(template_folder, template)
    # does the template file exist where we expect it?
    if not os.path.exists(tmpfilename):
        raise Exception('file does not exist: %s' % tmpfilename)
    # initiate flask app with default values...
    app = Flask(__name__)
    logging.debug('initiated flask with default values')

print('args: template: %s, debug: %s, json: %s, template_folder: %s', (args.template, args.debug, args.json, args.template_folder) )


@app.route('/')
def do_template():
    logging.debug('main page called')
    return render_template(template, **json_args)


if __name__ == '__main__':
    # run the flask app!
    # this has the flask runtime initiate and listen on a port (usually 5001)
    # for inbound user GET requests...
    logging.debug('starting flask runtime...')
    app.run()
