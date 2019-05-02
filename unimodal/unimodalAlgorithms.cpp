#include <fparser.hh>
#include <cmath>
#include "unimodalAlgorithms.h"

template<>
int FunctionParserBase<double>::Parse(const std::string&, const std::string&, bool);

template<>
double FunctionParserBase<double>::Eval(const double*);

double unimodal::FindMin(const std::string& function, const std::string& args,
                         double start, double end, double epsilon, IIterationObserver* observer)
{
    FunctionParser parser;
    const int res = parser.Parse(function, args);

    if (res >= 0)
    {
        throw std::runtime_error("Invalid function input.");
    }

    if (start >= end || std::abs(end - start) < epsilon)
    {
        throw std::runtime_error("Invalid bounds.");
    }

    unsigned it = 0;
    while (std::abs(end - start) > epsilon)
    {
        const double x = (end + start) / 2;
        const double values[] = { x - epsilon, x + epsilon };
        if (parser.Eval(values) < parser.Eval(values + 1))
        {
            end = x;
        }
        else
        {
            start = x;
        }

        if (observer != nullptr)
        {
            observer->OnNewIteration(++it, start, end);
        }
    }

    return (start + end) / 2;
}
