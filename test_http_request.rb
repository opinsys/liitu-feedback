# This script can be used to test f.ex. http post request from a client app
# requires packages: rubygems libsinatra-ruby

require 'rubygems'
require 'sinatra'

get '/' do
  puts params.inspect
  "GET"
end

post '/' do
  puts params.inspect
  "POST"
end

#curl -s -d'test=test' -D- http://localhost:4567/ -o/dev/null
