class Solution {
    public int[] findRedundantConnection(int[][] edges) {
        // length of n will create an array with indices till n - 1
        // BUT LENGTH OF n + 1 will create an array with indices till n
        // We want this n index, since we have an nth Node. The question
        // says that there are nodes from 1 to n, so our array must have
        // all those indices.
        
        // We will only use indices/nodes from 1 to n. The index/node 0
        // will be unused.
        int[] par = new int[edges.length + 1];
        int[] rank = new int[edges.length + 1];
        for (int i = 0; i < par.length; i++) {
            par[i] = i;
            rank[i] = 1;
        }

        for (int[] edge : edges) {
            if (!union(par, rank, edge[0], edge[1])) {
                return new int[]{edge[0], edge[1]};
            }
        }
        // If all edges are fine and we can't find the one which unions/merges
        // two nodes that are already connected. In that case, we just return
        // an empty array.
        return new int[]{};
    }

    private int find(int[] par, int n) {
        int p = par[n];
        while (p != par[p]) { // While not root node. Meaning the parent of the node is the node itself.
            par[p] = par[par[p]]; // Speeding up by making the parent into grandparent.
            p = par[p]; // Making the node into parent Node and then leaving the loop.
        }
        return p;
    }

    // parent is found from the parent array, through the index. Index i has i's parent Node.
    private boolean union(int[] par, int[] rank, int n1, int n2) {
        int p1 = find(par, n1);
        int p2 = find(par, n2);

        if (p1 == p2) {
            return false;
        }

        if (rank[p1] > rank[p2]) {
            par[p2] = p1;
            rank[p1] += rank[p2];
        } else if (rank[p2] > rank[p1]) {
            par[p1] = p2; // making p2 the parent of p1
            rank[p2] += rank[p1];
        } else {
            // since rank is equal we choose any arbitrary one as parent
            par[p2] = p1;
            rank[p1] += rank[p2];
        }
        return true;
    }
}
