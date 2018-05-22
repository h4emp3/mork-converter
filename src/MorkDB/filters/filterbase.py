# Copyright 2010 Kevin Goodsell

# This file is part of mork-converter.
#
# mork-converter is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License Version 2 as published
# by the Free Software Foundation.
#
# mork-converter is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with mork-converter.  If not, see <http://www.gnu.org/licenses/>.

# flake8: noqa
# pylint: disable=missing-docstring,invalid-name

class Filter(object):
    def add_options(self, parser):
        '''
        Add optparse options to the parser (an OptionParser object).
        '''
        pass

    def process(self, db, opts):
        '''
        Filter the MorkDatabase object db.
        '''
        raise NotImplementedError()

    # Order, to be overriden in derived classes or instances. Negative values
    # indicate something that shouldn't be used as a filter (such as base
    # classes or disabled filters).
    mork_filter_order = -1

    # Defined ordering values:
    #  2000 - Point at which any stripping of unneeded values is complete, and
    #         operations on remaining values can proceed.
    #  4000 - Point at which all character-level translations are complete
    #         and field-level translations can proceed.
    #  6000 - Point at which field-level translations are complete and
    #         table-level translations can proceed.
    #  8000 - Point at which table-level translations are complete and
    #         database-level translations can proceed.
    # 10000 - Point at which all translations are complete, and output can
    #         proceed.
