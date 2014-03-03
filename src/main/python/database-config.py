#!/usr/bin/env python

#    Copyright 2013 meltmedia
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

# Simple script to take database configuration and write it out in a json format. If incomplete data is given
# then no json file is produced.

# Note: This assumes the uri wiill be a jdbc connection to a mysql database.

from optparse import OptionParser
import sys
import json

parser = OptionParser()

# Setup options for the parser
parser.add_option("-n", "--dbname", dest="dbname",
                  help="Database Name to use on the database server")
parser.add_option("-u", "--dbusername", dest="dbusername",
                  help="Username for the database server")
parser.add_option("-p", "--dbpassword", dest="dbpassword",
                  help="Password for the database server")
parser.add_option("-a", "--dbaddress", dest="dbaddress",
                  help="Address for the database server")
parser.add_option("-r", "--dbport", dest="dbport",
                  help="Port for the database server")
parser.add_option("-o", "--output", dest="output",
                  help="Destination to output the config")

(options, args) = parser.parse_args()

# Output destination is always required
if not options.output:
    print >> sys.stderr, "No output specified"
    exit(1)    

if (not options.dbname or options.dbname == "N/A") or \
    (not options.dbusername or options.dbusername == "N/A") or \
    (not options.dbpassword or options.dbpassword == "N/A") or \
    (not options.dbaddress or options.dbaddress == "N/A") or \
    (not options.dbport or options.dbport == "N/A"):
    print >> sys.stdout, "Incomplete database information given. Ignoring..."
    exit(0)

# Construct the database uri (currently very specific for mysql and UTF-8 character encoding)
uri = "jdbc:mysql://" + options.dbaddress + ":" + options.dbport + "/" + options.dbname + "?characterEncoding=UTF-8"

# Build the attributes
attributes = {"database" : { "config" : { "source" : "attributes", "username" : options.dbusername, "password" : options.dbpassword, "uri" : uri, "database" : options.dbname, "address": options.dbaddress, "port": options.dbport}}}

f = open(options.output, 'w')
f.write(json.dumps(attributes))
f.close()



