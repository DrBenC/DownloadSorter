import os
import glob

x = os.getcwd()

#all top level folders which your files will be sorted into
subfolders = ["images", "videos", "models", "cif", "documents",
              "scripts", "presentations", "references", "torrent",
              "exe", "uf2", "data"]
              
image_types = ["jpg", "jpeg", "png", "bmp", "tif", "gif", "jfif", "JPG"]
video_types = ["avi", "mp4", "mpeg", "mov"]
doc_types = ["doc", "docx", "pdf", "pub", "PDF", "dotx"]
data = ["txt", "csv", "opju", "xls", "xlsx", "res", "mol2", "x3d", "wrl"]
scripts = ["py"]
references = ["ris", "bib", "enw", "nbib"]
presentations = ["pptx", "ppsx", "PPT"]
models = ["stl", "obj", "3mf", "f3d", "gcode", "STL"]

#this neat little loop checks the presence of folders and screates them if they don't exist
for i in subfolders:
    if os.path.exists(f"{x}/{i}"):
        print(f"{i} folder present")
    else:
        os.mkdir(i)
        print(f"{i} folder not present, folder added to {x}")


#takes stock of all folders in current working directory
loose_files = (glob.glob(f"{x}/*.*"))

for f in loose_files:
    file = f.split("\\")[-1]
    file_extension = str(f.split(".")[-1]).lower()

    if file_extension in subfolders:
        os.replace(file, f"{file_extension}/{file}")
        print(f"Moving {file} to {file_extension}")
        
    elif file_extension in image_types:
        os.replace(file, f"images/{file}")
        print(f"Moving {file} to images")
    
    elif file_extension in video_types:
        os.replace(file, f"videos/{file}")
        print(f"Moving {file} to videos")
        
    elif file_extension in doc_types:
        os.replace(file, f"documents/{file}")
        print(f"Moving {file} to documents")
        
    elif file_extension in scripts and file != "sorter.py":
        os.replace(file, f"scripts/{file}")
        print(f"Moving {file} to scripts")
        
    elif file_extension in references:
        os.replace(file, f"references/{file}")
        print(f"Moving {file} to references")
        
    elif file_extension in presentations:
        os.replace(file, f"presentations/{file}")
        print(f"Moving {file} to presentations")
        
    elif file_extension in models:
        os.replace(file, f"models/{file}")
        print(f"Moving {file} to models")
        
    elif file_extension in data:
        os.replace(file, f"data/{file}")
        print(f"Moving {file} to data")
