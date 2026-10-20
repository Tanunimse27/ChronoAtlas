from timeline import get_time_window , to_internal_year 

assert get_time_window(500,10)==(490,510)
assert get_time_window(-499,20)==(-519,-479)

assert to_internal_year(500,'BCE')==(-499)
assert to_internal_year(500,'CE')==(500)

assert to_internal_year(1,'BCE')==(0)
assert to_internal_year(1,'CE')==(1)
#assert to_internal_year(0,'BCE')==(1)

print("All timeline tests passed!")

from timeline import reverse_internal_year
assert reverse_internal_year(-499)==(500,"BCE")
assert reverse_internal_year(0)==(1,"BCE")
assert reverse_internal_year(1)==(1,"CE")
assert reverse_internal_year(500)==(500,"CE")

print ("All reverse tests passed!")