#!/bin/bash
grep -oE '[0-9]{7,9}' annonces.csv | sort -u > /tmp/existing_ids.txt
for id in 13760409 13115369 17741131 24127765 15630258 14595489 22908221 23483491 14106307; do
  if grep -q "^${id}\$" /tmp/existing_ids.txt; then
    echo "$id ALREADY IN CSV"
  else
    echo "$id new"
  fi
done
