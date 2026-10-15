import copy
import sys
import tempfile
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import research_agent as a

class TestResearch(unittest.TestCase):
    def setUp(self):
        self.targets = a.validate_targets(a.read_json(ROOT / 'data/targets.json'))
        self.snapshot = ROOT / 'data/github_snapshot.json'
        self.obs = a.collect(self.targets, 'fixture', self.snapshot)

    def test_all_entries_collected(self):
        self.assertEqual(len(self.obs), 10)
        self.assertEqual(len(a.brief(self.obs)['records']), 10)

    def test_no_doubled_targets(self):
        dup = self.targets + [self.targets[0]]
        with self.assertRaises(ValueError): a.validate_targets(dup)

    def test_invalid_slug(self):
        x = copy.deepcopy(self.targets)
        x[0]['repo'] = '../private_data'
        with self.assertRaises(ValueError): a.validate_targets(x)

    def test_mismatched_source_url_fails(self):
        x = copy.deepcopy(self.obs[0]['source'])
        x['html_url'] = 'https://github.com/another/repo'
        with self.assertRaises(ValueError): a.validate_observation(x, self.targets[0]['repo'])

    def test_negative_stars_fail(self):
        x = copy.deepcopy(self.obs[0]['source'])
        x['stargazers_count'] = -1
        with self.assertRaises(ValueError): a.validate_observation(x, self.targets[0]['repo'])

    def test_hypothesis_and_approval_boundary(self):
        result = a.brief(self.obs)
        self.assertIn('HYPOTHESIS', str(result['records'][0]))
        self.assertFalse(result['approval_gate']['publishing_allowed'])
        self.assertFalse(result['approval_gate']['messaging_allowed'])
        self.assertEqual(result['next_experiment']['status'], 'PROPOSED ONLY — not executed')

    def test_markdown_provenance(self):
        out = a.markdown(a.brief(self.obs))
        self.assertIn('https://github.com/n8n-io/n8n', out)
        self.assertIn('Stars/Forks', out)
        self.assertIn('No external messaging', out)

    def test_cli_writes_files_without_network(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = a.run(['--mode','fixture','--out',tmp])
            self.assertTrue((Path(tmp)/'market_landscape.md').exists())
            self.assertEqual(a.read_json(Path(tmp)/'research_audit.json')['sources'], 10)

if __name__ == '__main__': unittest.main()