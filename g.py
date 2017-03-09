#import org.gephi.profrom  import ProjectController
#ProjectController().newProject()
#workspace = ProjectController().getCurrentWorkspace()
#print workspace

import org.gephi.project.api as project
from org.openide.util import Lookup
def ProjectController(lookup):
    return lookup(project.ProjectController)

def main():
    lookup = Lookup.getDefault().lookup
    pc =ProjectController(lookup)
    pc.newProject()
    workspace = pc.getCurrentWorkspace()
    print workspace

if __name__=='__main__':main()
