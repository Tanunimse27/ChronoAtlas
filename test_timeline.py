from timeline import get_time_window
assert get_time_window(500,10)==(490,510)
assert get_time_window(-499,20)==(-519,-479)
print("All timeline tests passed!")