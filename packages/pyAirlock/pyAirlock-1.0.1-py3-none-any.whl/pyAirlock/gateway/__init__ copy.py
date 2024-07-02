# pyAirlock: Python library for Airlock products
# 
# Copyright (c) 2019-2024 Urs Zurbuchen <info@airlock.com>
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

"""
Airlock Gateway REST APIs

There is currently only one REST API for the Airlock Gateway.
It is used to manage the configuration.

Please refer to the [Airlock Gateway REST API](https://docs.airlock.com/gateway/latest/rest-api/config-rest-api.html#authentication) documentation to understand how
it works, e.g. the requirements for loading and activating a configuration.

"""

from . import configsession
from ..common import exception
from ..common import log, utils


class Connection( object ):
    """
    Representation of an Airlock Gateway

    * Allows configuration management over REST API.
    * Handles communication with Airlock Gateway, including session management
    * Provides access to REST APIs for individual configuration elements, such as mappings, virtual hosts etc.
    """

    def __init__( self, name: str, hostname: str, key: str, run_info=None ):
        """
        Parameters to connect to Airlock Gateway

        * `name` is a user-friendly (short) name
        * `hostname` is the FQDN or IP address of the management interface
        * `key` is the API key
        * `run_info` is provided by the Airscript shell and allows access to configuration and command line parameters
        """
        self._name = name
        self._hostname = hostname
        self._key = key
        self._run_info = run_info
        self._sessions = []
        self._url = f"https://{hostname}/airlock/rest"
        self._data_valid = False
        self._version = None
        self._nodename = None
        self._log = log.Log( self.__module__, self._run_info )
    
    def getName( self ) -> str:
        """ Return short name. """
        return self._name
    
    def getHost( self ) -> str:
        """ Return FQDN or IP address. """
        return self._hostname
    
    def getKey( self ) -> str:
        """ Return API key. """
        return self._key
    
    def getVersion( self ) -> str:
        """
        Return connected Gateway's version.

        Airlock Gateways versions 7.x do not support this feature.
        pyAirlock will report their version number as fix "7.8".

        Please note that Airlock Gateway 7.8 was end-of-support in October 2023.
        """
        if self._data_valid == False:
            raise( exception.AirlockNoSessionError )
        return self._version
    
    def getNodename( self ) -> str:
        """ Return connected Gateway's nodename. """
        if self._data_valid == False:
            raise( exception.AirlockNoSessionError )
        return self._nodename
    
    def isActive( self ) -> bool:
        """
        Check if Airlock Gateway is active node in an active/passive cluster
        
        Returns:
        * True if node is active or if node is not in an active/passive cluster
        * False if node is the passive partner
        """
        if self.failoverState() in ["active", "standalone"]:
            return True
        else:
            return False
    
    def session( self ) -> configsession.Session:
        """
        Create a new session connected to this Airlock Gateway.
        """
        sess = configsession.Session( self._hostname, self._key, self._run_info )
        if sess.connect() == False:
            raise exception.AirlockConnectionError()
        self._sessions.append( sess )
        resp = sess.get( "/system/status/node", expect=[200] )
        try:
            self._version = float( utils.getDictValue( resp.json(), "data.attributes.version" ))
        except TypeError:
            self._version = None
        try:
            self._nodename = utils.getDictValue( resp.json(), "data.attributes.hostName" )
        except TypeError:
            self._nodename = None
        self._data_valid = True
        self._log.info( f"Connected to '{self._name}' ({self._nodename})" )
        if not self._version:
            self._log.info( f"{self._name}: version indeterminable - assuming 7.8 but compatibility not guaranteed" )
            self._version = 7.8
        return sess

    def status( self ) -> dict:
        """
        Retrieve node status

        Returns: dict according to [API documentation](https://docs.airlock.com/gateway/latest/rest-api/config-rest-api.html#get-node-status)
        """
        for sess in self._sessions:
            try:
                resp = sess.get( "/system/status/node", expect=[200] )
            except exception.AirlockCommunicationError:
                continue
            try:
                return resp.json()['data']
            except KeyError:
                raise exception.AirlockDataError()
        raise( exception.AirlockNoSessionError )

    def failoverState( self ):
        """
        Retrieve failover state
        
        Returns:
        * active
        * passive
        * standalone
        * offline
        """
        status = self.status()
        try:
            return status['attributes']['failoverState']
        except KeyError:
            raise exception.AirlockDataError()

