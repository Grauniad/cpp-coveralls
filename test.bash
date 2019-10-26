#!/bin/bash
#
# Run system test.

export PATH="$PATH:$PWD/test-utils"

exit_on_fail="no"
if [[ "$1" == "-e" || "$1" == "--exit-on-fail" ]]; then
    exit_on_fail="yes"
fi

failed_tests=0
function TestFailed {
    let "failed_tests+=1"
    if [[ "$exit_on_fail" == "yes" ]]; then
        echo "(-e): Exiting due to first failure"
        exit 1
    fi
}

testDir.sh $@ test-src/simple || TestFailed

if [[ $failed_tests -gt 0 ]]; then
    echo ""
    echo "FAIL: $failed_tests unexpected failures!"
fi

exit $failed_tests
