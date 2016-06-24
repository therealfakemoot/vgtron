rate=1000

while [ $rate -lt 1000000 ]; do
    echo -e "REQUEST RATE: $rate per second\n"
    ./vegeta attack -targets static_get.conf -duration 5s -rate $rate -output "$rate".bin
    ./vegeta report -inputs "$rate".bin
    ./vegeta report -inputs "$rate".bin -reporter plot > ~/public_html/reports/"$rate".html
    echo -e "Report generated: '$rate'.html"
    let rate=$rate*10
done
