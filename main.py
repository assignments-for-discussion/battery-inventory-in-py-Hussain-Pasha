
def count_batteries_by_usage(cycles):
  count_low=0
  count_medium=0
  count_high=0
  for i in cycles:
    if i<400:
      count_low += 1
    elif i>=400 and i<=900 :
      count_medium +=1
    elif i>=900 :
      count_high += 1
  return {
    "lowCount": count_low,
    "mediumCount": count_medium,
    "highCount": count_high
  }


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
