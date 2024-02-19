# Combine SETS with the UNION function
S1 = {1,2,3}
S2 = {"A", "B", "C"}

# Create S3 by Merging set S2 with S1 using UNION function
S3 = S1.union(S2)
print(S3)

# Create S3 by Merging set S2 with S1 using | operator
S3 = S1 | S2
print(S3)