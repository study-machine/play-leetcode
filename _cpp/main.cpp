//
//#include "run.h"
//
//
//
//int main(int argc, char const *argv[]) {
//    run_220();
//    return 0;
//}

#include <iostream>
#include <chrono>
#include <random>
#include <algorithm>
#include <functional>
using namespace std;

int main()
{
    int scene[9][9] = { 0 };

    //随机生成一行1~9
    auto init = [](int* list)
    {
        for_each(list, list + 9, [=](int &i) {i = &i - list + 1; });
        unsigned seed = chrono::system_clock::now().time_since_epoch().count();
        shuffle(list, list + 9, default_random_engine(seed));
    };
    init(scene[0]);  //初始化第一行
    int trylist[9];
    init(trylist);  //用于数字的尝试顺序

    //判断填入的数字是否合法
    auto judge = [&scene](int i, int j, int num) -> bool
    {
        //判断行相同
        for (int k(0); k < j; k++)
            if (scene[i][k] == num)
                return false;
        //判断列相同
        for (int k(0); k < i; k++)
            if (scene[k][j] == num)
                return false;
        //判断区域相同
        int count = j % 3 + i % 3 * 3;
        while (count--)
            if (!(scene[i - i % 3 + count / 3][j - j % 3 + count % 3] - num))
                return false;
        return true;
    };

    //简单回溯方法填入数字
    function<bool(int, int, int*)> fill = [&trylist, &fill, &scene, judge](int y, int x, int* numloc) -> bool
    {
        if (y > 8)
            return true;
        if (judge(y, x, *numloc))
        {
            scene[y][x] = *numloc;
            if (fill(y + (x + 1) / 9, (x + 1) % 9, trylist))
                return true;
        }
        scene[y][x] = 0;
        if (numloc - trylist >= 8)
            return false;
        if (fill(y, x, numloc + 1))
            return true;
    };

    fill(1, 0, trylist);
    //输出
    for (int i(0); i < 9; i++)
    {
        for (int j : scene[i])
            cout << j << " ";
        cout << endl;
    }
    return 0;
}