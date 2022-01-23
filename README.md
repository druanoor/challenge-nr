# challenge-nr
New Relic Coding Challenge

## How to run your program

The program has been written using Python3. To execute the program just execute the following: (there are more examples on the runMe.sh file)

python3 app.py [book path]
Example:
    python3 app.py text-examples/moby-dick.txt

To run the tests:

python3 test.py text-examples/moby-dick.txt

## What would you do next, given more time (if anything)?

Implement concurrecy using threads (one thread per book in argv, or splitting the input from STDIN into multiple strings consumed by different threads)

## Are there bugs that you are aware of?

Yes, my output when running the moby-dick.txt book differs a little bit from the example. I'm pretty sure it's because a punctuation character that i couldn't find :(

# Extra Credit

- It handles unicode characters(eg. the ü in Süsse or ß in Straße): YES!
- The program can run in a docker container. In this case providing the container is not necessary but a dockerfile that can be built is required: YES! (challenge-nr.Dockerfile)
- The program is capable of processing large files and remains performant. Think about if the program needed to handle 1,000 Moby Dick's at once. What would you need to do? Consider memory consumption and speed.
Without using any extra components (f.e a queue (RabbitMQ or Kafka)), one easy solution is to use threads to divide the load between CPUs using parallelization. This will increase performance.

# Follow up questions:

- What are the steps needed to have this program (or any application) ready for production?

Once the code is pushed to the repository (or created PR, depends on gitflow) code must be tested, compiled(if necessary), and deployed into a test environment where QA team will test it themselves. Best case scenario, once QA team gives the OK to the changes/release, app will be deployed using a canary-testing deployment and monitored in order to find any possible errors. After that, app will be deployed to production.

- What would be the advantages or disadvantages of having a program like this running in a distributed system with a container-orchestration platform?

Advantages:

Horizontal scalability

Program will be SO agnostic (Will run on a container)

Program can be stateless (in this case, books will be stored in some persistent storage, like an S3)

Disadvantages:

Adds complexity to the deployments and platform team

Distributed systems always add extra "delay" because of the requests being made from one microservice to another.

- How would you scale this if you needed to support millions of requests simultaneously? (Imagine the program is complex enough to require it)

I would change the architecture to a Event driven architecture using a pub-sub broker. The publisher will send the request to a Kafka topic, then a consumer will pick it up and process it, saving the output in the desired storage (S3 for example). This allows to virtually scale it indefinitely.