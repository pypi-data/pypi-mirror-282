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
Connect to and communicate with Gateway

Please refer to the [Airlock Gateway REST API](https://docs.airlock.com/gateway/latest/rest-api/config-rest-api.html#authentication) documentation to understand how
it works, e.g. the requirements for loading and activating a configuration.
"""

import atexit
import json
import os
import requests
import tempfile
import urllib3

from urllib3.exceptions import MaxRetryError
from requests.adapters import HTTPAdapter, Retry

from ..common import exception
from ..common import log, lookup, utils
from .config_api import element
from .config_api.api_policy import APIPolicy
from .config_api.anomalyshield_application import AnomalyShieldApplication
from .config_api.anomalyshield_rule import AnomalyShieldRule
from .config_api.anomalyshield_settings import AnomalyShieldSettings
from .config_api.anomalyshield_trafficmatcher import AnomalyShieldTrafficMatcher
from .config_api.anomalyshield_trigger import AnomalyShieldTrigger
from .config_api.backendgroup import BackendGroup
from .config_api.certificate import Certificate
from .config_api.configuration import Configuration
from .config_api.graphql import GraphQL
from .config_api.host import Host
from .config_api.icap import ICAP
from .config_api.iplist import IPList
from .config_api.jwks import LocalJWKS, RemoteJWKS
from .config_api.kerberos import Kerberos
from .config_api.license import License
from .config_api.log_settings import LogSettings
from .config_api.mapping import Mapping
from .config_api.network_endpoint import NetworkEndpoint
from .config_api.network_services_settings import NetworkServicesSettings
from .config_api.node import Node
from .config_api.openapi import OpenAPI
from .config_api.reporting_settings import ReportingSettings
from .config_api.route import RouteIPV4Destination, RouteIPV6Destination, RouteIPV4Source, RouteIPV6Source
from .config_api.route_settings import RouteSettings
from .config_api.session_settings import SessionSettings
from .config_api.vhost import VirtualHost


class Session( object ):
    """
    Representation of a session with an Airlock Gateway

    * Handles communication with Airlock Gateway, including session management
    * Provides access to REST APIs for individual configuration elements, such as mappings, virtual hosts etc.
    """

    def __init__( self, hostname: str, key: str, name: str=None, run_info=None ):
        """
        Parameters to connect to Airlock Gateway

        * `name` is a user-friendly (short) name
        * `hostname` is the FQDN or IP address of the management interface
        * `key` is the API key
        * `run_info` is provided by the Airscript shell and allows access to configuration and command line parameters
        """
        #: The http session established with the Airlock Gateway. Handles cookies, timeouts and retries on errors.
        self.session = None
        self._hostname = hostname
        self._key = key
        self._name = name
        self._run_info = run_info
        self._url = f"https://{hostname}/airlock/rest"
        self._certfile = None
        self._tlsVerify = True
        self._version = None
        self._nodename = None
        if self._run_info:
            self._timeout = self._run_info.config.get( "airscript.timeout" )
        else:
            self._timeout = 5
        self._log = log.Log( self.__module__, self._run_info )
        #: CRUD and connection management REST API for `pyAirlock.gateway.config_api.api_policy.APIPolicy` configuration element
        self.api_policy = APIPolicy( self._name, self, self._run_info )
        #: CRUD and connection management REST API for `pyAirlock.gateway.config_api.anomalyshield_application.AnomalyShieldApplication` configuration element
        self.anomalyshield_application = AnomalyShieldApplication( self._name, self, self._run_info )
        #: CRUD and connection management REST API for `pyAirlock.gateway.config_api.anomalyshield_rule.AnomalyShieldRule` configuration element
        self.anomalyshield_rule = AnomalyShieldRule( self._name, self, self._run_info )
        #: CRUD and connection management REST API for `pyAirlock.gateway.config_api.anomalyshield_trafficmatcher.AnomalyShieldTrafficMatcher` configuration element
        self.anomalyshield_trafficmatcher = AnomalyShieldTrafficMatcher( self._name, self, self._run_info )
        #: CRUD and connection management REST API for `pyAirlock.gateway.config_api.anomalyshield_trigger.AnomalyShieldTrigger` configuration element
        self.anomalyshield_trigger = AnomalyShieldTrigger( self._name, self, self._run_info )
        #: CRUD and connection management REST API for `pyAirlock.gateway.config_api.backendgroup.BackendGroup` configuration element
        self.backendgroup = BackendGroup( self._name, self, self._run_info )
        #: CRUD and connection management REST API for `pyAirlock.gateway.config_api.certificate.Certificate` configuration element
        self.certificate = Certificate( self._name, self, self._run_info )
        #: CRUD and management REST API for `pyAirlock.gateway.config_api.configuration.Configuration` 
        self.configuration = Configuration( self._name, self, self._run_info )
        #: CRUD and connection management REST API for `pyAirlock.gateway.config_api.graphql.GraphQL` configuration element
        self.graphql = GraphQL( self._name, self, self._run_info )
        #: CRUD and connection management REST API for `pyAirlock.gateway.config_api.host.Host` configuration element
        self.host = Host( self._name, self, self._run_info )
        #: CRUD and connection management REST API for `pyAirlock.gateway.config_api.icap.ICAP` configuration element
        self.icap = ICAP( self._name, self, self._run_info )
        #: CRUD and connection management REST API for `pyAirlock.gateway.config_api.iplist.IPList` configuration element
        self.iplist = IPList( self._name, self, self._run_info )
        #: CRUD and connection management REST API for `pyAirlock.gateway.config_api.jwks.LocalJWKS` configuration element
        self.jwks_local = LocalJWKS( self._name, self, self._run_info )
        #: CRUD and connection management REST API for `pyAirlock.gateway.config_api.jwks.RemoteJWKS` configuration element
        self.jwks_remote = RemoteJWKS( self._name, self, self._run_info )
        #: CRUD and connection management REST API for `pyAirlock.gateway.config_api.kerberos.Kerberos` configuration element
        self.kerberos = Kerberos( self._name, self, self._run_info )
        #: CRUD and connection management REST API for `pyAirlock.gateway.config_api.mapping.Mapping` configuration element
        self.mapping = Mapping( self._name, self, self._run_info )
        #: CRUD and connection management REST API for `pyAirlock.gateway.config_api.network_endpoint.NetworkEndpoint` configuration element
        self.network_endpoint = NetworkEndpoint( self._name, self, self._run_info )
        #: CRUD and connection management REST API for Airlock Gateway `pyAirlock.gateway.config_api.node.Node`
        self.node = Node( self._name, self, self._run_info )
        #: CRUD and connection management REST API for `pyAirlock.gateway.config_api.openapi.OpenAPI` configuration element
        self.openapi = OpenAPI( self._name, self, self._run_info )
        #: CRUD and connection management REST API for `pyAirlock.gateway.config_api.route.RouteIPV4Destination` configuration element
        self.routes_ipv4_destination = RouteIPV4Destination( self._name, self, self._run_info )
        #: CRUD and connection management REST API for `pyAirlock.gateway.config_api.route.RouteIPV6Destination` configuration element
        self.routes_ipv6_destination = RouteIPV6Destination( self._name, self, self._run_info )
        #: CRUD and connection management REST API for `pyAirlock.gateway.config_api.route.RouteIPV4Source` configuration element
        self.routes_ipv4_source = RouteIPV4Source( self._name, self, self._run_info )
        #: CRUD and connection management REST API for `pyAirlock.gateway.config_api.route.RouteIPV6Source` configuration element
        self.routes_ipv6_source = RouteIPV6Source( self._name, self, self._run_info )
        #: CRUD and connection management REST API for `pyAirlock.gateway.config_api.vhost.VirtualHost` configuration element
        self.vhost = VirtualHost( self._name, self, self._run_info )

        #: Settings for `pyAirlock.gateway.config_api.anomalyshield_settings.AnomalyShieldSettings`
        self.settings_anomalyshield = AnomalyShieldSettings( self._name, self, self._run_info )
        #: Settings for `pyAirlock.gateway.config_api.log_settings.LogSettings`
        self.settings_log = LogSettings( self._name, self, self._run_info )
        #: Settings for `pyAirlock.gateway.config_api.network_services_settings.NetworkServicesSettings`
        self.settings_network_services = NetworkServicesSettings( self._name, self, self._run_info )
        #: Settings for `pyAirlock.gateway.config_api.reporting_settings.ReportingSettings`
        self.settings_reporting = ReportingSettings( self._name, self, self._run_info )
        #: Settings for `pyAirlock.gateway.config_api.route_settings.RouteSettings`
        self.settings_route = RouteSettings( self._name, self, self._run_info )
        #: Settings for `pyAirlock.gateway.config_api.session_settings.SessionSettings`
        self.settings_session = SessionSettings( self._name, self, self._run_info )
        #: Settings for `pyAirlock.gateway.config_api.license.License`
        self.license = License( self._name, self, self._run_info )
    
    def getHost( self ) -> str:
        """ Return FQDN or IP address. """
        return self._hostname
    
    def getName( self ) -> str:
        """ Return session name. """
        return self._name
    
    def getAPI( self, type_name ):
        """
        Retrieve handler for CRUD and connection management REST API for the configuration element.
        
        Possible values for `type_name` are:
        * api-policy-service
        * anomaly-shield-application
        * anomaly-shield-rule
        * anomaly-shield-traffi-matcher
        * anomaly-shield-trigger
        * back-end-group
        * ssl-certificate
        * graphql-document
        * host
        * icap-environment
        * ip-address-list
        * local-json-web-key-sets
        * remote-json-web-key-sets
        * kerberos
        * mapping
        * allowed-network-endpoint
        * node
        * openapi-document
        * virtual-host

        * anomaly-shield
        * license
        * log
        * network-services
        * reporting
        * route-default
        * session
        """
        if type_name == "api-policy-service":
            return self.api_policy
        elif type_name == "anomaly-shield-application":
            return self.anomalyshield_application
        elif type_name == "anomaly-shield-rule":
            return self.anomalyshield_rule
        elif type_name == "anomaly-shield-traffic-matcher":
            return self.anomalyshield_trafficmatcher
        elif type_name == "anomaly-shield-trigger":
            return self.anomalyshield_trigger
        elif type_name == "back-end-group":
            return self.backendgroup
        elif type_name == "ssl-certificate":
            return self.certificate
        elif type_name == "graphql-document":
            return self.graphql
        elif type_name == "host":
            return self.host
        elif type_name == "icap-environment":
            return self.icap
        elif type_name == "ip-address-list":
            return self.iplist
        elif type_name == "local-json-web-key-sets":
            return self.jwks_local
        elif type_name == "remote-json-web-key-sets":
            return self.jwks_remote
        elif type_name == "kerberos":
            return self.kerberos
        elif type_name == "mapping":
            return self.mapping
        elif type_name == "allowed-network-endpoint":
            return self.network_endpoint
        elif type_name == "node":
            return self.node
        elif type_name == "openapi-document":
            return self.openapi
        elif type_name == "route-ipv4-source":
            return self.routes_ipv4_source
        elif type_name == "route-ipv4-destination":
            return self.routes_ipv4_destination
        elif type_name == "route-ipv6-source":
            return self.routes_ipv6_source
        elif type_name == "route-ipv6-destination":
            return self.routes_ipv6_destination
        elif type_name == "virtual-host":
            return self.vhost
        elif type_name == "anomaly-shield":
            return self.settings_anomalyshield
        elif type_name == "license-response":
            return self.license
        elif type_name == "log":
            return self.settings_log
        elif type_name == "network-services":
            return self.settings_network_services
        elif type_name == "reporting":
            return self.settings_reporting
        elif type_name == "route-default":
            return self.settings_route
        elif type_name == "session":
            return self.settings_session
        return None

    def getVersion( self ) -> str:
        """
        Return connected Gateway's version.

        Airlock Gateways versions 7.x do not support this feature.
        pyAirlock will report their version number as fix "7.8".

        Please note that Airlock Gateway 7.8 was end-of-support in October 2023.
        """
        if not self._version:
            status = self.status()
            try:
                self._version = float( utils.getDictValue( status, "attributes.version" ))
            except TypeError:
                self._version = 7.8
            try:
                self._nodename = utils.getDictValue( status, "attributes.hostName" )
            except TypeError:
                self._nodename = "__unknown__"
        return self._version
    
    def getNodename( self ) -> str:
        """ Return connected Gateway's nodename. """
        if not self._nodename:
            self.getVersion()
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
    
    def setVerbosity( self, logLevel: int=None ) -> int:
        if logLevel != None:
            tmp_log = self._log( logLevel )
        return tmp_log

    def setCertificate( self, certfile=None, pem=None ):
        """
        Define CA certificate file to verify signature of Airlock Gateway's Config Center certificate.
        
        If Airlock Gateway Config Center uses a certificate not issued by any of the
        well-known certificate authorities (CAs) maintained in /etc/ssl/certs,
        the appropriate signing certificate must be specified here.

        Parameters:

        * `certfile`: path to CA certificate file, in PEM format
        * `pem`: CA certificate as string, in PEM format

        If you do not wish to verify the authenticity of the Airlock Gateway,
        you can use setTLSVerify() to turn verification off. This will also
        silence corresponding warnings.
        """
        if certfile == None and pem == None:
            self._certfile = None
        elif certfile:
            self._certfile = os.path.expanduser( certfile )
        else:
            try:
                fp, fname = tempfile.mkstemp( suffix=".pem", text=True )
                fp.write( pem )
                fp.close()
            except OSError as e:
                e.add_note( f"File: {fname}" )
                raise exception.AirlockFileWriteError()
            self._certfile = os.path.expanduser( fname )
            atexit.register( self._certificateCleanup, fname )
    
    def setTLSVerify( self, verify ) -> bool:
        """
        Suppress server certificate checking.
        
        Passing in `verify=False` completely disables server certificate checking.
        While this may be easy for self-signed Airlock Gateway Config Center
        certificates, it should not be used in production.
        
        Warning messages by the underlying libraries about unsecure connections
        will also be silenced.

        For an even stronger version, passing in `verify=None` also suppresses
        any warning messages related to the certificate.
        """
        if verify != True:
            urllib3.disable_warnings()
        if verify == None:
            self._tlsVerify = False
            return True
        if verify == True or verify == False:
            self._tlsVerify = verify
            return True
        return False
    
    def connect( self ) -> bool:
        """
        Establish session with Airlock Gateway.
        """
        if self.session != None:
            return True
        self.session = requests.Session()
        self.session.headers.update( {"Authorization": f"Bearer {self._key}"} )
        # retries = Retry( total=5, backoff_factor=0, allowed_methods=None, status_forcelist=[ 500, 502, 503, 504 ] )
        # self.session.mount( self._url, HTTPAdapter( max_retries=retries ))
        try:
            self.post( "/session/create", expect=[200] )
        except exception.AirlockCommunicationError:
            self.session = None
            return False
        return True
    
    def disconnect( self ):
        """
        Disconnect from Airlock Gateway, closing administrator session.
        
        Subsequent calls to the Airlock Gateway REST API endpoint will result in an error.

        This session will no longer count as existing parallel session in Config Center nor cause a warning that another administrator is active.
        """
        if self.session:
            self.post( "/session/terminate", expect=[200] )
            self._log.info( "Disconnected from '%s'" % (self._name,) )
        self.session = None
    
    def keepalive( self ):
        """
        A session to an Airlock Gateway times out after about 10 minutes of inactivity.
        To keep it active, REST API requests must be sent in regular intervals.
        This function fetches the node status and can be used as a side-effect free keep-alive.

        For standard scripts, this is not required.
        """
        try:
            self.get( "/configuration/license", expect=[200] )
        except exception.AirlockCommunicationError:
            pass

    def status( self ) -> dict:
        """
        Retrieve node status

        Returns: dict according to [API documentation](https://docs.airlock.com/gateway/latest/rest-api/config-rest-api.html#get-node-status)
        """
        resp = self.get( "/system/status/node", expect=[200] )
        try:
            return resp.json()['data']
        except KeyError:
            raise exception.AirlockDataError()

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

    def get( self, path: str, accept=None, timeout=None, expect: list[int]=None ) -> requests.Response:
        """
        Perform REST API GET and return HTTP response.
        
        Session with Airlock Gateway must previously have been established.

        Parameters:

        * `path`: REST API endpoint (without hostname or protocol), e.g. "/back-end-groups"
        * `expect`: list of expected HTTP response codes, other values result in exceptions
        * `accept`: set if you expect something else than 'application/json' as response
        * `timeout`: override the default session timeout, specify number of seconds

        Returns: [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response) object
        """
        try:
            resp = self.session.get( f"{self._url}{path}",
                                    headers=self._headers( accept=accept ),
                                    timeout=self._timeout if timeout == None else timeout,
                                    verify=self._verify() )
            return self._validateResponse( resp, path, expect )
        except (requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout, urllib3.exceptions.MaxRetryError) as e:
            raise exception.AirlockCommunicationError
    
    def post( self, path: str, data=None, accept=None, content=None, timeout=None, expect: list[int]=None ) -> requests.Response:
        """
        Perform REST API POST and return HTTP response.
        
        Session with Airlock Gateway must previously have been established.

        Parameters:
        
        * `path`: REST API endpoint (without hostname or protocol), e.g. "/session/cxreate"
        * `data`: must be pre-formatted, e.g. ready to be converted to JSON if REST endpoint expects JSON
        * `content`: must be set if data is not JSON
        * `expect`: list of expected HTTP response codes, other values result in exceptions
        * `accept`: set if you expect something else than 'application/json' as response
        * `timeout`: override the default session timeout, specify number of seconds

        Returns: [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response) object
        """
        try:
            resp = self.session.post( f"{self._url}{path}",
                                    headers=self._headers( accept=accept, content=content ),
                                    timeout=self._timeout if timeout == None else timeout,
                                    verify=self._verify(),
                                    data=self._jsonify( data ))
            return self._validateResponse( resp, path, expect )
        except (requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout, urllib3.exceptions.MaxRetryError) as e:
            raise exception.AirlockCommunicationError
    
    def patch( self, path: str, data=None, accept=None, content=None, timeout=None, expect: list[int]=None ) -> requests.Response:
        """
        Perform REST API PATCH and return HTTP response.
        
        Session with Airlock Gateway must previously have been established.

        Parameters:

        * `path`: REST API endpoint (without hostname or protocol), e.g. "/mappings/{id}/relationships/openapi-document"
        * `data`: must be pre-formatted, e.g. ready to be converted to JSON if REST endpoint expects JSON
        * `content`: must be set if data is not JSON
        * `expect`: list of expected HTTP response codes, other values result in exceptions
        * `accept`: set if you expect something else than 'application/json' as response
        * `timeout`: override the default session timeout, specify number of seconds

        Returns: [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response) object
        """
        try:
            resp = self.session.patch( f"{self._url}{path}",
                                    headers=self._headers( accept=accept, content=content ),
                                    timeout=self._timeout if timeout == None else timeout,
                                    verify=self._verify(),
                                    data=self._jsonify( data ) )
            return self._validateResponse( resp, path, expect )
        except (requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout, urllib3.exceptions.MaxRetryError) as e:
            raise exception.AirlockCommunicationError
    
    def put( self, path: str, data=None, accept=None, content=None, timeout=None, expect: list[int]=None ) -> requests.Response:
        """
        Perform REST API PUT and return HTTP response.
        
        Session with Airlock Gateway must previously have been established.

        Parameters:

        * `path`: REST API endpoint (without hostname or protocol), e.g. "/mappings/import"
        * `data`: must be pre-formatted, e.g. ready to be converted to JSON if REST endpoint expects JSON
        * `content`: must be set if data is not JSON
        * `expect`: list of expected HTTP response codes, other values result in exceptions
        * `accept`: set if you expect something else than 'application/json' as response
        * `timeout`: override the default session timeout, specify number of seconds

        Returns: [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response) object
        """
        try:
            resp = self.session.put( f"{self._url}{path}",
                                    headers=self._headers( accept=accept, content=content ),
                                    timeout=self._timeout if timeout == None else timeout,
                                    verify=self._verify(),
                                    data=self._jsonify( data ) )
            return self._validateResponse( resp, path, expect )
        except (requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout, urllib3.exceptions.MaxRetryError) as e:
            raise exception.AirlockCommunicationError
    
    def delete( self, path: str, data=None, accept=None, timeout=None, expect: list[int]=None ) -> requests.Response:
        """
        Perform REST API DELETE and return HTTP response.
        
        Session with Airlock Gateway must previously have been established.

        Parameters:

        * `path`: REST API endpoint (without hostname or protocol), e.g. "/virtual-hosts/{id}"
        * `data`: must be pre-formatted, e.g. ready to be converted to JSON if REST endpoint expects JSON
        * `expect`: list of expected HTTP response codes, other values result in exceptions
        * `accept`: set if you expect something else than 'application/json' as response
        * `timeout`: override the default session timeout, specify number of seconds

        Returns: [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response) object
        """
        try:
            resp = self.session.delete( f"{self._url}{path}",
                                        headers=self._headers( accept=accept ),
                                        timeout=self._timeout if timeout == None else timeout,
                                        verify=self._verify(),
                                        data=self._jsonify( data ) )
            return self._validateResponse( resp, path, expect )
        except (requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout, urllib3.exceptions.MaxRetryError) as e:
            raise exception.AirlockCommunicationError
    
    def upload( self, path: str, files=None, content=None, timeout=None, expect: list[int]=None ) -> requests.Response:
        """
        Perform REST API PUT to upload a file and return HTTP response.
        
        Session with Airlock Gateway must previously have been established.

        Parameters:

        * `path`: REST API endpoint (without hostname or protocol)
        * `files`: must be a dict "{ 'file': <opened file handle> }"
        * `content`: must be set to the uploaded data's content type (which is probably not 'application/json')
        * `expect`: list of expected HTTP response codes, other values result in exceptions
        * `timeout`: override the default session timeout, specify number of seconds

        Returns: [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response) object
        """
        try:
            resp = self.session.put( f"{self._url}{path}",
                                    headers=self._headers( content=content ),
                                    timeout=self._timeout if timeout == None else timeout,
                                    verify=self._verify(),
                                    files=files )
            return self._validateResponse( resp, path, expect )
        except (requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout, urllib3.exceptions.MaxRetryError) as e:
            raise exception.AirlockCommunicationError
    
    def uploadCopy( self, path: str, files=None, content=None, timeout=None, expect: list[int]=None ) -> requests.Response:
        """
        Perform REST API POST to upload a file and return HTTP response.
        
        Session with Airlock Gateway must previously have been established.

        Parameters:

        * `path`: REST API endpoint (without hostname or protocol)
        * `files`: must be a dict "{ 'file': <opened file handle> }"
        * `content`: must be set to the uploaded data's content type (which is probably not 'application/json')
        * `expect`: list of expected HTTP response codes, other values result in exceptions
        * `timeout`: override the default session timeout, specify number of seconds

        Returns: [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response) object
        """
        try:
            resp = self.session.post( f"{self._url}{path}",
                                    headers=self._headers( content=content ),
                                    timeout=self._timeout if timeout == None else timeout,
                                    verify=self._verify(),
                                    files=files )
            return self._validateResponse( resp, path, expect )
        except (requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout, urllib3.exceptions.MaxRetryError) as e:
            raise exception.AirlockCommunicationError
    
    def _headers( self, accept=None, content=None ) -> dict:
        """
        Return dict with HTTP headers to send to Airlock Gateway.

        Parameters:

        * `accept`: mime type of response, default is 'application/json'
        * `content`: mime type of sent data, default is 'application/json'
        """
        hdr = { "Accept": "application/json", "Content-Type": "application/json" }
        if accept != None:
            hdr['Accept'] = accept
        if content != None:
            hdr['Content-Type'] = content
        return hdr
    
    def _verify( self ) -> bool:
        """ Return certificate verification setting for requests library. """
        verify=True
        if self._certfile != None:
            verify = self._certfile
        if self._tlsVerify == False:
            verify = False
        return verify
    
    def _jsonify( self, data ):
        try:
            return json.dumps( data )
        except TypeError:
            return data
    
    def _validateResponse( self, response, path: str, expect: list[int] ) -> requests.Response:
        """
        Validate the response has one of the expect status codes

        Parameters:
        
        * `response`: the response to validate
        * `expect`: list of expected HTTP response codes, other values result in exceptions
        * `path`: original request path, for logging only

        Returns: [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response) object
        """
        if expect:
            if response.status_code not in expect:
                if response.status_code >= 500:
                    self._log.critical( f"{self._name}: {path} returned {response.status_code}" )
                    raise exception.AirlockServerError( response.status_code, response.text )
                elif response.status_code >= 400:
                    self._log.error( f"{self._name}: {path} returned {response.status_code}" )
                    raise exception.AirlockAPIError( response.status_code, response.text )
                elif response.status_code >= 200:
                    self._log.warning( f"{self._name}: {path} returned {response.status_code}" )
        return response

    def _certificateCleanup( self, fname: str ) -> None:
        if fname != None:
            try:
                os.remove( fname )
            except OSError:
                pass
    
