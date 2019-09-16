def lambda_handler(event):
    # TODO implement
    return {
        'event': event["key1"],
        'statusCode': 200,
        'body': 'Hello from Lambda!'
    }


if else
if elif else

for i in range(10)
for i in [1,2,3]
for i in "123"

while(i<10):
	print(i)
	i++


print(lambda_handler({"key1":"Hello Sai"}))

1 23 

"asdf" 'asdf' """asdfasdf
asdfasdf
"""
 abc = [1,2,3,4,5]
 defg = {"key":{1:[34,5,6,75,3]}}


def max(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return None
