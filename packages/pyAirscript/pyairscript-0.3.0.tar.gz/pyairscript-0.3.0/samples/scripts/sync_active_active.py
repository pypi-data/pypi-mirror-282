"""
AirScript: Airlock Gateway Configuration Script Engine

Copyright (c) 2019-2024 Urs Zurbuchen <urs.zurbuchen@ergon.ch>

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""

"""
Sync the config across Airlock Gateways in active/active mode

Usage: airscript sync-gw-config.py <origin | group>

If an origin node is specified, its configuration is sync'ed to the other nodes in the same group.
Ohterwise, the most recent config of all nodes in the same group is used.
Groups are defined in AirScript configuration file, by default ~/.airscript/config.yaml
"""

"""
The following global variables are pre-defined if run within AirScript shell:
- run.cmd
- run.config
- run.verbose
- run.is_console
- run.log_level
- run.log_file
"""

import sys

import airscript

from airscript.utils import scripts
from pyAirlock.common import log, output

out = output.Info()

def die( msg: str ):
    out.red( msg )
    sys.exit( 1 )

def sync_active_active( run ):
    log.set_level( 15 )

    origin = run.cmd.get_scriptparams()
    if not origin or origin == []:
        die( "Usage: sync-gw-config <origin | group>" )
    origin = origin[0]

    servers = airscript.gwLoad( None, run )
    if origin in servers:
        # use origin node
        session = servers[origin].session()
    else:
        # must be group name
        out.cyan( f"Finding most recent configuration for group {origin}" )
        ts = None
        for name in [name for name in servers if servers[name].group == origin]:
            session = servers[name].session()
            if session:
                cfg = session.configurationFindActive()
                if ts == None or ts < cfg.timestamp:
                    ts = cfg.timestamp
                    origin = name
                session.disconnect()

    out.yellow( f"Origin server: {origin}" )
    destinations = [name for name in servers if name != origin.name and servers[name].group == origin.group]
    origin_node = servers[origin]
    origin_session = origin_node.session()
    if not origin_session:
        die( f"Unable to establish session with origin node '{origin}'" )
    origin_config = origin_session.configurationFindActive()
    origin_name = origin_session.getNodename()

    out.cyan( f"- Downloading configuration" )
    zip_file = origin_config.download()

    for name in destinations:
        out.cyan( f"- {name}: uploading" )
        session = servers[name].session()
        if session:
            cfg = session.configurationFindActive()
            old_name = session.setNodename( origin_name )
            if not cfg.upload( zip_file ):
                out.error( "  failed" )
            session.setNodename( old_name )
            out.cyan( f"- {name}: activating" )
            if not cfg.activate( comment=f"{origin_config.comment} (sync from {origin})", options={'cluster': False} ):
                out.error( "  failed" )
            session.disconnect()

    out.green( "Completed" )

if __name__ == "__main__":
    sync_active_active( scripts.init() )
