# Course 01 Notes

Learning Objectives
What hardware support is needed?
How does the OS do this efficiently?
What OS mechanisms and policies support virtualization?
How does an OS virtualize resources?
What is an operating system?
Describe the basics of a C program
Compile and execute a C program
Leverage flags to provide more information about your program
Link your program to different libraries
Differentiate between static and dynamic linked libraries
Compile and execute a program separated across several files
Automate the build process with make
Debug your program with an interactive debugger

Course Introduction
What is an Operating System?
The operating system (OS) is a piece of software that ensures the system runs smoothly and efficiently.
An operating system makes it easy to run programs (even allowing you to seemingly run many at the same time) by allowing programs to share memory and enabling programs to interact with hardware.
Up until now, you probably have run code in an IDE of some kind (or from the command line) without considering how it interacted with hardware.
Consider your program a set of instructions to be run by your computer:
.guides/img/CPUrole
Millions (even billions) of times each second, the processor or CPU:
Fetches an instruction,
Decodes it (i.e., figures out which instruction this is), and
Executes it.
This repeats for each instruction until the program is finished.
This is a pretty simplistic view of what is happening under-the-hood. While a program is running, many other things are happening, controlled by the OS, to make the system easier to use.

Which of the following statements describe an Operating System?


It is a piece of software that makes sure the system runs smoothly and efficiently.


It is responsible for allowing programs to share memory.


It is responsible for enabling programs to interact with devices.


All of the Above.


None of the Above.

The operating system has a variety of responsibilities. These include, but are not limited to:

Ensuring the system runs smoothly and efficiently
Allowing programs to share memory resources
Allowing programs to interact with various devices
The correct answer is All of the Above.


Theme 1: Virtualization
One component of how the OS makes things easier to use is virtualization or the transformation of a physical resource (such a processor, memory, or disk) into a more general, powerful, and user-friendly virtual form.
Because virtualization allows many programs to run simultaneously (sharing the CPU), access their own instructions and data (sharing memory), and access devices (sharing storage, etc. ), the OS is commonly referred to as a resource manager.
Example: CPU Virtualization
With help from the hardware, the operating system creates the illusion of having a bunch of virtual CPUs.
The program to the left, cpu.c, prints the input string, waits 5 seconds, and repeats forever.
First, let’s run this program as if it were running on a single-processor system, passing the string “One” as input.
Click the button below:
Run One Program
You should see the following output in the terminal on the bottom-left:
One
One
One
One
...
This program will run forever, so type ^+C (by pressing the Ctrl and C keys at the same time) to terminate the program.
Running Several Programs
This time, let’s run four instances of the same program:
Run Four Programs
Your output should look something like this:
[1] 1389
[2] 1390
[3] 1391
[4] 1392
One
Two
Three
Four
One
Two
Three
Four
One
Two
Three
Four
...
Even though we only have one CPU, all four programs seem to be operating simultaneously! How does it work?
With help from the hardware, the operating system creates the illusion of having a bunch of virtual CPUs.
This virtualizing of the CPU, allows several applications to run simultaneously on a single CPU (or a limited collection of them), is the subject of our first course.
We’ll use the pkill command to terminate all instances of the cpu program:
Send pkill cpu command
To execute applications, stop them (such as above), or otherwise instruct the OS which programs to run, certain interfaces (APIs) must be available. These are how most users interact with operating systems.
Complete the paragraph below with the appropriate vocabulary

Through 
virtualization
, the operating system abstracts physical hardware into simplified representations.
These representations are accessed through 
interfaces
The operating system handles these requests, acting as a 
resource manager
Through virtualization, the operating system abstracts physical hardware into simplified representations. These representations are accessed through interfaces. The operating system handles these requests, acting as a resource manager.

Check It!


#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <sys/stat.h>

double getTime() {
    struct timeval t;
    gettimeofday(&t, NULL);
    return (double) t.tv_sec + (double) t.tv_usec/1e6;
}

void wait(int howlong) {
    double t = getTime();
    while ((getTime() - t) < (double) howlong)
      ; //wait...
}

int main(int argc, char *argv[])
{
    char *str = argv[1]; //string we passed

    while (1) {
      printf("%s\n", str);
      wait(5);
    }
    return 0;
}

codio@editormercury-ponchojester:~/workspace$ ./cpu "One"
One
One
One
One
One
^C
codio@editormercury-ponchojester:~/workspace$ ./cpu "One" & ./cpu "Two" & ./cpu "Three" & ./cpu "Four" &
[1] 136
[2] 137
[3] 138
[4] 139
One
Three
Four
codio@editormercury-ponchojester:~/workspace$ Two
One
Three
Four
Two
One
Three
Four
Two
One
Three
Four
Two
Three
One
Four
Two
Three
One
Four
Two
pkill cpu
[1]   Terminated              ./cpu "One"
[2]   Terminated              ./cpu "Two"
[3]-  Terminated              ./cpu "Three"
[4]+  Terminated              ./cpu "Four"
codio@editormercury-ponchojester:~/workspace$ 