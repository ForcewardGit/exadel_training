New user comes and can register as:
- a company
- a regular user

Registered user comes and can:
- login / logout

successful login:
    A regular user:
        can create a request for a particular company's service
    A company:
        respong to user requests

offers:
    A company:
        gives an offer
    A regular user:
        Chooses from the list of offers who to work with

reviews:
    A regular user:
        gives review for a particular company

notifications:
    for a company:
        when user has requested a service
        when user accepted an offer
    for a regular user:
        when a company has responded to a request with an offer

=================================================================

APPS:
    sign_up_in_out:
        home/login, home/logout, home/register
        A login / logout / register operations
    service_requests:
        home/requests/create, home/requests
        See what requests we have, create requets(for regular users)
    offers:
        home/offers, home/requests/id/create_offer, home/offers/id/accept
        See which offers a user/company has, make offers from the list of requests(company), accept offers from the list of offers(regular users)
