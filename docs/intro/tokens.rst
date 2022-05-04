.. _tokens:

=================
Getting a license
=================

This SDK works by routing function calls to Inspiration-Q's online API. Thus,
code that uses this library needs

1. a stable and fast internet connection to the API server, and
2. access tokens that authorize the code to consume the API.

Currently, Inspiration-Q offers three consumption models and ways to get those
access tokens.

Rapid API
=========

Rakuten's Rapid API is an online service that intermediates the access to third
party API's. It offers a self-subscription model where the user may open an
account and consume API's from different providers, without intermediation from
those providers.

Inspiration-Q's API is offered at `Rapid API's marketplace
<https://rapidapi.com/inspiration-q-inspiration-q-default/api/inspiration-q>`_
By choosing any of our suscription models, you will be provided a secret key
that can be used to gather access tokens.

    .. code-block:: python3

        from inspirationq.api.rapidapi import rapidapi_credentials
        credentials = rapidapi_credentials("your_secret_key")

AWS API Gateway
===============

Inspiration-Q also offers access tokens and registration of users via Amazon AWS'
API Gateway. This model is currently available only under contractual relations.
The programming interface is slightly different, in that access is controlled by
a user-password combination:

    .. code-block:: python3

        from inspirationq.api.aws import aws_credentials
        credentials = aws_credentials("inspirationq", "some_password")

On-premise installations
========================

As part of our licensing model, Inspiration-Q also offers secured installations
on premise for our clients. The access model is similar to AWS API Gateway, with
the only difference that the user must provide the IP for the locally installed copy:

    .. code-block:: python3

        from inspirationq.api.aws import sam_credentials
        credentials = sam_credentials("inspirationq", "some_password",
                                      base_url='http://127.0.0.1:3000/')

Disclaimer
==========

All of Inspiration-Q's secured API's are controlled by secret information that
is unique to each user. The user is responsible for keeping that information safe
and not sharing it with third parties. Inspiration-Q will not reimburse any costs
that result from a misusue of those credentials.