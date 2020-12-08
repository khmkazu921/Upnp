#!/usr/bin/env python
#-*- coding:utf-8 -*-

import urllib.request
from urllib.error import HTTPError

msg  = '<?xml version="1.0"?><s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><s:Body><u:AddPortMapping xmlns:u="urn:schemas-upnp-org:service:WANIPConnection:1"><NewRemoteHost></NewRemoteHost><NewExternalPort>7240</NewExternalPort><NewProtocol>TCP</NewProtocol><NewInternalPort>8081</NewInternalPort><NewInternalClient>192.168.129.57</NewInternalClient><NewEnabled>1</NewEnabled><NewPortMappingDescription>RaspberryPi</NewPortMappingDescription><NewLeaseDuration>86400</NewLeaseDuration></u:AddPortMapping></s:Body></s:Envelope>'
req = urllib.request.Request(url="http://192.168.129.1:57716/ctl/IPConn",data=msg.encode("utf-8"),method='POST')
req.add_header('Content-type', 'application/xml; charset="utf-8"')
req.add_header('SOAPACTION', '"urn:schemas-upnp-org:service:WANIPConnection:1#AddPortMapping"')

try:
   resp = urllib.request.urlopen(req).read().decode("utf-8")
   print(resp)
   print("Port Mapping Finished")
except HTTPError as e:
   content = e.read()
   print(content)

#getentry = '<?xml version="1.0"?><s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><s:Body><u:GetGenericPortMappingEntry xmlns:u="urn:schemas-upnp-org:service:WANIPConnection:1"><NewPortMappingIndex>2</NewPortMappingIndex></u:GetGenericPortMappingEntry></s:Body></s:Envelope>'
#req.add_header('SOAPACTION', '"urn:schemas-upnp-org:service:WANIPConnection:1#GetGenericPortMappingEntry"')
#req.add_header('SOAPACTION', '"urn:schemas-upnp-org:service:WANIPConnection:1#GetExternalIPAddress"')
