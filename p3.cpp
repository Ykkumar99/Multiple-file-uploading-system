#include<bits/stdc++.h>
using namespace std;
class Graph
{
    int V; // No. of vertices

    vector<list<int>> adj;
public:
    Graph(int V); // Constructor
    void addEdge(int v, int w);
    
    void BFS(int s);
};
Graph::Graph(int V)
{
    this->V = V;
    adj.resize(V);
}
void Graph::addEdge(int v, int w)
{
    adj[v].push_back(w); // Add w to v’s list.
}
void Graph::BFS(int s)
{
    vector<bool> visited;
    visited.resize(V,false);
    list<int> queue;
    visited[s] = true;
    queue.push_back(s);

    while(!queue.empty())
    {
        s = queue.front();
        cout << s << " ";
        queue.pop_front();
        for (auto adjecent: adj[s])
        {
            if (!visited[adjecent])
            {
                visited[adjecent] = true;
                queue.push_back(adjecent);
            }
        }
    }
}
int main()
{
    // Create a graph given in the above diagram
    Graph g(7);
    g.addEdge(0, 1);
    g.addEdge(0, 3);
    g.addEdge(1, 2);
    g.addEdge(1,5);
    g.addEdge(2, 4);
    g.addEdge(2,6);
    g.addEdge(3,5);
    g.addEdge(4,1);
    g.addEdge(4,5);
    g.addEdge(5,0);
    g.addEdge(6,4);

    cout << "Following is Breadth First Traversal "
        << "(starting from vertex 2) \n";
    g.BFS(0);

    return 0;
}
