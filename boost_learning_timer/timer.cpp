#include <boost/timer.hpp>
#include <iostream>

using namespace boost;

int main(){
    timer t;
    std::cout<< "max timespan:"
                << t.elapsed_max() / 3600 <<"h"<<std::endl;
    std::cout<< "min timespan:"
                <<t.elapsed_min() << "s"<<std::endl;
    std::cout<<"now time elapsed:"
               <<t.elapsed() <<"s"<<std::endl;

    return 0;
}
