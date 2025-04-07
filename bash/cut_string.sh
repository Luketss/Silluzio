while read line; do
    echo "$line" | cut -b 3
done

#cut more than one pos
while read line; do
    echo "$line" | cut -b 2,7
done