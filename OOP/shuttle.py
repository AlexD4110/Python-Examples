


#copy2() =       copy() + copies metadata (file's cration and modification times)
#copy() = copyfile() + permission mode + destination can be a directory
#copyfile () = copies contents of a file

import shutil

shutil.copyfile('test2.txt', '/Users/alexdeane/Desktop/copy.txt') #src.dst