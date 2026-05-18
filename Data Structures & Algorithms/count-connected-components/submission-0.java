class DSU {
    int[] parent;
    int[] rank;

    public DSU(int n) {
        parent = new int[n];
        rank = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            rank[i] = 1;
        }
    }

    /*
    For a node, find its root parent. Recall that, initially each
    node's root parent is itself. We need this find() function for
    the union() function to work.

    We need the root parent, as that is what defines the union()
    function, and the height of a component and whether it can be
    merged with another vertex.
    */
    public int find(int node) {
        // Let curr equal the node that was passed in.
        int curr = node;
        // Can stop searching once we reach the top node which is
        // its own parent.
        while (curr != parent[curr]) {
            // Set the parent of curr to it's grandparent.
            // A slight optimization which would make it faster.
            // We can now reach the root parent faster, our base case.
            parent[curr] = parent[parent[curr]];
            // The above line won't cause an error, it will just not
            // run and skip to the line below.
            curr = parent[curr];
        }
        return curr;
    }

    /*
    Take 2 nodes and Union their components together. Our first task
    is to find their ROOT parents. The absolute top of the chain!

    Then using the root parents, we can go ahead and merge them
    together.

    This union() and find() concept is more so the same, but can the
    design can vary depending on the question.

    From the two parents we find. The one with the greater RANK will
    be the parent from the two. To update parent we will use the
    parent array up top.
    */
    public int union(int n1, int n2) {
        int p1 = find(n1);  // these 'parents' are numbers in our chain
        int p2 = find(n2); // but their rank is stored in another array

        if (p1 == p2) {
            return 0;
        } else if (rank[p2] > rank[p1]) {
            parent[p1] = p2;
            // increase rank of p2, since we are adding children to it
            rank[p2]++;
        } else if (rank[p1] > rank[p2]) {
            parent[p2] = p1;
            rank[p1]++;
        }
        return 1;
    }
}

/*
Initially we start out with n different components, as each root is
on its own.
*/
class Solution {
    public int countComponents(int n, int[][] edges) {
        // this graph
        int res = n;
        DSU dsu = new DSU(n);
        for (int[] edge : edges) {
            res -= dsu.union(edge[0], edge[1]);
        }
        return res;
    }
}
