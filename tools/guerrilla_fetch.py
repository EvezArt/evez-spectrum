#!/usr/bin/env python3
"""EVEZ GUERRILLA FETCH — gorilla-grade proxy bypass ladder.
Routes around CloudFront geo-blocks, Cloudflare 403/451 walls, and UA blocks.
Every route is free-tier. Commandment 3 compliant.
VERIFIED 2026-10-03 by Cipher: Bybit direct 200 (BTC live), PHMSA 403->200 via jina-reader,
Wyoming Newspapers 451->200 via jina-reader, NTSB 200, Uinta County 200,
Church Buttes deleted-Wikipedia-article recovered via jina-reader."""
import sys, json, urllib.request, urllib.error, ssl

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36"
CTX = ssl.create_default_context(); CTX.check_hostname = False; CTX.verify_mode = ssl.CERT_NONE

def _get(url, timeout=20, ua=UA):
    req = urllib.request.Request(url, headers={"User-Agent": ua, "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
        return r.status, r.read().decode("utf-8", "ignore")

def r_direct(u):      return _get(u)
def r_jina(u):        return _get("https://r.jina.ai/" + u, ua="Mozilla/5.0")
def r_allorigins(u):  return _get("https://api.allorigins.win/raw?url=" + urllib.request.quote(u, safe=""))
def r_corsproxy(u):    return _get("https://corsproxy.io/" + urllib.request.quote(u, safe=""))
def r_wayback_live(u):
    api = "https://archive.org/wayback/available?url=" + urllib.request.quote(u, safe="")
    s, body = _get(api)
    snap = json.loads(body).get("archived_snapshots", {}).get("closest", {})
    if not snap: return 404, "no snapshot"
    return _get(snap["url"].replace("http://", "https://"))
def r_wayback_save(u):
    s, body = _get("https://web.archive.org/save/" + u, timeout=45)
    return s, body
def r_isomorphic(u):  return _get(u, ua="curl/8.5.0")

ROUTES = [("direct", r_direct), ("ua-flip", r_isomorphic), ("jina-reader", r_jina),
          ("allorigins", r_allorigins), ("corsproxy", r_corsproxy),
          ("wayback-snapshot", r_wayback_live), ("wayback-save", r_wayback_save)]

def guerrilla(url, want_status=None, min_bytes=50):
    log = []
    for name, fn in ROUTES:
        try:
            s, body = fn(url)
            ok = (want_status is None or s == want_status) and len(body) >= min_bytes
            log.append("%s -> %d (%d bytes)%s" % (name, s, len(body), " HIT" if ok else ""))
            if ok:
                return {"route": name, "status": s, "bytes": len(body), "log": log, "body": body}
        except urllib.error.HTTPError as e:
            log.append("%s -> HTTP %d" % (name, e.code))
        except Exception as e:
            log.append("%s -> %s" % (name, str(e)[:60]))
    return {"route": None, "status": 0, "bytes": 0, "log": log, "body": ""}

if __name__ == "__main__":
    url = sys.argv[1]
    res = guerrilla(url)
    print("ROUTE:", res["route"], "| STATUS:", res["status"], "| BYTES:", res["bytes"])
    for l in res["log"]: print("  ", l)
    print("---BODY HEAD---")
    print(res["body"][:400] if res["body"] else "(empty)")
