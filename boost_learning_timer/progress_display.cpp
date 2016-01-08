#include <boost/progress.hpp>
#include <iostream>
#include <vector>
#include <fstream>

int main(){
    std::vector<int> v(100);
    std::ofstream fs("./test.txt");
    boost::progress_display pd(v.size());
    for(auto & x : v){
        fs << x << std::endl;
        ++pd;
    }
    return 0;
}

