namespace unimodal
{
    class IIterationObserver
    {
    public:
        virtual ~IIterationObserver(){}
        virtual void OnNewIteration(unsigned iterationNumber, double newValue) = 0;
    };
}

