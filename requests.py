#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""yotaSituation requests layer"""

import urllib2
import json
import datetime


class Request(object):
  __baseUrl = 'http://status.yota.ru/devcontrol?callback=?&command='

  def __init__(self, commandName=None):
    self.commandName = commandName
    if commandName:
      self.url = self.__baseUrl+self.commandName
      self.make()
      self.sanitize()
      self.jsonize()

  def __nowStr(self):
    return datetime.datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)")
  def jsonize(self):
    self.data = json.loads(self.sanitized)
  def sanitize(self):
    self.sanitized = self.response[2:][:-2]
  def make(self):
    self.requestTime = self.__nowStr()
    self.response = urllib2.urlopen(self.url).read()
    self.responseTime = self.__nowStr()
  def __str__(self):
    result = {
      'requestTime': self.requestTime,
      'responseTime': self.responseTime,
      'requestUrl': self.url,
      'responseBody': self.data
    }
    return json.dumps(result, indent=2, separators=(',', ': '), sort_keys=True)


class GeneralInfo(Request):
  def __init__(self):
    super(GeneralInfo, self).__init__('getGeneralInfo')

class Status(Request):
  def __init__(self):
    super(Status, self).__init__('getStatus')
