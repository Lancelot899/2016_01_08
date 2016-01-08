#include <iostream>
#include <boost/date_time/gregorian/gregorian.hpp> //! operate the data
#include <boost/date_time/posix_time/posix_time.hpp> //! operate the time

int main(){
    boost::gregorian::date d1;
    boost::gregorian::date d2(2016, 1, 8);
    boost::gregorian::date d3(2015, boost::gregorian::Jan, 8);
    boost::gregorian::date d4(d2);
    if(d1 == boost::gregorian::date(boost::gregorian::not_a_date_time))
        std::cout << "d1 is a invalidable time" << std::endl;
    if(d2 == d4)
        std::cout << "d2 and d4 are the same date" << std::endl;
    if(d3 < d4)
        std::cout << "d3 is the day before d4" << std::endl;

    //boost::gregorian::date d5(boost::gregorian::from_string("1992-12-07"));
    // boost::gregorian::date d6 (boost::gregorian::from_string("1992/12/07"));
    boost::gregorian::date d7(boost::gregorian::from_undelimited_string("19921207"));


    return 0;

}

