# Eventy

* Source: [Eventy on GitLab](https://gitlab.com/qotto/oss/eventy)
* Package: [Eventy on Pypi](https://pypi.org/project/eventy/)
* Documentation: [Eventy API documentation](https://qotto.gitlab.io/oss/eventy/)

## What is Eventy?

Eventy is both a protocol and a library for making the design of fault-tolerant, event-driven, concurrent and
distributed applications in a microservices-oriented architecture easier.

As a protocol, Eventy is language-agnostic.

However, the reference implementation is written in Python. Whatever is your programming language, you can use Eventy.
If you are using Python, you will be able to make the most of it quicker.

## Motivation

The reality is, a distributed, microservices-oriented architecture is a bit hard to make right.

Martin Fowler even [ended up stating](https://www.drdobbs.com/errant-architectures/184414966):

> First Law of Distributed Object Design: “don't distribute your objects”.

He later [detailed his view](https://martinfowler.com/articles/distributed-objects-microservices.html) of the First Law
regarding microservices.

As Martin Folwer points out, inherently microservices come with their undeniable advantages and a few companies use them
with great success. The only reason why a lot of people end up struggling with microservices, is because it greatly
increases the complexity of the whole system, which makes it harder to get it right.

Eventy is adressing exactly that issue — providing you with a reliable framework to make microservices work for you.

A big part of the design process to create Eventy was to understand different use cases and see how the design can be
simplified. For instance, not only does Eventy offer state partitionning for free, it actually comes up with a few
stratagies that eliminate the need to persist state altogether.

## Inspiration

[Kafka Streams](https://kafka.apache.org/documentation/streams/) was a great influence in making
Eventy. [Celery](http://www.celeryproject.org/) and [Faust](https://github.com/robinhood/faust) are also worth to be
looked at if you are looking for an opiniated framework easy to get started with.

However, these frameworks only partially solve all the issues you will have with microservices. And, in our opinion,
these frameworks are not suitable for designing large critical systems.

They're both opinanated, and therefore cannot be easily integrated in your existing software. You will have to build
your software around the framework, instead of the other way around. They also don't give you the full control on the
way you can use them: you can only use them as a whole, or not at all.

## What Eventy can do for you

Eventy implements multiple features, but all of them simply solve two main problems:

* How to make services communicate with each other
* How to access and persist state

With Eventy, you can serialize data the way you want. You can use [Avro](https://avro.apache.org/)
, [JSON](https://www.json.org/), [gRPC](https://grpc.io/), or whatever customer serializer you like.

With Eventy, you can use any system you like as a persistency layer, as long as it supports transactions, if you need
strong processing guarantees. The most obvious choice is to use [Apache Kafka](https://kafka.apache.org/), but
persisting messages over [PostgreSQL](https://www.postgresql.org/) is completely feasable, too.

Eventy was destined with the mindset of a library of related but independently usable components - and not a framework:
the behaviour is explicit and you're the one in charge: you can design your software your own way.

This explicit behaviour, albeit requiring more boilerplate, gives you better clarity on what is happening. Recipes and
examples are provided so that you can understand how to use Eventy for most use cases.

You're free to use any part of Eventy as well. Even if you end up not using the Eventy protocol at all, simply reading
the documentation and understanding the issues that are adressed and how they are adressed can help you to get on the
right path.

## Main components of Eventy

* a **well-defined communication protocol** for sending various types of persisted messages, called _Records_: _Events_
  , _Requests_ and _Responses_
* **persistency of _Records_** that can be stored forever, which lets you keep track of all the changes in your system (
  especially useful for audits and business analytics)
* **queues** so that _Records_ can be processed asynchroneously, and aren't lost even if your system is down or
  overloaded
* **strong processing guarantees**: a Record can be designed to be processed _at least once_, _at most once_ and _
  exactly once_ even if your system encounters a process or network failure at any point
* **self-propagating _Contexts_** that in many cases entirely eliminate the need of persisting state
* **partitionned state persistency** so that you no longer have a single point of failure in your system (aka _the
  database_) and can scale up as your business grows

# Contribute

Install with dev dependencies:

```
poetry install -E celery -E sanic -E aiohttp -E django -E confluent-kafka -E avro -E requests -E gunicorn
```

Publish on PyPI:

The project uses [poetry](https://python-poetry.org/), to publish the project on [pypi.org/project/eventy](https://pypi.org/project/eventy/) you need:
* Update the version in `pyproject.toml`
* To create a `.pypirc` (similar to the `.pypirc.example`) file in your home directory
* Log in to pypi.org with login and password from bitwarden (the 2FA code is in bitwarden as well)
* Generate a token on pypi.org and add it to the `.pypirc` file
* `make clean build publish`

*Notes*:
* Using an "alpha" version number such as `3.4.2a0` `3.4.2a1` will publish the package as a pre-release. So it will not be resolved by default by poetry, unless explicitly asked for unsing `==3.4.2a0`.  It is a good way to test the package, typically before merging the feature branch.
* Then switching the next real version number, such as `3.4.2` will publish the package as a stable release. So it will be resolved by default by poetry e.g. for `>=3.4.0`.
