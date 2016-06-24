function incremental_test(rate, duration, test_conf) {
    #Setting the max rate should be configurable, but I don't want to have too many command line parameters. env var maybe?
    while [ $rate -lt 1000000 ]; do 
        echo -e "REQUEST RATE: $rate per second\n"
        ./vegeta attack -targets $test_conf -duration $duration -rate $rate -output "$test_conf"."$rate".bin
        ./vegeta report -inputs "$test_conf"."$rate".bin
        #Report output probably shouldn't ASSUME you've got public_html/. Maybe dump the output to ./.reports/ or something? Use your best judgement here.
        #Also, it'd be nice but not strictly necessary to include a timestamp on reports, so we can rerun tests without blowing away previous recorded data.
        ./vegeta report -inputs "$test_conf"."$rate".bin -reporter plot > ~/public_html/reports/"$test_conf"."$rate".bin
        echo -e "Report generated: '$test_conf'.'$rate'.html"
        #The rate increment 'step' should be configurable as well.
        let rate=$rate*10
    done
}

function main() {
find ./tests/ -type f -exec incremental_test($1, $2, {}) \; 
#This is the gist of what I want. Go over tests one at a time and run through the increments.
#Also, help output would be nice, but not necessary.
}

main()
