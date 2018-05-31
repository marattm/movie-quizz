# services/quizz/project/tests/test_quizz.py
import json
import unittest


from flask_testing import TestCase

from project.tests.base import BaseTestCase


class TestQuizzService(BaseTestCase):
    """Tests for the Quizz Service."""

    def test_quizz_ping(self):
        """Ensure that the ping behave correctly."""
        rv = self.client.get('/quizz/ping')
        data = json.loads(rv.data.decode())
        self.assertTrue('success', data['status'])
        self.assertTrue('pong', data['message'])
        self.assertEqual(rv.status_code, 200)
