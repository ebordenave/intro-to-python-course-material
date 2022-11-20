# This
# assignment is specifically
# meant
# to
# test
# your
# understanding
# of
# HTTP
# API
# requests.Please
# write
# code
# for the following functions in a module named homework.py and submit the module file to Grader Than for grading.
#
# You
# will
# need
# to
# use
# the
# following
# APIs in this
# assignment:
#
# https: // swapi.dev / - Use
# this
# to
# retrieve
# Star
# Wars
# information.
#
# https: // openweathermap.org / - Use
# this
# to
# retrieve
# weather
# information.An
# account and API - Key is required
# to
# use
# this
# API.Do
# not attempt
# to
# use
# the
# API
# key
# from my videos
#
# because
# I
# have
# deactivated
# the
# key.You
# do
# not need
# to
# pay
# for the account; the free tier of the API will suffice for this assignment.
#
# https: // restcountries.com - Use
# this
# to
# retrieve
# country
# information.
#
# Below is a
# link
# to
# a
# file
# that
# contains
# a
# list
# of
# US
# Zip
# codes
# mapped
# to
# latitudes and longitudes:
#
# https: // gist.githubusercontent.com / erichurst / 7882666 / raw / 5
# bdc46db47d9515269ab12ed6fb2850377fd869e / US % 2520
# Zip % 2520
# Codes % 2520
# from % 25202013 % 2520
# Government % 2520
# Data
#
# Note:
#
# You
# must
# make
# your
# own
# account
# on
# openweathermap.org and thecatapi.com
# to
# obtain
# an
# API
# key.
#
# The
# functional
# signatures
# with the return types that match "-> List[str]" denote the function is returning a list of strings.For this type-hint pattern to work in your code, you must add from typing import List to your imports.Typing is a builtin python module; you do not need to install anything.
#
#
# def sw_vehicle_search(cargo_capacity: int, max_speed: int, cost: int) -> list:
#     This
#     function
#     will
#     use
#     the
#     https: // swapi.dev / API
#     to
#     collect
#     its
#     information.This
#     function is meant
#     to
#     be
#     used
#     to
#     search
#     for vehicles in Star Wars that meet the specified criteria.The function should return a list of names of the vehicles that have cargo capacities and a max speed greater than or equal to the value specified but also cost less than or equal to the cost given.Vehicles with "unknown" or "none" for any of the mentioned categories should not be regarded.
#
#
# Keep in mind
# that
# not all
# of
# the
# vehicles in star
# wars
# are
# returned in one
# request
# to
# https: // swapi.dev / api / vehicles /.The
# JSON
# object
# returned
# by
# this
# request
# has
# a
# next
# attribute
# that
# represents
# the
# next
# page
# of
# information.You
# must
# make
# multiple
# requests
# for each page to collect all vehicle information.
#
# You
# might
# find
# it
# helpful
# to
# use
# the
# following
# API
# handle(s):
#
# https: // swapi.dev / api / vehicles / - to
# retrieve
# all
# vehicles in Star
# Wars
#
#
# def starship_piloted_species(starship: str) -> list:
#     This
#     function
#     will
#     use
#     the
#     https: // swapi.dev / API
#     to
#     collect
#     its
#     information.This
#     function
#     will
#     be
#     given
#     a
#     string
#     that
#     represents
#     the
#     name
#     of
#     a
#     starship in star
#     wars.It
#     should
#     return a
#     list
#     of
#     names
#     of
#     species
#     that
#     have
#     piloted
#     the
#     specified
#     starship.The
#     order
#     of
#     the
#     list
#     does
#     not matter.If
#     the
#     pilot
#     's species is empty, then the pilot is considered a "Human".
#
#
# You
# might
# find
# it
# helpful
# to
# use
# the
# following
# API
# handle(s):
#
# https: // swapi.dev / api / starships / - to
# retrieve
# all
# starships in Star
# Wars
#
#
# def wear_a_jacket(us_zip: str) -> bool:
#     This
#     function
#     should
#     use
#     https: // openweathermap.org / API(user
#     account
#     required) to
#     collect
#     its
#     weather
#     information.The
#     purpose
#     of
#     this
#     function is to
#     inform
#     you if you
#     should
#     wear
#     a
#     jacket or not.It
#     will
#     be
#     given
#     a
#     US
#     zip
#     code.This
#     function
#     should
#     query
#     the
#     API
#     to
#     figure
#     out
#     the
#     current
#     temperature in the
#     region
#     associated
#     with the US zip code.If the temperature is less than 60 degrees Fahrenheit (main.feels_like <= 60), or it is raining or snowing out (any weather.main in (Rain, Snow)), it will return true.Otherwise, it should return false.
#
#
# Keep in mind
# the
# weather
# attribute in the
# response is a
# list, and you
# have
# to
# check
# all
# elements in the
# list.
#
# You
# might
# find
# it
# helpful
# to
# use
# the
# following
# API
# handle(s):
#
# https: // api.openweathermap.org / data / 2.5 / weather - to
# retrieve
# the
# current
# weather
# conditions
#
#
# def past_weather(days: int, hours: int, minutes: int, us_zip: str) -> float:
#     This
#     function
#     should
#     use
#     https: // openweathermap.org / API(user
#     account
#     required) to
#     collect
#     its
#     weather
#     information.This
#     function
#     should
#     retrieve
#     the
#     historical
#     temperature in Fahrenheit
#     at
#     a
#     particular
#     US
#     location.You
#     will
#     be
#     given
#     a
#     number
#     of
#     days, hours, and minutes and a
#     United
#     States
#     zip
#     code.The
#     time
#     values
#     given
#     are
#     the
#     cumulative
#     total
#     time in the
#     past
#     minus
#     the
#     current
#     time, you
#     should
#     retrieve
#     the
#     historical
#     temperature(current.temp).In
#     other
#     words,
#     if the parameter days is 4 hours is 0 and minutes is 5. Then you should return the temperature 4 days and 5 minutes ago at the specified zip code.
#
#
# Since
# the
# open
# weather
# API
# does
# not have
# a
# method
# querying
# for historical weather with a zip code, please make use of this git hub document that maps US zip codes to latitude and longitude.https://
#     gist.githubusercontent.com / erichurst / 7882666 / raw / 5
# bdc46db47d9515269ab12ed6fb2850377fd869e / US % 2520
# Zip % 2520
# Codes % 2520
# from % 25202013 % 2520
# Government % 2520
# Data
# Keep in mind, you
# might
# need
# to
# remove
# erroneous
# white
# space
# characters
# from the beginning and end
# of
# the
# latitude and longitude
# values in this
# document
# after
# splitting
# the
# line
# with a comma delimiter ",".
#
# You
# might
# find
# it
# helpful
# to
# use
# the
# following
# API
# handle(s):
#
# http: // api.openweathermap.org / data / 2.5 / onecall / timemachine - to
# retrieve
# past
# weather
# information
#
#
# def borders(country_name_a: str, country_name_b: str) -> bool:
#     Using
#     the
#     https: // restcountries.com / API, this
#     function
#     will
#     answer
#     the
#     question, are
#     two
#     countries
#     neighbors? The
#     function
#     will
#     be
#     given
#     two
#     arguments
#     country_name_a and country_name_b.Both
#     arguments
#     are
#     partial
#     names
#     of
#     countries.The
#     function
#     's job is to find all nations with a name that contains country_name_a. Then check whether any countries are neighbors of the matching countries for country_name_b.
#
#
# One
# challenging
# aspect
# of
# this
# problem is that
# the
# country
# 's name will not be complete. For example, the partial country name may be "united" which will yield a long list of possible countries because many countries'
# official
# names
# include
# the
# word
# "united"
# for example, United States of America, United States Minor Outlying Islands, United Republic of Tanzania, United Mexican States, United Arab Emirates, and many more.Your goal is to check if the specified language is spoken in any countries that match the partial name.Use the endpoint https://
#     restcountries.com / v3
# .1 / name / {name}
# to
# get
# a
# complete
# list
# of
# countries
# with the partial name in their official name (replace {name} with the actual country_partial_name argument's value).
#
# The endpoint https://
#     restcountries.com / v3
# .1 / name / {name}
# will
# return a
# lot
# of
# information
# about
# each
# country.The
# critical
# bits
# you
# want
# to
# look
# at
# are
# the
# keys
# "borders" and "cca3".The
# key
# "borders"
# will
# tell
# you
# which
# country(s)
# border
# the
# given
# nation.The
# value
# associated
# with the key "borders" will be a list of 3-letter country codes.Remember that the key "border" will not be in the dictionary if the nation has no neighbors because it's an island. The key "cca3" will tell you the 3-letter country code for the given nation.
#
# The
# function
# should
# return True if a
# country
# matching
# country_name_a
# borders
# a
# country
# matching
# country_name_b.
#
# Example:
#
# assert borders("united", "united")
# assert borders("sweden", "republic")
# assert not borders("united", "tanzania")
# assert not borders("british", "sweden")