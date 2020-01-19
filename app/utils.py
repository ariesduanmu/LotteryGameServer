# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2019-12-18 16:13:40
# @Last Modified by:   Li Qin
# @Last Modified time: 2019-12-25 13:36:44
from urllib.parse import unquote

def data_2_json(state, errmsg="ok", content=""):    
    return {"status_code":state, "errmsg":errmsg, "content":content}

def parse_qsl(qs):
    r = []
    for pair in qs.replace(';', '&').split('&'):
        if not pair: continue
        nv = pair.split('=', 1)
        if len(nv) != 2: nv.append('')
        key = unquote(nv[0].replace('+', ' '), encoding='utf8')
        value = unquote(nv[1].replace('+', ' '), encoding='utf8')
        r.append((key, value))
    return r

def touni(s, enc='utf8', err='strict'):
    if isinstance(s, bytes):
        return s.decode(enc, err)
    return unicode("" if s is None else s)