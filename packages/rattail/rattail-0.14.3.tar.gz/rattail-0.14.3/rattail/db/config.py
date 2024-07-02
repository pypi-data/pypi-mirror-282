# -*- coding: utf-8; -*-
################################################################################
#
#  Rattail -- Retail Software Framework
#  Copyright © 2010-2024 Lance Edgar
#
#  This file is part of Rattail.
#
#  Rattail is free software: you can redistribute it and/or modify it under the
#  terms of the GNU General Public License as published by the Free Software
#  Foundation, either version 3 of the License, or (at your option) any later
#  version.
#
#  Rattail is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
#  FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
#  details.
#
#  You should have received a copy of the GNU General Public License along with
#  Rattail.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
"""
Database Configuration
"""

import logging
import warnings

from rattail.exceptions import SQLAlchemyNotInstalled


log = logging.getLogger(__name__)


def get_engines(config, section='rattail.db'):
    """
    DEPRECATED; please use
    :func:`wuttjamaican:wuttjamaican.db.conf.get_engines()` instead.
    """
    warnings.warn("rattail.db.config.get_engines() is deprecated; "
                  "please use wuttjamaican.db.get_engines() instead",
                  DeprecationWarning, stacklevel=2)
    from wuttjamaican.db import get_engines
    return get_engines(config, section)


def get_default_engine(config, section='rattail.db'):
    """
    DEPRECATED; please use
    :func:`wuttjamaican:wuttjamaican.db.conf.get_engines()` instead.
    """
    warnings.warn("rattail.db.config.get_default_engine() is deprecated; "
                  "please use wuttjamaican.db.get_engines() instead",
                  DeprecationWarning, stacklevel=2)
    from wuttjamaican.db import get_engines
    return get_engines(config, section).get('default')


# TODO: Deprecate/remove this.
def configure_session(config, session):
    """
    Configure a session factory or instance.  Currently all this does is
    install the hook to record changes, if config so dictates.
    """
    if config.getbool('rattail.db', 'changes.record', usedb=False):
        from rattail.db.changes import record_changes
        record_changes(session, config=config)


def configure_versioning(config, force=False, manager=None, plugins=None, **kwargs):
    """
    Configure Continuum versioning.
    """
    if not config.versioning_enabled() and not force:
        return

    try:
        from sqlalchemy.orm import configure_mappers
        import sqlalchemy_continuum as continuum
        from sqlalchemy_continuum.plugins import TransactionMetaPlugin
        from rattail.db.continuum import versioning_manager, RattailPlugin
    except ImportError as error:
        raise SQLAlchemyNotInstalled(error)
    else:
        kwargs['manager'] = manager or versioning_manager
        if plugins:
            kwargs['plugins'] = plugins
        else:
            kwargs['plugins'] = [TransactionMetaPlugin(), RattailPlugin()]
        log.debug("enabling Continuum versioning")
        continuum.make_versioned(**kwargs)

        # TODO: is this the best way/place to confirm versioning?
        try:
            model = config.get_model()
            configure_mappers()
            transaction_class = continuum.transaction_class(model.User)
            config.versioning_has_been_enabled = True
        except continuum.ClassNotVersioned:
            raise RuntimeError("Versioning is enabled and configured, but is not functional!  "
                               "This probably means the code import sequence is faulty somehow.  "
                               "Please investigate ASAP.")
