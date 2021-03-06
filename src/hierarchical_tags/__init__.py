# -*- coding: utf-8 -*-

# Hierarchical Tags 2 for Anki
#
# Coypright (C) 2014  Patrice Neff <http://patrice.ch/>
# Copyright (C) 2018-2020  Aristotelis P. <https//glutanimate.com/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from anki.hooks import wrap
from aqt.browser import Browser

from ._version import __version__  # noqa: F401
from .browser import onTagClick, onTagClickOld, userTagTree, userTagTreeOld
from .consts import old_anki


def setupAddon():
    if not old_anki:
        Browser.onTagClick = onTagClick
        Browser._userTagTree = wrap(Browser._userTagTree, userTagTree, "around")
    else:
        Browser.onTagClick = onTagClickOld
        Browser._userTagTree = wrap(Browser._userTagTree, userTagTreeOld, "around")

setupAddon()
