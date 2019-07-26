# coding=utf-8
import json
import digdag

class EXAMPLE(object):
  def getParam(self):
    list = ["e", "x", "a", "m", "p", "l", "e"]
    digdag.env.store({'params': json.dumps(list)})

  def getParamNum(self):
    list = ["e", "x", "a", "m", "p", "l", "e"]
    result = []
    for i in range(len(list)):
      result.append({'no': i, 'value': list[i]})
    digdag.env.store({'params': json.dumps(result)})

