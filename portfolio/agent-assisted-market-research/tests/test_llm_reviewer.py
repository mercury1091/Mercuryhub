import sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import llm_reviewer as l
import research_agent as a
class TestLLM(unittest.TestCase):
 def setUp(self):
  self.audit=a.brief(a.collect(a.validate_targets(a.read_json(ROOT/'data/targets.json')),'fixture',ROOT/'data/github_snapshot.json'))
 def test_only_public_metadata_in_request(self):
  data=l.build_request(self.audit,'test-model')
  self.assertIn('https://github.com/', data['input'])
  self.assertNotIn('OPENAI_API_KEY',data['input'])
  self.assertFalse(data['store'])
 def test_rejects_unsafe_url(self):
  self.audit['records'][0]['source_url']='https://invalid-domain.com/example'
  with self.assertRaises(AssertionError):l.build_request(self.audit,'test-model')
 def test_extract_responses_api_text(self):
  self.assertEqual(l.extract_text({'output':[{'content':[{'type':'output_text','text':'draft review'}]}]}),'draft review')
if __name__=='__main__':unittest.main()