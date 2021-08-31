from kth_largest import Solution
from unittest import TestCase
class TestSolution(TestCase):
    def test_findkth(self):
        s = Solution()
        out = s.findKthLargest([4,5,63,2,1,-21], 1)
        self.assertEqual(out, 63)
