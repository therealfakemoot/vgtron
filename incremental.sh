rate=1000

while [ $rate -lt 1000000 ]; do
    echo -e "REQUEST RATE: $rate\n"
    ./vegeta attack -targets static_get.conf -duration 5s -rate $rate| tee results.bin | ./vegeta report -reporter plot > ~/public_html/reports/"$rate".html
    let rate=$rate*10
done
