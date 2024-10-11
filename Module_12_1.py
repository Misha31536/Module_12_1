import unittest
import runner as r
class RunnerTest(unittest.TestCase):

    def test_walk(self):
        m1 = r.Runner("member1")
        for _ in range(10):
            m1.walk()
        self.assertEqual(m1.distance, 50)
    def test_run(self):
        m2 = r.Runner("member2")
        for _ in range(10):
            m2.run()
        self.assertEqual(m2.distance, 100)
    def test_challenge(self):
        m3 = r.Runner("member3")
        m4 = r.Runner("member4")
        for _ in range(10):
            m3.walk()
            m4.run()
        self.assertNotEqual(m3.distance, m4.distance)



