./pyyc ./tests/mytests/test1.py

gcc -m32 -g tests/mytests/test1.s runtime/libpyyruntime.a -lm -o tests/mytests/test1

cat tests/mytests/test1.in | tests/mytests/test1 > tests/mytests/test1.out

cat tests/mytests/test1.in | python3.10 tests/mytests/test1.py > tests/mytests/test1.expected

diff -w -B -u tests/mytests/test1.expected tests/mytests/test1.out


---------------------------------------------------------------

./pyyc ./tests/autograde/p0/hard/nested_op.py

gcc -m32 -g ./tests/autograde/p0/hard/nested_op.s runtime/libpyyruntime.a -lm -o ./tests/autograde/p0/hard/nested_op

cat ./tests/autograde/p0/hard/nested_op.in | ./tests/autograde/p0/hard/nested_op > ./tests/autograde/p0/hard/nested_op.out

cat ./tests/autograde/p0/hard/nested_op.in | python3.10 ./tests/autograde/p0/hard/nested_op.py > ./tests/autograde/p0/hard/nested_op.expected

diff -w -B -u ./tests/autograde/p0/hard/nested_op.expected ./tests/autograde/p0/hard/nested_op.out

-----------------------------------------------------------------
cd tests
pytest --pyyctests autograde
