README:
In implementing the parallel function of srt, I found it difficult to understand
what the code was initially doing. I tried to first parallelize the
halfsample loops within the pixel loops but I eventually realized it was
easier to just parallelize the pixels that are processed (i.e. so that each
thread would work on a specifi column of pixels). I also had difficulty
figureing out how to pass all the things i needed to the funciton.
Initially, I just created a struct of a bunch of different variables, but
I eventually found it easier and less wordy to just declare those
variables within the thread function. I also didnt really
understand how the image was actually being generated and it took  several
readthroughs to figure out that it was printing out the color floats.
Once i realized this, i made a global 3d array so each thread could just
write to that and then i would print out that array in the main thread.

Based on my observations of make check, it appears that the multithreaded
srt is much faster than the single threaded sort. Doubling the number
of threads almost halves the time it takes for the function to run. 
