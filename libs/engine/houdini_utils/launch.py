import hou
import os

here = os.path.dirname(__file__)

#todo : there is a problem when the pipeline shelf is loading on a houdini session with a shelf that already named "pipeline". Fix iiiit

def load_shelves():
    # print "Here : ", here
    shelf_dir = os.path.join(here, 'shelves')
    try:
        from pathlib2 import Path
        for shelf_path in Path(shelf_dir).iterdir():
            shelf_path = str(shelf_path).replace(os.sep, r'/')
            # print shelf_path
            shelf_name = os.path.basename(shelf_path).split('.')[0]
            #print("installing " + shelf_name)
            newShelf = False
            #print("shelf_path = " + shelf_path)
            local_shelf = hou.shelves.defaultFilePath()
            #print("local_shelf = " + local_shelf)
            if os.path.exists(local_shelf):
                hou.shelves.loadFile(local_shelf)
                #print("local shelf loaded")

            #print("shelfSets = " + str(hou.shelves.shelfSets()))
            #print("shelves = " + str(hou.shelves.shelves()))

            if shelf_name not in hou.shelves.shelfSets():
                hou.shelves.loadFile(shelf_path)
                # if shelf_name
                newShelf = True
                #print('Loaded shelf : {}'.format(shelf_name))
                #print("Home = " + str(hou.homeHoudiniDirectory()))
            else:
                print("shelves already exist")

                '''
                if the tool already exist :
                    replace
                 else :
                    add it to the shelf
                '''

    except Exception as e:
        print('Problem loading Pipeline shelves')
        print(e)
                
#load all the hda placed in 03_HDAs
def load_HDAs(hda_lib_path):
    import os
    print(hou.hipFile.path()+" HDA path = "+hda_lib_path)
    dir_list = os.listdir(hda_lib_path)
    print("#######################")
    print("###Try loading HDAs ###")
    print("#######################")
    #print("dirlist = "+str(dir_list))
    for i in dir_list:
        #sprint(i)
        split = i.split(".")
        #print("split = "+str(split))
        if(len(split)>1 and split[-1]=="hdanc"):
            #print("test")
            print("import hda"+i)
            hda_path = hda_lib_path+"/"+i
            hou.hda.installFile(hda_path, change_oplibraries_file=False, force_use_assets=False)
            hou.hda.reloadFile(hda_path)

