import sys

HASH_MOD = 1_000_000_007
MULTIPLIER = 263


def get_bucket_index(value, bucket_count):
    hash_value = 0
    power = 1
    for character in value:
        hash_value = (hash_value + character * power) % HASH_MOD
        power = power * MULTIPLIER % HASH_MOD
    return hash_value % bucket_count


input_data = sys.stdin.buffer
bucket_count = int(input_data.readline())
query_count = int(input_data.readline())
buckets = [[] for _ in range(bucket_count)]
answers = []

for _ in range(query_count):
    query = input_data.readline().split()
    operation = query[0]

    if operation == b"add":
        value = query[1]
        bucket = buckets[get_bucket_index(value, bucket_count)]
        if value not in bucket:
            bucket.insert(0, value)
    elif operation == b"del":
        value = query[1]
        bucket = buckets[get_bucket_index(value, bucket_count)]
        if value in bucket:
            bucket.remove(value)
    elif operation == b"find":
        value = query[1]
        bucket = buckets[get_bucket_index(value, bucket_count)]
        answers.append("yes" if value in bucket else "no")
    else:
        bucket_index = int(query[1])
        answers.append(" ".join(value.decode() for value in buckets[bucket_index]))

sys.stdout.write("\n".join(answers))