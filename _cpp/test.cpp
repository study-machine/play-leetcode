#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char const *argv[])
{
    int arr[5]={1, 2, 3, 4, 5};
    vector<int> v(arr,arr+5);
    v[6]=100;
    for (std::vector<int>::iterator i = v.begin(); i != v.end(); ++i)
    {
        cout<<*i;
    }


    return 0;
}