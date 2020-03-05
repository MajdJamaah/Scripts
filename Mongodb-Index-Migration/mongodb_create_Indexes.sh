#!/bin/bash

#example : ./mongodb_create_Indexes.sh indexes {DBNAME} {COLLATIONNAME}

if [ $# -lt 3 ];
then
echo "Please send IndexesFile dbName collectionName"
else
Indexes=$(cat $1)
echo $Indexes
for col in $Indexes
do
mongo $2 --eval 'db.'"${3}"'.createIndex('"${col}"')'
done
fi

