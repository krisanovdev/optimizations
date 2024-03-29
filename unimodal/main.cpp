#include <iostream>
#include "unimodalAlgorithms.h"

template <class T>
T SafeGet()
{
    T x;
    while(!(std::cin >> x))
    {
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        std::cout << "Invalid input. Try again: ";
    }

    return x;
}

class ConsoleIterationObserver : public unimodal::IIterationObserver
{
public:
    virtual void OnNewIteration(unsigned iterationNumber, double newA, double newB) override
    {
        std::cout << "Iteration " << iterationNumber << ": a=" << newA << " b=" << newB << std::endl;
    }
};

int main()
{
    try
    {
        std::string function;
        std::cout << "f(x) = ";
        std::getline(std::cin, function);

        if(std::cin.fail())
        {
            throw std::runtime_error("Unsuported syntax.");
        }

        std::cout << "left bound: ";
        const double leftBound = SafeGet<double>();
        std::cout << "right bound: ";
        const double rightBound = SafeGet<double>();
        std::cout << "epsilon: ";
        const double epsilon = SafeGet<double>();

        ConsoleIterationObserver observer;
        const double res = unimodal::FindMin(function, "x", leftBound, rightBound, epsilon, &observer);
        std::cout << "x=" << res << std::endl;
    }
    catch(const std::exception& ex)
    {
        std::cout << ex.what() << std::endl;
    }

    system("pause");
    return 0;
}
