# -*- coding: utf8 -*-
# SDAPS - Scripts for data acquisition with paper based surveys
# Copyright(C) 2008, Christoph Simon <post@christoph-simon.eu>
# Copyright(C) 2008, Benjamin Berg <benjamin@sipsolutions.net>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

u"""
This module adds the functionality to automatically recognize the scanned image
data. It reads the image data and tries to guess whether a checkbox is
empty/checked/filled and finds the written area in a textfield.
"""

from sdaps import model
from sdaps import script

from sdaps.ugettext import ugettext, ungettext
_ = ugettext


@script.register
@script.logfile
@script.doc(_(u'''

    Recognize all added sheets.

    Attention: This script overwrites all data, including manual changes made
        with the gui!
    '''))
def recognize(survey_dir):
    survey = model.survey.Survey.load(survey_dir)
    import recognize
    recognize.recognize(survey)

