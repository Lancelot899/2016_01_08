#include <iostream>
#include <boost/progress.hpp>


int main(){
    boost::progress_timer t;
    int f1(1), f2(1);
    int f(0);
    for(int i = 0; i < 10000000; i++){
        f = f1 + f2;
        f1 = f2;
        f2 = f;
    }
    std::cout << "after 10000000, the f is " << f << std::endl;
    return 0;
}

