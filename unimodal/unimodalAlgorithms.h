#include <string>
#include "IIterationObserver.h"

namespace unimodal
{
    double FindMin(const std::string& function, const std::string& args,
                   double start, double end, double epsilon, IIterationObserver* observer = nullptr);
}
