#!/usr/bin/env python3
"""Optional bounded LLM-assisted analysis of public-source research. NOT run by default.
Only public GitHub metadata and explicit analyst hypotheses are submitted, after CLI approval.
"""
import argparse
import json
import os
from pathlib import Path
import sys
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent

def build_request(audit: dict, model: str) -> dict:
    assert audit['report_status'].startswith('DRAFT'), 'input should remain review-pending'
    rows = audit['records']
    safe_rows = []
    for row in rows:
        url = row['source_url']
        assert url.startswith('https://github.com/') and '/' in url[19:], 'unexpected source URL'
        safe_rows.append({k: row[k] for k in ('repo', 'source_url', 'stars_snapshot', 'category', 'possible_buyer_HYPOTHESIS', 'pain_HYPOTHESIS', 'validation_question')})
    return {
        'model': model,
        'instructions': ('Act as a Product Ops research analyst. Use ONLY the supplied public metadata and labeled analyst hypotheses. '
            'Do not invent feature claims, user interviews, financial figures or confirmed customers. '
            'For each selected hypothesis cite a supplied exact source URL. '
            'Explain why GitHub stars alone do not establish demand, revenue or adoption. '
            'Produce (1) 3 buyer hypotheses, (2) 5 interview questions, '
            '(3) a 2-week experiment proposal with measurable metrics and risks, '
            '(4) an evidence-gaps list and human approval gates. Clearly mark hypotheses and uncertainties.'),
        'input': 'Research snapshot (public GitHub metadata + UNVERIFIED analyst hypotheses):\n' + json.dumps(safe_rows, ensure_ascii=False),
        'max_output_tokens': 1600,
        'store': False,
    }

def extract_text(payload: dict) -> str:
    if isinstance(payload.get('output_text'), str) and payload['output_text'].strip():
        return payload['output_text']
    chunks = []
    for entry in payload.get('output', []):
        for part in entry.get('content', []):
            if part.get('type') == 'output_text' and part.get('text'):
                chunks.append(part['text'])
    if not chunks:
        raise ValueError('Response contains no text')
    return '\n'.join(chunks)

def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument('--audit', type=Path, default=ROOT/'output'/'research_audit.json')
    p.add_argument('--out', type=Path, default=ROOT/'output'/'llm_hypotheses_DRAFT.md')
    p.add_argument('--confirm-share-public-metadata', action='store_true')
    args = p.parse_args(argv)
    if not args.confirm_share_public_metadata:
        p.error('Explicit --confirm-share-public-metadata required; sends public repository metadata to an LLM API')
    token = os.environ.get('OPENAI_API_KEY')
    model = os.environ.get('OPENAI_MODEL')
    if not token or not model:
        p.error('Set OPENAI_API_KEY and OPENAI_MODEL securely in your local environment first')
    audit = json.loads(args.audit.read_text(encoding='utf-8'))
    payload = build_request(audit, model)
    req = Request('https://api.openai.com/v1/responses',
        data=json.dumps(payload).encode('utf-8'),
        headers={'Content-Type':'application/json', 'Authorization':'Bearer '+token}, method='POST')
    with urlopen(req, timeout=45) as response:
        result = json.load(response)
    text = extract_text(result)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text('# LLM hypotheses — DRAFT / NOT FACT-CHECKED\n\n'
        '> Generated with an LLM from public GitHub metadata and analyst hypotheses. Human source checks required.\n\n'
        + text + '\n', encoding='utf-8')
    print(f'Wrote review-only draft to {args.out}')

if __name__ == '__main__':
    try: main()
    except (ValueError, AssertionError, OSError) as e:
        print(f'LLM stage stopped: {e}', file=sys.stderr)
        sys.exit(1)