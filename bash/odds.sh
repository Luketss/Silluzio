i=1

while [[ $i -le 99 ]] ; do
    if [ $(($i % 2)) != 0 ]; then
        echo $i
    fi
    (( i+= 1))
done


for i in {1..99}
do
    if [ $(($i % 2)) != 0 ]; then
        echo $i
    fi
done