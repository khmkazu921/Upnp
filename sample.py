#!/usr/bin/env python
#-*- coding:utf-8 -*-

import time
import urllib.request
import urllib.parse
from urllib.error import HTTPError

host = '192.168.129.1'
port = '57716'
extport = '5555'
IP = '192.168.129.57'

getentry = '<?xml version="1.0"?><s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><s:Body><u:GetGenericPortMappingEntry xmlns:u="urn:schemas-upnp-org:service:WANIPConnection:1"><NewPortMappingIndex>2</NewPortMappingIndex></u:GetGenericPortMappingEntry></s:Body></s:Envelope>'

portmapping  = '<?xml version="1.0"?><s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><s:Body><u:AddPortMapping xmlns:u="urn:schemas-upnp-org:service:WANIPConnection:1"><NewRemoteHost></NewRemoteHost><NewExternalPort>8080</NewExternalPort><NewProtocol>UDP</NewProtocol><NewInternalPort>88</NewInternalPort><NewInternalClient>192.168.129.57</NewInternalClient><NewEnabled>1</NewEnabled><NewPortMappingDescription>Test</NewPortMappingDescription><NewLeaseDuration>0</NewLeaseDuration></u:AddPortMapping></s:Body></s:Envelope>'

#msg2 = '<?xml version="1.0"?><s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><s:Body><u:GetExternalIPAddress xmlns:u="urn:schemas-upnp-org:service:WANIPConnection:1"></m:GetExternalIPAddress></s:Body></s:Envelope>'

msg = getentry#portmapping
#msg = msg.encode("utf-8")
req = urllib.request.Request(url="http://192.168.129.1:57716/ctl/IPConn",data=msg.encode("utf-8"),method='POST')
req.add_header('Content-type', 'application/xml; charset="utf-8"')
req.add_header('SOAPACTION', '"urn:schemas-upnp-org:service:WANIPConnection:1#GetGenericPortMappingEntry"')
#req.add_header('SOAPACTION', '"urn:schemas-upnp-org:service:WANIPConnection:1#AddPortMapping"')
#req.add_header('SOAPACTION', '"urn:schemas-upnp-org:service:WANIPConnection:1#GetExternalIPAddress"')

i=0
while(True):
   try:
      resp = urllib.request.urlopen(req).read().decode("utf-8")
      print(resp)
   except HTTPError as e:
      content = e.read()
      print(content)
      pass
   i += 1
   print(i)
   time.sleep(30)
