class SegmentTree:
    def __init__(self, size):
        self.n = size
        self.min_val = [float('inf')] * (4 * size)
        self.max_val = [float('-inf')] * (4 * size)
        self.lazy = [0] * (4 * size)

    def _push(self, node):
        if self.lazy[node] != 0:
            lazy_val = self.lazy[node]
            self.min_val[2 * node] += lazy_val
            self.max_val[2 * node] += lazy_val
            self.lazy[2 * node] += lazy_val
            self.min_val[2 * node + 1] += lazy_val
            self.max_val[2 * node + 1] += lazy_val
            self.lazy[2 * node + 1] += lazy_val
            self.lazy[node] = 0

    def _update(self, node, start, end, l, r, val):
        if r < start or end < l:
            return
        if l <= start and end <= r:
            self.min_val[node] += val
            self.max_val[node] += val
            self.lazy[node] += val
            return
        
        self._push(node)
        mid = (start + end) // 2
        self._update(2 * node, start, mid, l, r, val)
        self._update(2 * node + 1, mid + 1, end, l, r, val)
        
        self.min_val[node] = min(self.min_val[2 * node], self.min_val[2 * node + 1])
        self.max_val[node] = max(self.max_val[2 * node], self.max_val[2 * node + 1])

    def _set_leaf(self, node, start, end, idx, val):
        if start == end:
            self.min_val[node] = val
            self.max_val[node] = val
            self.lazy[node] = 0
            return
        
        self._push(node)
        mid = (start + end) // 2
        if idx <= mid:
            self._set_leaf(2 * node, start, mid, idx, val)
        else:
            self._set_leaf(2 * node + 1, mid + 1, end, idx, val)
            
        self.min_val[node] = min(self.min_val[2 * node], self.min_val[2 * node + 1])
        self.max_val[node] = max(self.max_val[2 * node], self.max_val[2 * node + 1])

    def _find_first_zero(self, node, start, end):
        if not (self.min_val[node] <= 0 <= self.max_val[node]):
            return -1
            
        if start == end:
            return start
        
        self._push(node)
        mid = (start + end) // 2
        
        res = self._find_first_zero(2 * node, start, mid)
        if res != -1:
            return res
        return self._find_first_zero(2 * node + 1, mid + 1, end)

    def update_range(self, l, r, val):
        self._update(1, 0, self.n - 1, l, r, val)
        
    def activate_index(self, idx):
        self._set_leaf(1, 0, self.n - 1, idx, 0)
        
    def find_leftmost_zero(self):
        return self._find_first_zero(1, 0, self.n - 1)

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        st = SegmentTree(n)
        
        max_val = max(nums)
        last_seen = [-1] * (max_val + 1)
        
        ans = 0
        
        for r in range(n):
            val = nums[r]
            st.activate_index(r)
            change = 1 if (val % 2 == 0) else -1
            prev = last_seen[val]
            st.update_range(prev + 1, r, change)
            last_seen[val] = r
            l = st.find_leftmost_zero()
            if l != -1:
                ans = max(ans, r - l + 1)
                
        return ans