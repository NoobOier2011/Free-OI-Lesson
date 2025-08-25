struct BIT {
    vector<int> Tree;
    int n;

    int lowbit(int n) { 
        return n & -n;
    }

    int query_1_n(int n) {
        int ans = 0;
        while(n != 0) {
            ans += Tree[n];
            n -= lowbit(n);
        }
        return ans;
    }

    void init(int size) {
        Tree.resize(size+10);
        n = size;
    }

    void update(int i,int x) {
        while(i <= n) {
            Tree[i] += x;
            i += lowbit(i);
        }
    }

    int query(int l,int r) {
        return query_1_n(r)-query_1_n(l-1);
    }
};