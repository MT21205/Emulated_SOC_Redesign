# Reference 1: https://docs.python.org/3/library/profile.html
# Reference 2: https://hpc.research.uts.edu.au/software_general/python/python_profiling/

import cProfile
import pstats
import io


profile_obj = cProfile.Profile()
profile_obj.enable()
import Main
profile_obj.disable()
string = io.StringIO()
ps = pstats.Stats(profile_obj, stream=string).sort_stats('tottime')
ps.print_stats()

with open('Profile_Stats.txt', 'w+') as f:
    f.write(string.getvalue())