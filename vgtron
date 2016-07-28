#!/bin/bash


incremental_test() {
    output_dir="$(dirname $4)_data"
    test_start=$(date +"%Y-%m-%d_%H-%M-%S")

    #read -p "Engintron? y/n" engine
    #TODO: Amend the output filename generation to include whether nginx or apache is handling the test.

    #Setting the max rate should be configurable, but I don't want to have too many command line parameters. env var maybe?
    while [ $rate -lt $maxrate ]; do 
        echo -e "REQUEST RATE: $rate per second\n"
        vegeta attack -targets $4 -duration $2 -rate $rate -output "$output_dir/$test_start"."$rate".bin
        let rate=$rate + $3

    #echo "$request http://$hostname" |./vegeta attack -duration $duration -rate 1
    done
}

help() {
  cat <<EOF
Example Invocations:

# Flags
#All invocations
-d Duration (in seconds)
-r Rate (requests per second)
-s Step (rate increase between tests)

#Dynamic
-v HTTP verb #Default to GET
-t target hostname

#Target File
-f Target File

# The Dynamic and Target File flag groups are mutually exclusive with each other.

# ./vgtron -f all -d 30s -r 10000 -s 50


# ./vgtron tests/posts/write 30s 10000 50

EOF

}

case $@ in
    -h|--help) help;

    -d|--duration)
        duration="$1"
        shift 1;
    -r|--rate)
        rate="$1"
        shift 1;
    -s|--step)
        step="$1"
        shift 1;
    -v|--verb)
        verb="$1"
        shift 1;
    -t|--target)
        target="$1"
        shift 1;

    -f|--file)
        file="$1"
        shift 1;
esac

# 
#find ./tests/ -type f -exec incremental_test($1, $2, {}) \; 
