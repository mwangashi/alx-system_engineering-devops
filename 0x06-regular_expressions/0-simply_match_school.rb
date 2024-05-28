#!/usr/bin/env ruby
#Simply matching School

string = ARGV[0]
regex = /School/
matches = string.scan(regex)
puts matches
