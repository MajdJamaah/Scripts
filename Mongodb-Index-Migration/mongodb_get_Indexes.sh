#!/bin/bash

#redirect output to file : ./mongodb_get_Indexes.sh {DBNAME} {COLLATIONNAME} > indexes
if [ $# -lt 2 ];
then
echo "Please send dbName collectionName"
else
mongo --quiet $1 --eval 'for(var l of db.'"${2}"'.getIndexes()){print(JSON.stringify(l.key))}'
fi

