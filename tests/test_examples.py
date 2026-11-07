import csv
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEMO = ROOT / 'skills/sales-prospecting/examples/fictional-campaign'

class SalesFixtureTests(unittest.TestCase):
    def load(self, name):
        with (DEMO / name).open(newline='') as f:
            return list(csv.DictReader(f))

    def test_no_reachable_contacts(self):
        contacts = self.load('contacts.csv')
        self.assertTrue(contacts)
        self.assertTrue(all(not r['work_email'] for r in contacts))
        self.assertTrue(all(r['email_verification'] != 'verified' for r in contacts))

    def test_no_send_or_outreach_permission(self):
        events = self.load('activity.csv')
        self.assertTrue(events)
        self.assertTrue(all(r['event_type'] == 'draft_created' and r['outcome'] == 'unsent' for r in events))
        self.assertTrue(all(not r['message_id'] for r in events))

    def test_reserved_demo_domains(self):
        companies = self.load('companies.csv')
        self.assertEqual({r['company_domain'] for r in companies}, {'example.org'})

if __name__ == '__main__':
    unittest.main()
