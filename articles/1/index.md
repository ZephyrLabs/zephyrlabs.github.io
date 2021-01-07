# prime bench, 
## the insights shown by this simple benchmark tool..

### what is prime bench ?
prime bench is a simple benchmark tool, part of my set of programs in the crinkle bench repository I made, to see how fast a processer could calculate the number of prime numbers within a given range, 
specificallly how good one single core from the processer could do it..

this bench has been slightly conterversial to me for the way it has shown results across the table, 
and shows to the naked eye, that there is more to a processer's performance than just simple clockspeed or architecture,

### how does this benchmark work ?

the source code is available on github (via) this [link](https://github.com/ZephyrLabs/Crinkle-bench/prime_bench/)

let's go over more about the benchmark itself:
> it is a standard algorithim to check if a number is a prime number, but checking the divisibility of the number with all the numbers behind it
> it doesn't check all the numbers behind it, rather checks half of the numbers behind the number being checked from 0 to the mid way point..
> eg. to check if 97 is a prime, it rounds to the nearest half point, which is 49, and checks if 97 is divisible from 0 to 47 onwards...
> if it finds one number that is divisible, it will immediately stop checking for that number, assumes its a composite number, and move on to the next number..

calculating primes is takes a logarithmic path, where increasing the limit for finding primes leads to testing exponential amount of numbers..

this can be seen with the count of numbers that need to be checked with the increase in the number limit

maximum count of numbers to test = (n*(n+1))/4

```
eg, the approximate number of primes to be checked from 2 to 100 = 9900/4 = 2475, and 
the approximate number of primes to be checked from 2 to 1000 = 999000/4 = 249750
```

### that's 100x more numbers to check for just a 10x limit increase!


last but not least.. for choice of programming language, 
the program is made in C++ for its speed and minimal overhead,
unlike with other languages, which may be interpreted, 
those would take much longer and would be much more innaccurate, as it would be a test to the interpreter, not the program itself..

## time to test drive the program!

to test this program, I used my main work laptop, as well as some single board computers, and with a help of some volunteers, even tested it on the new M1 SoC from apple ! 

the standard search limit selected was 1 million,
and the scores may slightly surprise you.. 

``` please note, all tests ran single threadded !!!```

in the **x86_64** systems tested..

1st test, **Intel i3-1005G1:**
`completed in 35 seconds`

2nd test, **Intel i5-8300H:**
`completed in 44 seconds`

3rd test, **AMD ryzen 5 3600:**
`completed in 45 seconds`

in the **ARM** systems tested..

1st test, **Allwinner A64:**
`completed in 120 seconds`

2nd test, **Rockchip RK3399:**
`completed in 72 seconds`

3rd test, **Amlogic A311D:**
`completed in 41 seconds`

4th test, **Qualcomm Snapdragon 820:**
`completed in 22 seconds`

5th test, **Apple M1:**
`completed in 7 seconds`

and for fun, we slightly modifed the code, to run on some **Arduino** compatible boards

1st test, **Arduino Uno:** 
`completed in 240 seconds`

2nd test, **Espressif ESP32:**
`completed in 10 seconds`

the scores seem to be all over the place, and the number make no sense at first glance,

**"how can an i3 surpass an i5 and even a desktop class ryzen 5"** or, 

**" how could an ESP32 do it faster than an ARM Single board computer running at nearly 10x its clock frequency?!"**

and the answers have some real depth to them.., 
remember, prime bench is program made to show how fast a processer can calculate prime numbers, 

and to surpass this benchmark, a processer must have:
* fast clock speeds  
* an efficent architecture, the more the basic instruction set, the better, and finally
* plentifuls of cache and CPU/memory integrity

and already a lot can be made from these three points,

take a look at the tests conducted for the **x86** systems,

the i3-1005G1 is part of the latest intel core processer series for mobile compute, 
and has the shiniest bells and whistles such as AVX-512 support and SSE2 etc.
i.e SIMD instructions for faster vector computing..

when these things are utilized during compiling, the resultant program is highly optimised for performance and is able to out perform the i5 and ryzen 5 3600 of yester year..

for the **ARM** systems,
the M1 SoC was the brain child of Apple's silicon technology,
and had the latest of ARM technology, such as ARMv8.6 ISA etc

and has some outstanding peformance in natively compiled programs, as well as programs virtualised in Rosetta 2 translation layer..

now, these things didn't really give it any significant gain in performance, rather the indirect things that helped to push to its performance, like the having plentiful of cache for ARM's out-of-order execution model etc.

the Snapdragon 820, being slightly older, still had excellent performance, and still beat every **x86** system tested, by a very long margin..

another startling thing was that the A311D and RK3399, both having cores, that are by design SUPPOSED to outperform the SD820, actually underperformed!

I will cover this part in my next article, but it seems to show a flaw in the design of these chips, that seem to be very detrimental to the performance shown here..

but a key eye opener, that was observed was with the ESP32 running arduino,
### how could a tiny microcontroller beat out 90% of all these tested systems !?

there are 2 things that contributed to this performance gain,
* the lightweight arithmetic part of the instruction set, and 
* the key tweak made in the Arduino port of this program..

the key tweak made was, disabling a flag and compare check in the prime checking part of the program, 

this seems like cheating a bit, 
but do be reminded that these are microcontrollers, and do not have dedicated MMU (memory management units) like with the processers tested,

normal processers could move the data without a problem, due to their superiority of having dedicated memory management, hence to level the playing field 
the key part that handicapped the chip, was removed, unlocking its speed, and allowing it to crunch numbers faster, 

> after all, the program is made to test the computing limits of the chip, and was not to test the cache integrity, 

> the cache integrity, was only a key factor for the processer to shine

I will do more testing to see what more can be uncovered from this amazing insight..
