#include <atomic>
#include <ppl.h>

std::atomic<int> value(0);

int create_id()
{
    return std::atomic_fetch_add(&value, 1);
}

extern "C" __declspec(dllexport) void colorsearch(unsigned char *pic, unsigned char *colors, int width, int totallengthpic, int totallengthcolor, int *outputx, int *outputy, int *lastresult)
{
    value = 0;
    concurrency::parallel_for(0, totallengthcolor / 3 + 1, [&](int i)
                              {
        int r = colors[(i * 3)];
        int g = colors[(i * 3 + 1)];
        int b = colors[(i * 3 + 2)];
        for (int j =0; j <= totallengthpic; j+=3){
            if ((r == pic[j]) && (g == pic[j + 1]) && (b == pic[j + 2])){
                int dividend = (j / 3);
                int quotient = (dividend / width);
                int remainder = (dividend % width);
                int upcounter = create_id();
                outputx[upcounter] = quotient;
                outputy[upcounter] = remainder;
                lastresult[0] = upcounter;
            }
        } });
}
