import os
joiner = os.path.join

dirs = [
    joiner("data","raw"),
    joiner("data","processed"),
    "notebooks",
    "saved_models",
    "src",
    
]

for dir_ in dirs:
    os.makedirs(dir_,exist_ok=True)
    with open(joiner(dir_,".gitkeep"),'w'):
        pass
    

file_s = [
    "dvc.yaml",
    "params.yaml",
    joiner("src","__init__.py"),
    # ".gitignore",
    # "README.md"
]
for file_ in file_s:
    with open(file_,"w"):
        pass
        
# we can use cooki cutter for this template easly
