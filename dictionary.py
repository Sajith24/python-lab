d={1:2,3:4,4:3,2:1,0:0}
print("dictionary is",d)
sorted_d=dict(sorted(d.items()))
print("dictionary sorted in ascending order is:",sorted_d)
sorted_b=dict(sorted(d.items(),reverse=True))
print("dictionary sorted in descending order is:",sorted_b)
