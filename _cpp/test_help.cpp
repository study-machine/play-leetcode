#include <iostream>
#include <vector>

using namespace std;
void print_arr(vector<int> v){
    cout<<"print:";
    for (int i = 0; i < v.size(); ++i)
    {
        cout<<v[i]<<" ";
    }
    cout<<endl;
}