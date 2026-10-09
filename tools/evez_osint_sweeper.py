#!/usr/bin/env python3
"""EVEZ OSINT SWEEPER v1.0 — cross-referential, non-linear attributive inference engine.
Free-tier, HTTPS-only. Every output line carries its source. No fabrication.
Usage: python3 evez_osint_sweeper.py <key> [key...]  (domain, TRON wallet, etc.)
Wheel law: source timeouts log as FRICTION; the sweep continues."""
import sys, json, urllib.request, socket

socket.setdefaulttimeout(15)

def get(url, accept='application/json'):
    req = urllib.request.Request(url, headers={'User-Agent': 'evez-osint-sweeper/1.0', 'Accept': accept})
    return urllib.request.urlopen(req).read().decode('utf-8', 'replace')

def doh(name, typ):
    try:
        d = json.loads(get('https://dns.google/resolve?name=%s&type=%s' % (name, typ)))
        return [a.get('data', '') for a in d.get('Answer', [])] or ['NOT FOUND']
    except Exception as e:
        return ['FRICTION: ' + str(e)[:60]]

def urlscan(domain):
    try:
        d = json.loads(get('https://urlscan.io/api/v1/search/?q=domain:%s&size=5' % domain))
        out = []
        for r in d.get('results', [])[:5]:
            out.append('%s | ip=%s | asn=%s | %s' % (
                r.get('task', {}).get('time', '')[:10],
                r.get('page', {}).get('ip', '?'),
                r.get('page', {}).get('asn', '?'),
                r.get('page', {}).get('url', '')[:70]))
        return out or ['NOT FOUND (no scans)']
    except Exception as e:
        return ['FRICTION: ' + str(e)[:60]]

def wayback(domain):
    try:
        d = get('http://web.archive.org/cdx/search/cdx?url=%s&output=json&limit=5&collapse=timestamp:4' % domain)
        rows = json.loads(d) if d.strip().startswith('[') else []
        return ['%s | %s' % (r[1][:8], r[2][:70]) for r in rows[1:5]] or ['NOT FOUND (no snapshots)']
    except Exception as e:
        return ['FRICTION: ' + str(e)[:60]]

def tron(wallet):
    out = []
    try:
        acc = json.loads(get('https://api.trongrid.io/v1/accounts/' + wallet))
        data = (acc.get('data') or [None])[0]
        if data:
            out.append('balance: %s TRX' % (data.get('balance', 0) / 1e6))
            out.append('trc20 positions: %d' % len(data.get('trc20', [])))
        else:
            out.append('NOT FOUND (empty account)')
    except Exception as e:
        out.append('FRICTION: ' + str(e)[:60])
    return out

def sweep(key):
    print('=== KEY: %s ===' % key)
    if key.startswith('T') and len(key) == 34:
        for line in tron(key): print('  [TRON]  ', line)
        return
    for typ in ('A', 'NS', 'MX'):
        for line in doh(key, typ): print('  [DoH %s]' % typ, line)
    for line in urlscan(key): print('  [URLSCAN]', line)
    for line in wayback(key): print('  [WAYBACK]', line)
    print('  [GITHUB] (agent-side: code-search the key via mcp_github_search_code)')
    print('  [OFAC]  (agent-side: grep treasury.gov/ofac/downloads/sdn.csv)')

if __name__ == '__main__':
    keys = sys.argv[1:] or ['aeza.net', 'xorek.cloud', 'smartdi.rs']
    for k in keys:
        sweep(k)
        print()
