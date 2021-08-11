#! /usr/bin/perl
# This perl script runs AFF API SavedSearch using REST

use strict;
use warnings;
use REST::Client;
use JSON;

my $client = REST::Client->new();

#connect to AFF
my $auth = '{"username":"admin", "password":"algosec", "domain":"" }';
$client->POST('https://192.168.0.237/FireFlow/api/authentication/authenticate', $auth, { "Content-type" => 'application/json'});

#build a JSON Hash from response to get sessionId
my $response = from_json($client->responseContent());
my $sessionId = $response->{'data'}{'sessionId'};
print $response